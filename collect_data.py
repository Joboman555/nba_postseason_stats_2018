#!/bin/python2
# Scrape NBA player data from NBA website

from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import os
import re

OUTPUT_FILE = 'postseason_stats_2018.csv'

def output(line):
	with open(OUTPUT_FILE, 'a') as f:
		print(line, file=f)


def scrape_data_for(team, printHeader=False):
	page = requests.get("http://www.espn.com/nba/team/stats/_/name/{}".format(team))
	soup = BeautifulSoup(page.content, 'html.parser')
	try:
		stat_rows = soup.find('table').find_all('tr')
	except:
		print("Parsing failed for team: {}".format(team))
		quit()
	if printHeader:
		header = soup.find('table').find('tr', class_='colhead')
		print("Writing Header")
		fields = [cell.get_text() for cell in header.find_all("td")] + ['TEAM']
		output(','.join(fields))
	for row in soup.find('table').find_all('tr', {"class" : re.compile("player*")}):
		fields = [cell.get_text().split(',')[0] for cell in row.find_all("td")] + [team]
		print("Writing {}".format(fields[0]))
		output(','.join(fields)) 

try:
	os.remove(OUTPUT_FILE)
except OSError:
	pass

playoff_teams=['HOU', 'MIN', 'OKC', 'UTAH', 'POR', 'NOR', 'GSW', 'SAS', 'TOR', 'WAS', 'CLE', 'IND', 'PHI', 'MIA', 'BOS', 'MIL']
print(len(playoff_teams))
scrape_data_for(playoff_teams[0], printHeader=True)
for team in playoff_teams[1:]:
	scrape_data_for(team, printHeader=False)

