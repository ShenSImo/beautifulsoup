#Print out all the tags that have an id attribute. 
#this should be done with a single API call
import sys
from bs4 import BeautifulSoup, SoupStrainer

filename = sys.argv[1]

if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"
has_id = SoupStrainer(id=True)
with open(filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, parser, parse_only=has_id)

for tag in soup.find_all(id=True):
    print(tag)
