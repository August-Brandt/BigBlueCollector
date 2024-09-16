import requests
from bs4 import BeautifulSoup
import re

url = "https://www.dba.dk/computer-og-spillekonsoller/hardware-og-software/grafikkort/side-1"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find the number of pages
pagination = soup.find('div', {"class": "pagination"})
pages = int(pagination.find_all('li')[-2].find('a').string) # Get the number of the last pagination link

# print(soup.prettify())
print("-"*45)
for listing in soup.find_all('tr', {"class": re.compile("^dbaListing")}):
    link = listing.find('a', {"class": "listingLink"})
    text = link.find('span', {"class": "text"}).string
    price = link.find('span', {"class": "price"}).string
    print(text)
    print("\t " + price)
    print("-"*45)
    # print(listing['class'])

# with open('test.html', "wb") as f:
#     f.write(response.content)

