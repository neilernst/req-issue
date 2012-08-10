"""
Find the set of developers in an HG repository
"""

from collections import defaultdict
import csv
from mercurial import ui, hg

repo = hg.repository(ui.ui(), '.')

devs = defaultdict(int)
for i in range(0,len(repo)):
	devs[repo[i].user()] += 1

dev_writer = csv.writer(open('devs.csv','wb'))
for dev in devs:
	dev_writer.writerow([dev,devs[dev]])

