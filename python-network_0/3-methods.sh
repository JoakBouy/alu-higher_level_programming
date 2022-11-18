#!/bin/bash
# script that takes url and displays HTTP methods server will accept
curl -sI "$1" | grep "Allow:" | sed 's/Allow: //'
