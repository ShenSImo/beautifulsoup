# SoupReplacer: change tags while the document is being parsed
class SoupReplacer(object):
    #more flexible to change tag names and attributes with a function than to just replace them with a string
    #keep the original og_tag and alt_tag for convenience, but you can also just pass in a function to change the tag name or attributes
    def __init__(self, og_tag=None, alt_tag=None,
                 name_xformer=None, attrs_xformer=None, xformer=None):
        if og_tag is not None:
            #a lambda function to change the tag name if it matches the original tag, otherwise return the original tag name
            name_xformer = lambda tag: alt_tag if tag.name == og_tag else tag.name
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def transform(self, tag):
        #use returned values from xformers to change tag name and attributes, or just call xformer to modify tag in place
        if self.name_xformer is not None:
            tag.name = self.name_xformer(tag)
        if self.attrs_xformer is not None:
            tag.attrs = self.attrs_xformer(tag)
        if self.xformer is not None:
            self.xformer(tag)