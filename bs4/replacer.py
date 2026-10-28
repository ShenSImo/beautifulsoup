#SoupReplacer: rename tags while the document is being parsed and the tree is being built
class SoupReplacer(object):
    og_tag: str
    alt_tag: str

    def __init__(self, og_tag: str, alt_tag: str):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def replace(self, name: str) -> str:
        #return the tag as the new tag if tag matches with og_tag
        if name == self.og_tag:
            return self.alt_tag
        return name

    def __repr__(self) -> str:
        return "<%s %r -> %r>" % (self.__class__.__name__, self.og_tag, self.alt_tag)