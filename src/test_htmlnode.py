import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_true(self):
        node = HTMLNode("a", "click here", None, {"href": "www.clicker.com"})
        self.assertEqual(node.props_to_html(), ' href="www.clicker.com"')

    def test_propsmissing(self):
        node = HTMLNode("a", "click here", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_multipleprops(self):
        node = HTMLNode("a", "click here", None, {"href": "www.clicker.com", "target": "_landingpage"})
        props_html = node.props_to_html()
        self.assertIn(' href="www.clicker.com"', props_html)
        self.assertIn(' target="_landingpage"', props_html)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is fat.")
        self.assertEqual(node.to_html(), "<b>This is fat.</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", {"href": "www.whatalink.com"})
        self.assertEqual(node.to_html(), '<a href="www.whatalink.com">Click me</a>')

    def test_noTag(self):
        node = LeafNode(None, "Some Text", {"href": "www.linky.com"})
        self.assertEqual(node.to_html(), "Some Text")

    def test_noValue(self):
        node = LeafNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
