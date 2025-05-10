import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()

