#!/usr/bin/python3
""" Sending a request to URL """


if __name__ = "__main__":
	import urllib.request
	import sysy

	with urllib.request.urlopen(sys.argv[1] as response:
		head = response.headers.get('X-Request-Id')
		print(head)
