import argparse
import sys
from get_news import NewsDownloader


def parse_arguments(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("topic", type=str, help='Argument topic is required')
    parser.add_argument("query", type=str, help='Type a topic to search for in the newsapi')
    parsed_args = parser.parse_args(args)
    return parsed_args


def main():
    input_args = parse_arguments(sys.argv[1:])
    downloader = NewsDownloader(input_args.query)


if __name__ == "__main__":
    main()