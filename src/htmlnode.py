class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        stringlist = []
        for prop in self.props:
            propvalue = self.props[prop]
            stringlist.append(f' {prop}="{propvalue}"')
        html_string = "".join(stringlist)
        return html_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value missing")
        elif self.tag is None:
            return f"{self.value}"
        else:
            adress = self.props_to_html()
            return f"<{self.tag}{adress}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag missing")
        elif self.children is None:
            raise ValueError("Children missing, call 911")
        else:
            childrenlist = []
            for child in self.children:
                childrenlist.append(child.to_html())
            result = "".join(childrenlist)
            return f"<{self.tag}>{result}</{self.tag}>"
