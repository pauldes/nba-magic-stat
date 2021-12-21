import argparse

from nba_magic_stat import conf, logger
from nba_magic_stat import download, magic


def download_data(args=None):
    """Download data"""
    download.download_data()


def generate_stats(args=None):
    """Generate stats for a game"""
    magic.generate_stats()


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")
    subparser.add_parser("download", help="Download data")
    subparser.add_parser("magic", help="Generate stats for a game")
    return parser


def run(args=None):
    """CLI entry point.

    Args:
        args : List of args as input of the command line.
    """
    parser = get_parser()
    args = parser.parse_args(args)
    if args.command == "download":
        download_data(args)
    elif args.command == "magic":
        generate_stats(args)
