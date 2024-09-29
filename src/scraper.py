import utils
import sys

args = sys.argv
if len(args) < 2:
    print("Usage: python3 main.py [path-to-definition-file]")
    quit()

# Retrieve url from definition file
keywords = []
with open(args[1], "r") as f:
    url = f.readline().rstrip()
    while line := f.readline().rstrip():
        match line[0:4]:
            case "key:":
                keywords.append(line[4:].lower())
            case _:
                print(f"Invalid syntax: {line[0:4]}\n\tLine: {line}")
                quit()

print("Getting listing from: " + url + " ...")
# Append page number to url
if url[-6:] != "side-1":
    url += "/side-1"
utils.GetHtmlFile(url)
pages = utils.GetNumberPages(url)
print("Pages:", pages)

listings = utils.GetAllListings(url, pages)

print("Total listings:", len(listings))

""" print("-"*45)
for listing in listings:
    print(f"Listing: {listing[0]}\n\tPrice: {listing[1]} kr")
    print("-"*45) """


print("-"*45)
for listing in listings:
    for keyword in keywords:
        if keyword in listing[0].lower():
            print(listing[0])
            print("\t" + listing[1])
            print("-"*45)
            break

