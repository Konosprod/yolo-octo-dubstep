#/usr/bin/python3.3

from bs4 import BeautifulSoup
import urllib.request
import sys


def downloadTumblr(url):
    print("here")

def printUsage():
    print("Usage : " + sys.argv[0] + " [tumblr url]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printUsage()
    else
        downloadTumblr(sys.argv[1])
