import requests
from bs4 import BeautifulSoup
import re

url = "https://www.dba.dk/computer-og-spillekonsoller/hardware-og-software/grafikkort/side-1"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the number of pages
pagination = soup.find('div', {"class": "pagination"})
pages = int(pagination.find_all('li')[-2].find('a').string) # Get the number of the last pagination link
print(pages)
listings = []
for i in range(2, pages + 1):
    page_listings = 0
    for listing in soup.find_all('tr', {"class": re.compile("^dbaListing")}):
        page_listings += 1
        link = listing.find('a', {"class": "listingLink"})
        text = link.find('span', {"class": "text"}).string
        price = link.find('span', {"class": "price"}).string
        listings.append((text, price))
        # print(listing['class'])
    print("Page", i-1, page_listings)
    response = requests.get(url[:-1] + str(i))
    soup = BeautifulSoup(response.content, 'html.parser')

print(len(listings))

# print("-"*45)
# for listing in listings:
#     print(listing[0])
#     print("\t" + listing[1])
#     print("-"*45)

# with open('test.html', "wb") as f:
#     f.write(response.content)

