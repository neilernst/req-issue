import urllib2
import json
import datetime
from Jira_Issue import Jira_Issue

DB_LOC = '/Users/nernst/Dropbox/research/projects/req-issues/'
DB_NAME = 'lucene-features.db'


def parse_issue(issue_arg):
    """ Return a Jira_Issue for the given issue argument"""
    #ssue_pre = 'LUCENE-'
    issue_num = issue_arg
    base_url = 'https://issues.apache.org/jira/rest/api/latest/issue/'

    url = base_url + issue_num
    issue = Jira_Issue(issue_num)
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


def store_issue(issue):
    """ Store a Jira_Issue in the database"""
    import sqlite3
    conn = sqlite3.connect(DB_LOC + DB_NAME)
    c = conn.cursor()
    insert_stmt = 'INSERT INTO work_item (name, summary, tool_id, url, created, \
            creator_text, closed, issue_type, fix_version) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'

    c.execute(insert_stmt, (issue.name, issue.summary, issue.issue_num, issue.url,
            issue.events['issue_open'], issue.creator_name, issue.events['issue_close'],
            'New Feature', issue.fix_version))  # use ? interpolation with issue instance

    conn.commit()
    conn.close()
