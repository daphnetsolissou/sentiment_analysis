import requests

URL = 'https://newsapi.org/v2/everything'
KEY = '949120e5934548c1a41a240b23635ac8'


class GetTheNews:

    def __init__(self, topic):
        self.topic = topic
        self.params = {'q': self.topic,
                       'apiKey': KEY,
                       'page': 1,
                       'from': '2021-12-12',
                       'language': 'en'
                       }

    # def query_newsapi(self):
