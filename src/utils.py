import requests
from bs4 import BeautifulSoup
import re
import threading
import time


def GetNumberPages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pagination = soup.find('div', {"class": "pagination"})
    pages = int(pagination.find_all('li')[-2].find('a').string) # Get the number of the last pagination link
    return pages

def GetAllListings(startUrl, numberOfPages):
    listings = []
    lock = threading.Lock()
    threads = []
    starttime = time.time()
    for i in range(1, numberOfPages + 1):
        thread = threading.Thread(target=GetListings, args=(startUrl, i, listings, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    endtime = time.time()
    print("Total fetch time:", endtime - starttime)
    return listings

def GetListings(baseurl, pagenum, listings, lock):
    print("Fetching page", pagenum)
    response = requests.get(baseurl[:-1] + str(pagenum))
    soup = BeautifulSoup(response.content, 'html.parser')
    listingsBuffer = []
    for listing in soup.find_all('tr', {"class": re.compile("^dbaListing")}):
        link = listing.find('a', {"class": "listingLink"})
        text = link.find('span', {"class": "text"}).string
        price = link.find('span', {"class": "price"}).string
        listingsBuffer.append((text, price))

    lock.acquire()
    listings.extend(listingsBuffer)
    lock.release()
    print("Finished fetching page", pagenum)

def GetHtmlFile(url):
    response = requests.get(url)
        
    with open('test.html', "wb") as f:
        f.write(response.content)