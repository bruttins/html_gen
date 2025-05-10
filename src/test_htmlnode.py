import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_true(self):
        node = HTMLNode("a", "click here", None, {"href": "www.clicker.com"})
        assert node.props_to_html() == ' href="www.clicker.com"'

    def test_propsmissing(self):
        node = HTMLNode("a", "click here", None, None)
        assert node.props_to_html() == ""

    def test_multipleprops(self):
        node = HTMLNode("a", "click here", None, {"href": "www.clicker.com", "target": "_landingpage"})
        props_html = node.props_to_html()
        assert ' href="www.clicker.com"' in props_html
        assert ' target="_landingpage"' in props_html

if __name__ == "__main__":
    unittest.main()
