#!/usr/bin/python3
<<<<<<< HEAD
"""
Script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
   request = urlib.request.Request("https://intranet.htbn.io/status")
   with urlib.request.urlopen(request) as response:
	body = response.read()
	print("Body response")
	print("\t- type: {}".format(type(body)))
	print("\t- content: {}".format(body))
	print("\t- utf8 content: {}".format(body.decode("utf-8")))
=======
"""a Python script that fetches an url"""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
>>>>>>> 3089ad19de348278c71f7f07a8420b8944e0b912
