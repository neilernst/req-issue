def scrape(page):
    from bs4 import BeautifulSoup
    file = open(page,'r')
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
    created = soup.select('.dates #create-date')[0].get_text().strip() #TODO returns human readable dates, must convert
    updated = ''
    try:
        updated = soup.select('.dates #updated-date')[0].get_text().strip() #TODO returns human readable dates, must convert
    except:
        pass #print "not yet modified"
    print related_issues,conv_date(created)
    if updated:
        print conv_date(updated)#,item_sum.get_text()
    #issue_open
    #issue_close

def conv_date(dtstr):
    #convert dates from human readable
    import datetime, re
    days = {'Monday':0, 'Tuesday':1, 'Wednesday': 2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday': 6}
    # format: "Today 9:49 AM" - and we don't care about the time.
    td = re.match('Today', dtstr)
    #tm = re.match('Tomorrow', dtstr)
    yd = re.match('Yesterday', dtstr)
    day = re.match('[a-zA-Z]*day', dtstr)
    if day:
        day = day.group(0)
    today = datetime.date.today()
    if td:
        return today
    elif yd:
        return today -  datetime.timedelta(days=1)
    elif day and not (td or yd):
        dw = today.weekday() - days[day]   # 0 = monday
        if dw < 0:
            dw = dw + 7
        return today - datetime.timedelta(days=dw)
    else:
        # a 'normal' datestring of format 13/Mar/13 9:49 AM
        return datetime.datetime.strptime(dtstr, "%d/%b/%y %I:%M %p")

def test_date():
    print "testing date conversion"
    print conv_date("Today 9:49 AM")
    print conv_date("Tuesday 10:11PM")
    print conv_date("Monday 3:53 PM")
    print conv_date("Friday 3:53 PM")
    print conv_date("19/Mar/12 12:47 PM")

if __name__ == '__main__':
    test_date()
    scrape('CONN-313.html')
