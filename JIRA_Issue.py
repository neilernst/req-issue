from collections import defaultdict

class JIRA_Issue: 
	""" A class to hold data about issues relevant to requirements"""
	events = dict(
		comment = [],
		issue_open = [],
		issue_close = [],
		issue_field_change = [])

	unique_authors = defaultdict(int)

	issue_num = ''

	def __init__(self, issue_num):
    		self.issue_num = issue_num

    	def __repr__(self):
		return "Test()"
	def __str__(self):
		return "Issue: " + str(self.issue_num) + '\nEvents: ' + str(self.events) + '\nAuthors: ' +str(self.unique_authors)