import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_textuneq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_propertyuneq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_urluneq(self):
        node = TextNode("This is a text node", TextType.CODE, "www.codetext.com")
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_to_html_text(self):
        node = TextNode("This is plain Text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is plain Text")

    def test_to_html_bold(self):
        node = TextNode("This is bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold Text")

    def test_to_html_italic(self):
        node = TextNode("This is italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic Text")

    def test_to_html_code(self):
        node = TextNode("This is Code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is Code")

    def test_to_html_link(self):
        node = TextNode("This is a Link", TextType.LINK, "www.zelda.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")    
        self.assertEqual(html_node.value, "This is a Link")
        self.assertEqual(html_node.props, {"href": "www.zelda.com"})

    def test_to_html_image(self):
        node = TextNode("Here is my Alt-Text", TextType.IMAGE, "www.imigy.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")  
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.imigy.com", "alt": "Here is my Alt-Text"})

if __name__ == "__main__":
    unittest.main()

