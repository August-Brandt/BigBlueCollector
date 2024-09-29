import utils
import sys


def scrapeUrl(url: str, keywords: list[str]=None):
    # TODO: add threading to speed up fetching data
    # Append page number to url
    if url[-6:] != "side-1":
        url += "/side-1"
    
    numberOfPages = utils.GetNumberPages(url)
    listings = utils.GetAllListings(url, numberOfPages)
    return {
        'numberOfPages': numberOfPages,
        'listings': listings
    }

def main():
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

if __name__ == "__main__":
    main()