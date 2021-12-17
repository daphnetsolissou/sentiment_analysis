import pytest
import os
from main import parse_arguments, download_news, report_sources, parse_year_option, report_sentiment

ROOT_DIR = os.path.dirname(os.getcwd())


@pytest.fixture()
def argsparser():
    return parse_arguments(['topic', 'christmas', '--year=2021'])


def test_parse_arguments(argsparser):
    assert argsparser.topic == 'topic'
    assert argsparser.query == 'christmas'


def test_report_sources(argsparser):
    articles = download_news(argsparser.topic, '2021')
    my_report = report_sources(articles, argsparser)
    assert len(my_report) > 1


def test_report_sources_year(argsparser):
    args_list = parse_arguments(['topic', 'christmas', '--year=2021'])
    articles = download_news(args_list.query, args_list.year)
    my_report = report_sources(articles, argsparser)
    assert len(my_report) > 1


def test_parse_year_option(argsparser):
    year = parse_year_option(argsparser)
    assert year == '2021'


def test_report_sentiment():
    old_dir = os.getcwd()
    os.chdir(ROOT_DIR)
    args_list = parse_arguments(['topic', 'christmas', '--sentiment'])
    articles = download_news('christmas', '2021')
    emotions = report_sentiment(args_list.methodB, articles)
    os.chdir(old_dir)
    assert len(emotions) > 1


def test_report_sentiment_methodB():
    old_dir = os.getcwd()
    os.chdir(ROOT_DIR)
    args_list = parse_arguments(['topic', 'christmas', '--sentiment', '--methodB'])
    articles = download_news('christmas', '2021')
    emotions = report_sentiment(args_list.methodB, articles)
    os.chdir(old_dir)
    assert len(emotions) > 1


def test_report_sentiment_methodA():
    old_dir = os.getcwd()
    os.chdir(ROOT_DIR)
    args_list = parse_arguments(['topic', 'christmas', '--sentiment', '--methodA'])
    articles = download_news('christmas', '2021')
    emotions = report_sentiment(args_list.methodB, articles)
    os.chdir(old_dir)
    assert len(emotions) > 1


def test_report_sentiment_methodA_year():
    old_dir = os.getcwd()
    os.chdir(ROOT_DIR)
    args_list = parse_arguments(['topic', 'christmas', '--sentiment', '--methodA', '--year=2021'])
    articles = download_news('christmas', '2021')
    emotions = report_sentiment(args_list.methodB, articles)
    os.chdir(old_dir)
    assert len(emotions) > 1


def test_report_sentiment_year():
    old_dir = os.getcwd()
    os.chdir(ROOT_DIR)
    args_list = parse_arguments(['topic', 'christmas', '--sentiment', '--year=2021'])
    articles = download_news('christmas', '2021')
    emotions = report_sentiment(args_list.methodB, articles)
    os.chdir(old_dir)
    assert len(emotions) > 1
