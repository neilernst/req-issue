from collections import defaultdict
import datetime


class JIRA_Issue:
    """ A class to hold data about issues relevant to requirements"""

    def get_duration(self):
        """ report how many days this issue was open for or has been open"""
        if self.events['issue_close'] is not None:
            return (self.events['issue_close'] - self.events['issue_open']).days
        else:
            return (datetime.datetime.today() - self.events['issue_open']).days

    def get_fixed_in(self):
        return self.fix_version

    def __repr__(self):
        return "Test()"

    def __str__(self):
        return "Issue: " + str(self.issue_num) + '\nEvents: ' + \
            str(self.events) + '\nAuthors: ' + str(self.unique_authors)

    def __init__(self, issue_num):
        self.issue_num = issue_num
        self.events = dict(
            comment=[],
            issue_open=None,
            issue_close=None,
            issue_field_change=[])

        self.unique_authors = defaultdict(int)
        self.fix_version = None
        #self.issue_num = None
        self.creator_name = None
        self.name = None
        self.summary = None
        self.url = None

