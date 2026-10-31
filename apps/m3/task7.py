# Milestone 3: task7 using SoupReplacer with a transformer
# Find all the <p> tags and add (or replace) class="test" during parsing, then write the tree onto a file.
# Change the tag at the moment it is closed
import sys
from bs4 import BeautifulSoup, SoupReplacer

filename = sys.argv[1]

if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"


# the body of the M1 for loop is now in a function, which will be called by the SoupReplacer for every tag
def p_class_test(tag):
    if tag.name == "p":
        tag["class"] = "test"


replacer = SoupReplacer(xformer=p_class_test)

with open(filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, parser, replacer=replacer)

# no for loop needed: every <p> already got class="test" during parsing

output = "task7_output.html"
with open(output, "w", encoding="utf-8") as file:
    file.write(soup.prettify())