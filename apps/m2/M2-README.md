# Milestone-2

## API, file, and line number
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