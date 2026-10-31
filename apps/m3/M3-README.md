# Milestone-3

## What I changed

1. `bs4/replacer.py`: SoupReplacer now also takes `name_xformer`, `attrs_xformer` and `xformer`.
2. `bs4/__init__.py`: the replacer runs when each tag is closed (in `popTag`).
3. `bs4/tests/test_soupreplacer_m3.py`: 6 new tests. Run with `pytest bs4/tests/test_soupreplacer_m3.py -v`
4. `apps/m3/task7.py`: task 7 from Milestone 1, using an `xformer`. Run with `python apps/m3/task7.py <file.html>`. Same output as Milestone 1 (checked with `diff`).

All tests: 1 failed, 627 passed, 216 skipped. The 1 failure was already there before my changes.

## Technical brief: M2 vs M3

### M2: use two names

```python
SoupReplacer("b", "blockquote")
```

Super simple and hard to get wrong. But it can only rename one tag to another. Nothing else.

### M3: use functions

```python
SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
SoupReplacer(xformer=remove_class_attr)
```

1. `name_xformer` returns a new name.
2.  `attrs_xformer` returns new attributes.
3.  `xformer` changes the tag directly and returns nothing.

Much more flexible: you can change names, attributes, or anything, with different orders. But you have to write a function, and it's easier to make mistakes. For example, if you forget `else tag.name`, every tag gets renamed.

### How I built it

M2 renamed tags before they were created, in two places (start tag and end tag). M3 functions need a real tag, so that didn't work anymore. If I renamed a tag right after creating it, `</b>` couldn't find it and the tree would break.

So now the change happens when a tag is closed. By then the tag is complete and already closed with its original name. Only one place in the code needed to change.

The old M2 style is turned into a `name_xformer` behind the scenes. So both styles share the same code, and the M2 tests still pass.

### Downsides

1. A SoupStrainer still sees the original tag names, because the change happens later.
2. The function runs on every tag, so a slow function slows down parsing.
3. `xformer` has few limitaiton, so a bad one might distort the entire tree.

### Recommendation

Keep both in one class. Use the M2 style for simple renames. Use the M3 functions when you need more. Pick `name_xformer` or `attrs_xformer` when they're enough, since they only touch one thing, and save `xformer` for when you need several changes at once. Since M2 is built on top of M3, there's only one piece of code to maintain, and old code keeps working.