from bs4 import BeautifulSoup
file = open('CONN-313.html','r')
soup = BeautifulSoup(file)
#print(soup.prettify())
#print(soup.title)
print(soup.find_all(id='issuedetails'))