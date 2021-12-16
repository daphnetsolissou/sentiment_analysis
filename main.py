import argparse
import sys
from get_news import NewsDownloader
from report_sources import SourcesReporter
from report_sentiment import SentimentReporter
import pandas as pd


def parse_arguments(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("topic", type=str, help='Argument topic is required')
    parser.add_argument("query", type=str, help='Type a topic to search for in the newsapi')
    parser.add_argument("--sentiment", help='Perform sentiment analysis', action="store_true")
    parser.add_argument("--methodA", help='Perform sentiment analysis using Deep Neural Network', action="store_true")
    parser.add_argument("--methodB", help='Perform sentiment analysis using Multinomial Naive Bayes',
                        action="store_true")
    parsed_args = parser.parse_args(args)
    return parsed_args


def main():
    input_args = parse_arguments(sys.argv[1:])
    downloader = NewsDownloader(input_args.query)
    articles = downloader.download_articles()
    # articles.to_csv('Articles.csv', index=False, encoding='utf8')
    if input_args.sentiment:
        if input_args.methodB:
            reporter = SentimentReporter(articles)
        else:
            reporter = SentimentReporter(articles, 'dnn')
        results = reporter.get_report_string()
        print(results)

    if len(sys.argv[1:]) == 2:
        reporter = SourcesReporter(articles)
        json = reporter.get_report_json()
        print(json)


if __name__ == "__main__":
    main()