# Milestone-4

## What I did

1. `bs4/__init__.py`: added `__iter__` to `BeautifulSoup`. Now `for node in soup:` goes through every node.
2. `bs4/tests/test_soup_iter.py`: 5 tests. Run with `pytest bs4/tests/test_soup_iter.py -v`

All tests: 1 failed, 632 passed, 216 skipped. The 1 failure was there before my made the changes.

## Technical brief

### 1. What changed

1. Before: `for node in soup` only gave the top-level tags, which are the child nodes of the root node.
2. Now: it gives every node (tags, text, comments) in the order they appear.

### 2. How it works

    def __iter__(self):
        node = self.contents[0] if self.contents else None
        while node is not None:
            next_node = node.next_element
            yield node
            node = next_node

1. BeautifulSoup already links each node to the next one (`next_element`). So I just follow that chain from the first node to the end.
2. `yield` gives out one node and waits at the function. The next node is only found when the loop asks for it.
3. I grab the next node before `yield`, so it still works if the current node gets removed in the loop.

### 3. Why not a list

1. A list keeps every node in memory. This only keeps one, which is much more memory efficient when working with a large file.
2. You get the first node right away.

### 4. Things to know

1. I only changed `BeautifulSoup`. Looping over a normal tag still gives just its children.
2. The order is the same as bs4's own `soup.descendants`.
3. Downside: `for node in soup` means something different now, so old code that expected only the top level would break.
4. Downside: `len(soup)` still counts only the top level, so it doesn't match the loop.

### 5. My recommendation

1. Keep it a generator. That's what makes it work on big files.
2. Maybe instead of modifying the existed code, deifining a new method might be better, as we could keep the old code intact.