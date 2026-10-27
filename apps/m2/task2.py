#Print out all the hyperlinks(<a> tags)
#use find_all to find indicated tags
import sys
from bs4 import BeautifulSoup, SoupStrainer
filename = sys.argv[1]

if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"
strained = SoupStrainer("a")
with open(filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, parser, parse_only=strained)

for link in soup.find_all("a"):
    print(link)