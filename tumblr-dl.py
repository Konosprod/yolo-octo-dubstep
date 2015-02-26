#!/usr/bin/python3.3

from bs4 import BeautifulSoup
import urllib.request
import sys
import photoset

rem_file = ""

def dlProgress(count, blockSize, totalSize):
    global rem_file
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r"+ "Downloading " + rem_file + " ...%d%%" % percent)
    sys.stdout.flush()
    
def getFilename(url):
    return url[url.rfind('/')+1:]

def downloadTumblr(url):
    basename = url[:-1]
    html = photoset.getSource(url)
    
    print("Downloading " + url + "page/1")
    downloadPage(html)
    page = html.find('a', attrs = {'id' : 'next'})
    
    while(page):
        print("Downloading " + basename + page['href'])
        html = photoset.getSource(basename + page['href'])
        downloadPage(html)
        page = html.find('a', attrs = {'id' : 'next'})

def downloadPage(html):
    global rem_file
    photosets = html.findAll('iframe', attrs={'class' : 'photoset'})
    for s in photosets:
        imgUrl = photoset.getPhotosetImagesUrl(s['src'])
        for u in imgUrl:
            rem_file = getFilename(u)
            urllib.request.urlretrieve(u, rem_file, reporthook=dlProgress)
            print("")
            
    images = html.findAll('img', attrs = {'id' : 'photo'})
    for i in images:
        rem_file = getFilename(i['src'])
        urllib.request.urlretrieve(u, rem_file, reporthook=dlProgress)
        print("")

def printUsage():
    print("Usage : " + sys.argv[0] + " [tumblr url]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printUsage()
    else:
        downloadTumblr(sys.argv[1])
