import pytest

from get_news import NewsDownloader


@pytest.fixture()
def downloader():
    return NewsDownloader('brexit')


def test_query_newsapi(downloader):
    data = downloader.query_newsapi()
    if isinstance(data, dict):
        assert len(data) == 3
    else:
        assert data == -1
