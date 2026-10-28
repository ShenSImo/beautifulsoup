from bs4 import BeautifulSoup, SoupReplacer

#tests for SoupReplacer
#Run wtih: pytest bs4/tests/test_soupreplacer.py -v

# Test 1: check that the replacement happens.
# Every <b> tag should become <blockquote>, and the text inside should stay the same.
def test_b_replaced_with_blockquote():
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup("<p><b>bold</b> and <b>again</b></p>", "html.parser", replacer=replacer)
    assert str(soup) == "<p><blockquote>bold</blockquote> and <blockquote>again</blockquote></p>"

# Test 2: check that the tree structure is still correct after the replacement.
# The parser still sends the end tag as "b", so handle_endtag must rename it too.
# Otherwise </b> cannot close the <blockquote>, and <span> ends up inside it.
def test_replaced_tag_closes_correctly():
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup("<div><b>x</b><span>y</span></div>", "html.parser", replacer=replacer)
    assert str(soup) == "<div><blockquote>x</blockquote><span>y</span></div>"