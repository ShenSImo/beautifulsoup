# Milestone-2

## Part 1: SoupStrainer

Files: `apps/m2/task2.py`, `apps/m2/task3.py`, `apps/m2/task4.py`

Run: `python apps/m2/task2.py <file.html>` (same for task3, task4)

| Task | SoupStrainer | Output same as M1? |
|---|---|---|
| task2 | `SoupStrainer("a")` | Yes (2163 lines) |
| task3 | `SoupStrainer(True)` | Yes (57291 lines) |
| task4 | `SoupStrainer(id=True)` | Yes (29888 lines) |

Correctness was checked on `Bash (Unix shell) - Wikipedia.html` (1.0 MB) by comparing `wc -l` of the M1 and M2 output.

### Performance on a large file

Test file: `bash-x50.html` (52 MB, the Bash Wikipedia page copied 50 times). Parser: `html.parser`. Measured with `/usr/bin/time -l`, output sent to `/dev/null`.

| Task | M1 time | M2 time | M1 memory | M2 memory |
|---|---|---|---|---|
| task2 | 8.60 s | 4.90 s | 886 MB | 523 MB |
| task3 | 51.07 s | 50.63 s | 930 MB | 897 MB |
| task4 | 30.85 s | 29.80 s | 917 MB | 883 MB |

### Observations

- **task2 benefits the most** (about 43% faster, 41% less memory). `<a>` tags are small and make up a small part of the page, so most tags are never created.
- **task4 barely benefits.** On Wikipedia, large wrappers like `<div id="content">` contain almost the whole article. Once a tag matches, everything inside it is kept. On the 1 MB page, 9717 of 9776 tags were still created. Most of the time is also spent printing, which SoupStrainer does not change.
- **task3 cannot benefit.** The task needs every tag, so `SoupStrainer(True)` filters out almost nothing.
- SoupStrainer only saves the cost of **creating objects**. The whole file is still read into memory, and the parser still scans every character.

### About the 1 GB file

`sample-1gb.html` from Milestone 1 is almost entirely one big HTML comment with only a few tags and no `<a>` tags, so it is not useful for comparing SoupStrainer. That is why I made `bash-x50.html` instead.

## Part 2: API, file, and line number

Line numbers refer to the original, unmodified source (commit `a49ea64`, bs4 4.13.0).

| My code | API | Source File | Line Number | Task |
|---|---|---|---|---|
| `BeautifulSoup` | `BeautifulSoup` | `bs4/__init__.py` | 133 | task 1-8 |
| `BeautifulSoup(f, parser)` | `BeautifulSoup.__init__` | `bs4/__init__.py` | 209 | task 1-8 |
| `SoupStrainer` | `SoupStrainer` | `bs4/filter.py` | 313 | M2 task 2-4 |
| `SoupStrainer(...)` | `SoupStrainer.__init__` | `bs4/filter.py` | 345 | M2 task 2-4 |
| `soup.get_text()` | `PageElement.get_text` | `bs4/element.py` | 524 | task 8 |
| `link.find_parent("p")` | `PageElement.find_parent` | `bs4/element.py` | 992 | task 5 |
| `tag["class"] = "test"` | `Tag.__setitem__` | `bs4/element.py` | 2223 | task 7, 8 |
| `print(tag)` | `Tag.__str__` -> `Tag.decode` | `bs4/element.py` | 2302 / 2334 | task 2-5 |
| `soup.prettify()` | `Tag.prettify` | `bs4/element.py` | 2601 | task 1, 6, 7 |
| `soup.find_all(...)` | `Tag.find_all` | `bs4/element.py` | 2715 | task 2-8 |
| `tag.name = "blockquote"` | `Tag.name` (`self.name = name`) | `bs4/element.py` | 1648 | task 6 |

## Part3: SoupReplacer

### how to use

```python
from bs4 import BeautifulSoup, SoupReplacer
r = SoupReplacer(“b”, “blockquote”)
soup = BeautifulSoup(html, “html.parser”, replacer=r)
```

It changes every `<b>` tag to `<blockquote>` while the file is being parsed.

I used `_` instead of `-` when naming the paramter `og-tag` and `alt-tag`.

### What I changed

- `bs4/replacer.py` (new file): the SoupReplacer class.
- `bs4/__init__.py`:
  - import SoupReplacer
  - added `replacer=None` to `BeautifulSoup.__init__`
  - in `handle_starttag`: change the tag name before the tag is created
  - in `handle_endtag`: change the end tag name too

### Why I did it this way

- I put the change in `handle_starttag` and `handle_endtag` because every parser calls these two methods, and SoupStrainer is also checked there.
- The end tag also needs to be renamed. Otherwise `</b>` can't close the `<blockquote>`, and the rest of the page ends up inside it.
- If no replacer is given, nothing changes. All old tests give the same result as before.

### Tests

Run: `pytest bs4/tests/test_soupreplacer.py -v`

- `test_b_replaced_with_blockquote`: checks that every `<b>` becomes `<blockquote>`.
- `test_replaced_tag_closes_correctly`: checks that `<span>` comes after `</blockquote>`, not inside it. This fails if `handle_endtag` is not changed.

All tests: 1 failed, 621 passed, 216 skipped. (619 old + 2 new. The 1 failure was already there before my change.)

### task6

Run: `python apps/m2/task6.py <file.html>`

The output is the same as Milestone 1 task6 (checked with `diff`).

Speed on `bash-x50.html` (52 MB):

| | Time | Memory |
|---|---|---|
| M1 task6 | 10.96 s | 1196 MB |
| M2 task6 | 10.84 s | 1197 MB |

Almost no difference. SoupReplacer skips one loop over the tree, but most of the time is spent on parsing and `prettify()`.