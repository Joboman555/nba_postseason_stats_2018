#!/bin/python2
# Scrape NBA player data from NBA website

from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import os

OUTPUT_FILE = 'postseason_stats_2018.csv'

def output(line):
	with open(OUTPUT_FILE, 'a') as f:
		print(line, file=f)


def scrape_data_for(team):
	page = requests.get("http://www.espn.com/nba/team/stats/_/name/{}".format(team))
	soup = BeautifulSoup(page.content, 'html.parser')

	stat_rows = soup.find('table').find_all('tr')
	for row in stat_rows:
		fields = [cell.get_text() for cell in row.find_all("td")]
		output(','.join(fields)) 

try:
	os.remove(OUTPUT_FILE)
except OSError:
	pass

scrape_data_for('CLE')
