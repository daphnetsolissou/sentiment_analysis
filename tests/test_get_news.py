import pytest

from get_news import NewsDownloader


@pytest.fixture()
def downloader():
    return NewsDownloader('brexit')


def test_get_articles_list(downloader):
    data = downloader.get_articles_list()
    if isinstance(data, list):
        assert len(data) > 0
    else:
        assert data == -1
