# Tests for iterating over a BeautifulSoup object (Milestone 4)
# Run with: pytest bs4/tests/test_soup_iter.py -v
from bs4 import BeautifulSoup


# Test 1: tags and text come out in document order
def test_iter_tags_and_text_in_order():
    soup = BeautifulSoup("<p>hi <b>there</b></p>", "html.parser")
    nodes = []
    for node in soup:
        nodes.append(str(node))
    assert nodes == ["<p>hi <b>there</b></p>", "hi ", "<b>there</b>", "there"]


# Test 2: every kind of node is visited: doctype, comment, tag, text
def test_iter_visits_every_node_type():
    soup = BeautifulSoup("<!DOCTYPE html><!--note--><p>x</p>", "html.parser")
    nodes = []
    for node in soup:
        nodes.append(str(node))
    assert nodes == ["html", "note", "<p>x</p>", "x"]


# Test 3: deeply nested tags are all reached, parent before child
# (text nodes have no name, so their name is None)
def test_iter_deeply_nested():
    soup = BeautifulSoup("<a><b><c><d>x</d></c></b></a>", "html.parser")
    names = []
    for node in soup:
        names.append(node.name)
    assert names == ["a", "b", "c", "d", None]


# Test 4: an empty document gives nothing (and does not crash)
def test_iter_empty_document():
    soup = BeautifulSoup("", "html.parser")
    count = 0
    for node in soup:
        count += 1
    assert count == 0


# Test 5: the loop can stop early; the nodes after it are never visited
def test_iter_can_stop_early():
    soup = BeautifulSoup("<p>1</p><p>2</p><p>3</p>", "html.parser")
    visited = []
    for node in soup:
        visited.append(str(node))
        if str(node) == "1":
            break
    assert visited == ["<p>1</p>", "1"]