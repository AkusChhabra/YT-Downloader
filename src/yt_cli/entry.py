import argparse
from .yt_dl import download

def cli_entry_point():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    parser_request = subparsers.add_parser('url', help='set the url link for the youtube video to download')

    args = parser.parse_args()

    if args.command == 'url':
        download()
    else:
        parser.print_help()