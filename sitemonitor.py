#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import requests

__version__ = '0.1'

def geturls():
    return ['http://www.google.com/']


def checkurls(args):
    print args.email, args.file
    errors = []
    urls = geturls()
    for url in urls:
        r = requests.head(url)
        if 200 != r.status_code:
            errors.append((r.status_code, url))


def main():
    parser = argparse.ArgumentParser(description='Monitor availability of websites.', version=__version__)
    parser.add_argument('--file', required=True, help='File with newline separated urls.')
    parser.add_argument('--email', required=True, help='Email address to deliver error report.')
    parser.set_defaults(func=checkurls)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
