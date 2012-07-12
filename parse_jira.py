import urllib2
import json
import datetime
from JIRA_Issue import JIRA_Issue


def parse_issue(issue_arg):
    """ Return a JIRA_Issue for the given issue argument"""
    #ssue_pre = 'LUCENE-'
    issue_num = issue_arg
    base_url = 'https://issues.apache.org/jira/rest/api/latest/issue/'

    url = base_url + issue_num
    issue = JIRA_Issue(issue_num)
    print url

    try:
        data = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
        print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
        print "Network error: %s" % e.reason.args[1]

    objs = json.loads(data)

    # comments and participants
    comments = objs['fields']['comment']['comments']
    num_comments = len(comments)
    resolve = objs['fields']['resolutiondate']
    opened = objs['fields']['created']
    issue.events['issue_open'] = \
        datetime.datetime.strptime(opened[:-9], '%Y-%m-%dT%H:%M:%S')
    try:
        issue.events['issue_close'] = \
            datetime.datetime.strptime(resolve[:-9], '%Y-%m-%dT%H:%M:%S')
    except TypeError, e:
        issue.events['issue_close'] = None  # not yet closed
    try:
        issue.fix_version = objs['fields']['fixVersions'][0]['name']
    except IndexError, e:
        # there was no assigned version this will be applied to
        issue.fix_version = 'TBD'

    for c in comments:
        author = c['updateAuthor']['name']
        issue.unique_authors[author] += 1
        created = c['created']
        created = datetime.datetime.strptime(created[:-9], '%Y-%m-%dT%H:%M:%S')
        issue.events['comment'].append(created)

    return issue
