import requests

URL = 'https://newsapi.org/v2/everything'
KEY = '949120e5934548c1a41a240b23635ac8'


class NewsDownloader:

    def __init__(self, query):
        self.params = {'q': query,
                       'apiKey': KEY,
                       'page': 1,
                       'pageSize': '100',
                       'from': '2021-12-12',
                       'language': 'en'
                       }

    def query_newsapi(self):
        try:
            response = requests.get(url=URL, params=self.params)  # attempt a connection
        except requests.exceptions.RequestException:
            return -1

        if response.status_code == 200:
            data = response.json()
            if data['totalResults'] > 100:
                pass
            else:
                return data
        else:
            error_response = response.json()
            print(f"Status code {error_response['code']} with message: '{error_response['message']}'")
            return -1

    # def paginate(self):