from bs4 import BeautifulSoup
file = open('CONN-313.html','r')
soup = BeautifulSoup(file)

issue_field = {}
try:
    issue_field['type'] = soup.select('#type-val')[0].get_text().strip()
    issue_field['status'] = soup.select('#status-val')[0].get_text().strip()
    issue_field['priority'] = soup.select('#priority-val')[0].get_text().strip()
    issue_field['resolution'] = soup.select('#resolution-val')[0].get_text().strip()
    issue_field['versions'] = soup.select('#versions-val')[0].get_text().strip()
    issue_field['components'] = soup.select('#components-val')[0].get_text().strip()
    issue_field['LOE'] = soup.select('#customfield_10020-val')[0].get_text().strip()
    issue_field['reporting_org'] = soup.select('#customfield_10041-val')[0].get_text().strip()
    issue_field['description'] = soup.select('#issue-description')[0].get_text().strip()
    issue_field['points'] = soup.select('#customfield_10060-val')[0].get_text().strip()
except: 
    pass

#print(issue_field)
#item summary
item_sum = soup.select('.item-summary')[0]
links = soup.select('#outwardLinks_table .flooded a[href]')
related_issues = []
for link in links:
    related_issues.append(link.attrs['href'])
created = soup.select('.dates #create-date')[0].get_text().strip() #TODO returns human readable dates, myst convert
updated = ''
try:
    updated = soup.select('.dates #updated-date')[0].get_text().strip() #TODO returns human readable dates, myst convert
except:
    print "not yet modified"
print related_issues,created,updated,item_sum.get_text()
#issue_open
#issue_close
