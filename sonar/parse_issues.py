import xml.etree.ElementTree as ET
import urllib
import urllib2

api_url = 'https://jira.codehaus.org/rest/api/latest/project/SONAR'
#issue/

tree = ET.parse("/Users/nernst/Dropbox/research/projects/req-issues/sonar/sonar-new-feature.xml")
root = tree.getroot()
tasks = {}
for elem in root.findall('Task'):
    tasks[elem.get('Key')] = elem.get('Label')

# for each task get the associated comments on that issue
for task in tasks.keys():
	url = api_url + '/issue/' + task
	response = urllib2.urlopen(url).read()
