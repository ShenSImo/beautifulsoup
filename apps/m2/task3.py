#Print out all the tags in the document

import sys
from bs4 import BeautifulSoup, SoupStrainer
filename = sys.argv[1]

if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"
tags = SoupStrainer(True)
with open(filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, parser, parse_only=tags)

for tag in soup.find_all(True):#speficy what tags we are looking for 
    print(tag)