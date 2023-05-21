import re
from datetime import datetime
from bs4 import BeautifulSoup
from time import sleep
import requests
import pytz
from collections import OrderedDict
import pandas
import cloudscraper

url = "https://www.hltv.org/results?startDate=2023-04-17&endDate=2023-04-18"
def scrape_match_list(start_date, end_date, sleep_time = 0.05, update_csv=True):
    """
    Gets list of all matches in date range.  List format: ['ID', 'DATE', 'TITLE', 'URL', 'TEAMS', 'WINNER', 'SCORE']
    Saves to csv by default.
    Does not check if matches within date range are already saved.
    """

    results_url = f"https://www.hltv.org/results?startDate=2023-04-25&endDate=2023-04-24"

    match_list = []

    next_page_exists = True
    while next_page_exists:

        results_page_html = get_page_html(results_url, sleep_time = sleep_time)
        results_holder = results_page_html.find('div', {'class':'results-holder allres'})
        match_list_htmls = results_holder.find_all('div', {'class':'result-con'})

        for match in match_list_htmls:
            match_url = "https://www.hltv.org" + match.find('a', {'class':'a-reset'})['href']
            match_id, match_title = get_match_id_title(match_url)
            match_date_unix = match['data-zonedgrouping-entry-unix']
            match_date = datetime.fromtimestamp(int(match_date_unix)/1000).strftime('%Y-%m-%d')

def get_page_html(url, sleep_time=0):
    sleep(sleep_time)
    cscraper = cloudscraper.create_scraper()
    response = cscraper.get(url)
    html = response.text
    match_html = BeautifulSoup(html, 'html.parser')
    #print(match_html.encode("utf-8"))
    print(match_html)

get_page_html(url)


