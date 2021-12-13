import pytest
import pandas as pd

from main import parse_arguments, download_articles


@pytest.fixture()
def argsparser():
    return parse_arguments(['topic', 'brexit'])


def test_parse_arguments(argsparser):
    # parser = parse_arguments(['topic', 'brexit'])
    assert argsparser.topic == 'topic'
    assert argsparser.query == 'brexit'


def test_download_articles(argsparser):
    articles = download_articles(argsparser)
    if isinstance(articles, pd.DataFrame):
        assert len(articles.columns) > 0
