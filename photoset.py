#!/usr/bin/python3.3

from bs4 import BeautifulSoup
import urllib.request
import sys

#Download source code of a page
def getSource(url):
    reponse = urllib.request.urlopen(url)
    pageSource = reponse.read()
   
    return BeautifulSoup(pageSource.decode("utf8"))

#Get all photoset image url
def getPhotosetImagesUrl(url):
    ret = []
    html = getSource(url)
    
    entries = html.findAll('a', attrs = {'data-photoset-index' : True})
    for s in entries :
        ret.append(s['href'])
    
    return ret

if __name__ == "__main__":
    print(getPhotosetImagesUrl(sys.argv[1]))
