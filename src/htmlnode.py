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
