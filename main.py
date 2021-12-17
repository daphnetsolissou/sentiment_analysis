import argparse
import sys
from get_news import NewsDownloader
from report_sources import SourcesReporter
from report_sentiment import SentimentReporter
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


def parse_arguments(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("topic", type=str, help='Argument topic is required')
    parser.add_argument("query", type=str, help='Type a topic to search for in the newsapi')
    parser.add_argument("--sentiment", help='Perform sentiment analysis', action="store_true")
    parser.add_argument("--methodA", help='Perform sentiment analysis using Deep Neural Network', action="store_true")
    parser.add_argument("--methodB", help='Perform sentiment analysis using Multinomial Naive Bayes',
                        action="store_true")
    parser.add_argument("--year", type=str, help='Restrict results by year')
    parsed_args = parser.parse_args(args)
    return parsed_args


def parse_year_option(input_args):
    year = '2021'
    if input_args.year:
        year_arg = input_args.year
        if year_arg.find('=') > -1:
            year = year_arg.split('=')[1]

    return year


def download_news(query, year, save_results_csv=False):
    downloader = NewsDownloader(query, year=year)
    articles = downloader.download_articles()
    if save_results_csv:
        articles.to_csv(f'{query}_news.csv', index=False, encoding='utf8')
    return articles


def report_sentiment(is_methodb, articles, save_results_csv=False, query=''):
    if is_methodb:
        reporter = SentimentReporter(articles, model_name='bayes', save_classified_df=save_results_csv, topic=query)
    else:
        reporter = SentimentReporter(articles, model_name='dnn', save_classified_df=save_results_csv, topic=query)
    results = reporter.get_report_string()
    print(results)


def report_sources(articles, input_args):
    if input_args.topic:
        reporter = SourcesReporter(articles)
        json = reporter.get_report_json()
        print(json)


def main():
    input_args = parse_arguments(sys.argv[1:])
    year = parse_year_option(input_args)
    articles = download_news(input_args.query, year=year, save_results_csv=True)

    if input_args.sentiment:
        report_sentiment(is_methodb=input_args.methodB, articles=articles, save_results_csv=True,
                         query=input_args.query)
    else:
        report_sources(articles, input_args)


if __name__ == "__main__":
    main()