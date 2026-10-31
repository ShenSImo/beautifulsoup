# Tests for new SoupReplacer (M3)
# Run with: pytest bs4/tests/test_soupreplacer_m3.py -v
from bs4 import BeautifulSoup, SoupReplacer

# helper: parse the html with the replacer and return the result as a string
def parse(html, replacer):
    return str(BeautifulSoup(html, "html.parser", replacer=replacer))


# Test 1: name_xformer renames <b> to <blockquote> (the example from the assignment)
def test_name_xformer():
    r = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
    assert parse("<p><b>hi</b></p>", r) == "<p><blockquote>hi</blockquote></p>"


# Test 2: after renaming, the tree structure is still correct
# (<span> must come after </blockquote>, not inside it)
def test_name_xformer_keeps_structure():
    r = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
    assert parse("<div><b>x</b><span>y</span></div>", r) == "<div><blockquote>x</blockquote><span>y</span></div>"


# Test 3: attrs_xformer replaces the attributes of <p>, other tags keep theirs
def test_attrs_xformer():
    r = SoupReplacer(attrs_xformer=lambda tag: {"id": "new"} if tag.name == "p" else tag.attrs)
    assert parse('<p class="a">x</p><div class="b">y</div>', r) == '<p id="new">x</p><div class="b">y</div>'


# Test 4: xformer removes the class attribute (the example from the assignment)
def test_xformer_removes_class():
    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    r = SoupReplacer(xformer=remove_class_attr)
    assert parse('<p class="a">x</p><div class="b" id="d">y</div>', r) == '<p>x</p><div id="d">y</div>'


# Test 5: xformer adds class="test" to every <p> (same as task7)
# it adds the class if missing, and replaces it if there is one
def test_xformer_adds_class_to_p():
    def p_class_test(tag):
        if tag.name == "p":
            tag["class"] = "test"
    r = SoupReplacer(xformer=p_class_test)
    assert parse('<p>a</p><p class="old">b</p><div>c</div>', r) == '<p class="test">a</p><p class="test">b</p><div>c</div>'


# Test 6: all three used together, run in order: name, then attrs, then xformer
def test_all_three_together():
    def mark(tag):
        tag["data-seen"] = "yes"
    r = SoupReplacer(
        name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name,
        attrs_xformer=lambda tag: {},
        xformer=mark,
    )
    assert parse('<b class="x">hi</b>', r) == '<strong data-seen="yes">hi</strong>'