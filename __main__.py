import argparse
import sys

from bookbot import report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="the file containing the book to report on")
    args = parser.parse_args()
    sys.exit(report(args.file))
