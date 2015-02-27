#!/usr/bin/python3.3

from bs4 import BeautifulSoup
import urllib.request
import sys
import photoset
import os

rem_file = ""
directory = ""

#Download with a progress bar
def dlProgress(count, blockSize, totalSize):
    global rem_file
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r"+ "Downloading " + rem_file + " ...%d%%" % percent)
    sys.stdout.flush()
    
def getBlogName(url):
    name = url[:-1]
    return name[name.rfind('/')+1:name.find('.')]

#Get filename
def getFilename(url):
    return url[url.rfind('/')+1:]

#Download the blog
def downloadTumblr(url):
    global directory
    basename = url[:-1]
    html = photoset.getSource(url)
    
    directory = getBlogName(url)
    
    os.mkdir(directory)
    
    print("Downloading " + url + "page/1")
    downloadPage(html)
    page = html.find('a', attrs = {'id' : 'next'})
    
    #While there is still page
    while(page):
        print("Downloading " + basename + page['href'])
        html = photoset.getSource(basename + page['href'])
        downloadPage(html)
        page = html.find('a', attrs = {'id' : 'next'})

def downloadPage(html):
    global rem_file
    global directory
    #Find all photoset iframes
    photosets = html.findAll('iframe', attrs={'class' : 'photoset'})
    for s in photosets:
        #get photosets image urls
        imgUrl = photoset.getPhotosetImagesUrl(s['src'])
        for u in imgUrl:
            rem_file = directory + "/" + getFilename(u)
            #download the file
            urllib.request.urlretrieve(u, rem_file, reporthook=dlProgress)
            print("")
    #For all normal images
    images = html.findAll('img', attrs = {'id' : 'photo'})
    for i in images:
        rem_file = directory + "/" + getFilename(i['src'])
        #Download them
        urllib.request.urlretrieve(u, rem_file, reporthook=dlProgress)
        print("")

def printUsage():
    print("Usage : " + sys.argv[0] + " [tumblr url]")


if __name__ == "__main__":
	
    url = ""
	
    if len(sys.argv) < 2:
        url = input("Entrez l'url du blog : ")
        downloadTumblr(url)
    elif len(sys.argv) == 2:
        downloadTumblr(sys.argv[1])
    else:
        printUsage()
