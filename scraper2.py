import re
from datetime import datetime
from bs4 import BeautifulSoup
from time import sleep
import requests
import pytz
from collections import OrderedDict
import pandas as pd 
import cloudscraper

url = "https://www.hltv.org/results?startDate=2023-04-17&endDate=2023-04-18"

#HTTP GET Requests
page = requests.get(url)

def get_page_html(url, sleep_time=0):
  sleep(sleep_time)
  cscraper = cloudscraper.create_scraper()
  response = cscraper.get(url)
  html = response.text
  bs = BeautifulSoup(html, 'html.parser')
  #print(results_html.encode("utf-8"))
  #print(results_html)
  list_all_matches = bs.findAll('div', class_='result-con')
  #print(list_all_matches)
  #print(len(list_all_matches))
  matches = list_all_matches[0]
  print(matches)
  for link in matches.find_all('a'):
    print(link.get('href'))




#get_page_html(url)

r_url = "https://www.hltv.org/ranking/teams/2023/april/24"

def export_table(data):
  table = pd.DataFrame(data, columns=['Team_Name', 'Team_Rank', 'Team_Page'])
  table.index = table.index + 1 
  table.to_csv(f'teams.csv', sep=',', encoding='utf-8',index=False)
  #print(table)

team = []
def get_teams(team):
  for team in top30:
      name = team.find('span', class_='name').text
      #print(name)
    
      rank = team.find('span', class_='position').text
      #print(rank)
      global team_id
      team_page = team.find('a', {'class' : 'moreLink'})
      team_id = team_page.get('href')
      
      #print(link)
      data['Team_Name'].append(name)
      data['Team_Rank'].append(rank)
      data['Team_Page'].append(team_id)

      #print(data)
  #print(team)
  

sleep(0)
cscraper = cloudscraper.create_scraper()
response = cscraper.get(r_url)
html = response.text
if page.status_code == requests.codes.ok:
  print("Everything is cool")
  bs = BeautifulSoup(html, 'html.parser')
  #print(results_html.encode("utf-8"))
  #print(bs)
  top30 = bs.findAll('div', class_='ranked-team standard-box')
  data = {
    'Team_Name': [],
    'Team_Rank': [],
    'Team_Page': [],
  }
  #print(top30)
  #print(len(top30))
  #print(team)

def parse_page(next_url):
  page = requests.get(next_url)
  # Checking if we succesfully fetched the URL
  if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(html, 'html.parser')


#HTTP GET Requests
page2 = requests.get(r_url)
#get_teams(team)
#export_table(data)
    #for link in team.find_all('a'):
      #print(link.get('href'))
#print(data)

team_df = pd.read_csv("C:/Users/niki/Documents/hltv/oma_hltv/teams.csv")
team_df['Team_Page']
#print(team_df['Team_Page'])


#team_df['Team_Page'] = team_df['Team_Page'].apply(lambda x: str(x).replace('/', '='))

#print(team_df['Team_ID'])

#result_url = "https://www.hltv.org/results?team={team_id}"

def get_team_matches():
  team_df = pd.read_csv("C:/Users/niki/Documents/hltv/oma_hltv/teams.csv")
  team_df['Team_ID'] = team_df['Team_Page'].str.split('/').str[2]
  team_url_list = list(team_df['Team_ID'])
  for team_page in team_url_list:
    #print(team_page)
    url = f"https://www.hltv.org/results?team={team_page}"
    print(url)

get_team_matches()
