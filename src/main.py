import utils

url = "https://www.dba.dk/computer-og-spillekonsoller/hardware-og-software/grafikkort/side-1"

pages = utils.GetNumberPages(url)
print("Pages:", pages)

listings = utils.GetAllListings(url, pages)

print("Total listings:", len(listings))

# print("-"*45)
# for listing in listings:
#     print(listing[0])
#     print("\t" + listing[1])
#     print("-"*45)

# with open('test.html', "wb") as f:
#     f.write(response.content)

