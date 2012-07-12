# Requirements in Tasks
This project is looking at how requirements are manifested in development processes, particularly as tasks.

## Parsing
One objective is to automatically generate stats from JIRA or other ALM tools. These include things like number of commenters on an issue, issue duration, and so on. 

### Data sources
* [JIRA REST API](http://docs.atlassian.com/jira/REST/latest/)
    * Sample: https://issues.apache.org/jira/rest/api/latest/issue/LUCENE-1458

### Wishlist
- blocks/blocked by
- summary of description
- Eric's work on elicit vs understand
- collect the extended event data on issue modification
- type and priority, resolution (fixed,wontfix etc)
- parse comments for relevant SVN commit ids

## Qualitative study
The other objective is to reconstruct feature narratives to understand what is going on with a feature when people build software. It seems like there will be patterns to software development. A rough cut might suggest that there are complex issues, where things have to be re-investigated, dead ends, where issues never get completed, simple issues that are quickly resolved, and so on. The idea is to go beyond 'bug fixes' as a way of characterizing software development activity. 