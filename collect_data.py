#!/bin/python
# Scrape NBA player data from NBA website

import requests
from bs4 import BeautifulSoup


page = requests.get("http://www.espn.com/nba/team/stats/_/name/cle")
soup = BeautifulSoup(page.content, 'html.parser')

stat_rows = soup.find('table').find_all('tr')
for row in stat_rows:
	cells = row.find_all("td")
	print ','.join(cells) 

