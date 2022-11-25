#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
