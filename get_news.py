import requests

URL = 'https://newsapi.org/v2/everything'
KEY = '949120e5934548c1a41a240b23635ac8'


class RequestNews:

    def __init__(self, topic):
        self.params = {'q': topic,
                       'apiKey': KEY,
                       'page': 1,
                       'from': '2021-12-12',
                       'language': 'en'
                       }

    def query_newsapi(self):
        try:
            responce = requests.get(url=URL, params=self.params)  # attempt a connection
        except requests.exceptions.RequestException:
            return -1

        # handle http error codes 500 or 40x
        if str(responce.status_code).startswith('5' or '4'):
            error_responce = responce.json()
            return f"Status code {error_responce['']} with message: '{error_responce['message']}'"

        data = responce.json()  # get response's data in json format
        return data