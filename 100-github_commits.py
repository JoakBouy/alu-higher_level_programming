#!/usr/bin/python3
"""
script takes 2 args and gets 10 commits
"""
import sys
import requests


if __name__ == "__main__":
    # Get the arguments, arg1: repo name, arg2: repo owner
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
