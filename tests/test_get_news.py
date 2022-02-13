import pytest
from datetime import datetime, timedelta
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


def test_download_articles():
    downloader = NewsDownloader('brexit', paginate=False)
    articles = downloader.download_articles()
    assert len(articles) > 0


def test_create_from_to_dates(downloader):
    today = datetime.today().strftime('%Y-%m-%d')
    one_month_before = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    date_from, date_to = downloader.create_from_to_dates()
    assert (date_from, date_to) == (one_month_before, today)


def test_create_from_to_dates_custom_year():
    downloader = NewsDownloader('brexit', year='2020', paginate=True)
    date_from, date_to = downloader.create_from_to_dates()
    assert (date_from, date_to) == ('2020-01-01', '2020-12-31')


def test_failed_create_from_to_dates_custom_year():
    today = datetime.today().strftime('%Y-%m-%d')
    one_month_before = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    downloader = NewsDownloader('brexit', year='2020', paginate=False)
    date_from, date_to = downloader.create_from_to_dates()
    assert (date_from, date_to) == (one_month_before, today)


def test_send_request(downloader):
    response = downloader.send_request()
    assert len(response) > 0


def test_get_complete_results(downloader):
    first_results = downloader.send_request()
    results = downloader.get_complete_results(first_results)
    assert len(results) > 0
