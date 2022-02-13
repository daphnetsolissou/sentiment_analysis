import requests
import pandas as pd
import sys
import time
from datetime import datetime, timedelta
from dotenv import dotenv_values
import os

root_dir = os.path.dirname(__file__)
print(f'My root {root_dir}')
config = dotenv_values(os.path.join(root_dir, ".env"))
URL = 'https://newsapi.org/v2/everything'
try:
    KEY = config['API_KEY']
except KeyError:
    print("Provide a .env file with the API_KEY.")
    sys.exit()


class NewsDownloader:

    def __init__(self, query, paginate=False, sleep_time=10, year=None):
        if year is None:
            year = datetime.today().year
        self.year = year
        self.paginate = paginate
        self.sleep_time = sleep_time
        date_from, date_to = self.create_from_to_dates()
        self.params = {'q': query,
                       'apiKey': KEY,
                       'page': 1,
                       'pageSize': 100,
                       'from': date_from,
                       'to': date_to,
                       'language': 'en'
                       }

    def create_from_to_dates(self):
        today = datetime.today().strftime('%Y-%m-%d')
        one_month_before = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
        try:
            past_year = (int(self.year) < datetime.today().year)
            if self.paginate and past_year:
                date_from = f'{str(self.year)}-01-01'
                date_to = f'{str(self.year)}-12-31'
            else:
                date_to = today
                if self.paginate:
                    date_from = f'{str(self.year)}-01-01'
                else:
                    date_from = one_month_before
        except TypeError:
            print(f'Invalid input for year. Using date range {one_month_before}-{today}.\n')
            return one_month_before, today

        return date_from, date_to

    def download_articles(self):
        articles_list = self.get_articles_list()
        if isinstance(articles_list, list):
            articles_df = pd.DataFrame(articles_list)
            articles_df['source_name'] = articles_df['source'].apply(lambda x: x['name'])
            return articles_df
        else:
            print('Could not download news. Exiting...\n')
            sys.exit(-1)

    def get_articles_list(self):
        first_result_data = self.send_request()

        if first_result_data == -1:
            return -1
        else:
            if self.paginate:
                return self.get_complete_results(first_result_data)
            else:
                return first_result_data['articles']

    def send_request(self):
        try:
            response = requests.get(url=URL, params=self.params)  # attempt a connection
        except requests.exceptions.RequestException:
            print("A RequestException occurred. Could not connect to the server. "
                  "Maybe check your connection or your request parameters?\n")
            return -1

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            error_response = response.json()
            print(f"Status code {error_response['code']} with message: '{error_response['message']}'\n")
            return -1

    def get_complete_results(self, first_result_data):
        total_results = first_result_data['totalResults']
        pagesize = self.params['pageSize']
        articles = first_result_data['articles']

        if total_results > pagesize:
            pages = (total_results // pagesize) + 1
        else:
            return articles

        for page in range(2, pages + 1):
            self.params['page'] = page
            print(f'Waiting {self.sleep_time}s before next page request.\n')
            time.sleep(self.sleep_time)
            next_page_data = self.send_request()
            if next_page_data == -1:
                return articles
            articles.append(next_page_data['articles'])
            return articles
