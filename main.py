import argparse
import sys
from get_news import NewsDownloader
import pandas as pd


def parse_arguments(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("topic", type=str, help='Argument topic is required')
    parser.add_argument("query", type=str, help='Type a topic to search for in the newsapi')
    parsed_args = parser.parse_args(args)
    return parsed_args


def report_sources(input_args):
    pass


def download_articles(input_args):
    downloader = NewsDownloader(input_args.query)
    articles_list = downloader.get_articles_list()
    if isinstance(articles_list, list):
        articles_df = pd.DataFrame(articles_list)
        articles_df['source'] = articles_df['source'].apply(lambda x: x['name'])
        return articles_df
    else:
        raise sys.exit(-1)


def main():
    input_args = parse_arguments(sys.argv[1:])
    if len(sys.argv) == 2:
        report_sources(input_args)


if __name__ == "__main__":
    main()