""" Parse all project JIRA issues of the given type
    and pass them to parse_jira"""

import urllib2
import json
import datetime
from parse_jira import parse_issue

prot = 'https://'
query_url = 'issues.apache.org/jira/rest/api/latest/search?maxResults=100&jql='
query = "project='LUCENE' AND (status='In Progress' OR status=Open) AND type='New Feature' AND priority=Major"

url = prot + query_url + urllib2.quote(query)
try:
    data = urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print "HTTP error: %d" % e.code
except urllib2.URLError, e:
    print "Network error: %s" % e.reason.args[1]

issues = json.load(data)['issues']
for issue in issues:
    x = parse_issue(issue['key'])
    # do something ...
    print x.get_fixed_in()
