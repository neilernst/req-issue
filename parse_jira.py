import urllib2, json, datetime
from JIRA_Issue import JIRA_Issue

issue_pre = 'LUCENE-'
issue_num = '1458'
base_url = 'https://issues.apache.org/jira/rest/api/latest/issue/'

url = base_url + issue_pre + issue_num
issue =  JIRA_Issue(issue_num)

try:
	data = urllib2.urlopen(url).read()
	objs = json.loads(data)#sort_keys=True, indent=4)
except urllib2.HTTPError, e:
	print "HTTP error: %d" % e.code
except urllib2.URLError, e:
	print "Network error: %s" % e.reason.args[1]

# comments and participants
comments = objs['fields']['comment']['comments']
num_comments =  len(comments)

issue.events['issue_open'] = objs['fields']
for c in comments: 
	author = c['updateAuthor']['name']
	issue.unique_authors[author] += 1
	created = c['created']
	created = datetime.datetime.strptime(created[:-9],'%Y-%m-%dT%H:%M:%S')
	issue.events['comment'].append(created)

print issue



# find all other events. Comments, modifications. 