# Milestone 2 Part-3: task6 using SoupReplacer
import sys
from bs4 import BeautifulSoup, SoupReplacer      
#import SoupReplacer

filename = sys.argv[1]

if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"

# a rule: rename every <b> to <blockquote> while the tree is being built
b_to_blockquote = SoupReplacer("b", "blockquote")

with open(filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, parser, replacer=b_to_blockquote)   # ③ 交给 BeautifulSoup


output = "task6_output.html"
with open(output, "w", encoding="utf-8") as file:
    file.write(soup.prettify())