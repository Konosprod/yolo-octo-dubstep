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
    global rem_file
    html = photoset.getSource(url);
    photosets = html.findAll('iframe', attrs={'class' : 'photoset'})
    for s in photosets:
        imgUrl = photoset.getPhotosetImagesUrl(s['src'])
        for u in imgUrl:
            rem_file = getFilename(u)
            urllib.request.urlretrieve(u, rem_file, reporthook=dlProgress)
            print("")
            
        

def printUsage():
    print("Usage : " + sys.argv[0] + " [tumblr url]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printUsage()
    else:
        downloadTumblr(sys.argv[1])
