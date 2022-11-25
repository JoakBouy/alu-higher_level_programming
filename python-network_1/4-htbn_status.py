#!/usr/bin/python3
"""Check status"""
import requests


if __name__ == "__main__":
    reply = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(reply)))
    print("\t- content: {}".format(reply))
