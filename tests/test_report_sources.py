import pytest

from get_news import NewsDownloader
from report_sources import SourcesReporter


@pytest.fixture()
def downloader():
    return NewsDownloader('brexit')


def test_count_per_sources(downloader):
    articles_df = downloader.download_articles()
    reporter = SourcesReporter(articles_df)
    counts = reporter.count_per_sources()
    assert len(counts) == len(set(articles_df['source_name'].tolist()))


def test_report(downloader):
    articles_df = downloader.download_articles()
    reporter = SourcesReporter(articles_df)
    my_dict = reporter.report_dict
    assert len(my_dict) == 3


def test_get_report_json(downloader):
    articles_df = downloader.download_articles()
    reporter = SourcesReporter(articles_df)
    my_json = reporter.get_report_json()
    assert len(my_json) > 0
