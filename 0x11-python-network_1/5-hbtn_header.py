#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


def fetch_data():
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    fetch_data()
