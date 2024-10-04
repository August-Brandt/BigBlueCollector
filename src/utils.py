import requests
from bs4 import BeautifulSoup
import re
import time

def GetNumberPages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pagination = soup.find('div', {"class": "pagination"})
    pages = int(pagination.find_all('li')[-2].find('a').string) # Get the number of the last pagination link
    return pages

def GetAllListings(startUrl, numberOfPages):
    listings = []
    starttime = time.time()
    for i in range(1, numberOfPages + 1):
        response = requests.get(startUrl[:-1] + str(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"\rFetching page {i} ...", end='')
        listings.extend(GetListings(soup))
    print()
    endtime = time.time()
    print("total fetch time:", endtime - starttime)
    return listings

def GetListings(soup):
    listings = []
    for listing in soup.find_all('tr', {"class": re.compile("^dbaListing")}):
        link = listing.find('a', {"class": "listingLink"})
        text = link.find('span', {"class": "text"}).string
        price = link.find('span', {"class": "price"}).string
        listings.append((text, price))
    return listings

def GetHtmlFile(url):
    response = requests.get(url)
        
    with open('test.html', "wb") as f:
        f.write(response.content)