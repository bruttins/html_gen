import unittest
from code import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is a `code block` textblock.", TextType.TEXT)
        result_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_node = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" textblock.", TextType.TEXT)
        ]
        self.assertEqual(result_node, expected_node)

    def test_bold(self):
        node = TextNode("This is a **bold** word.", TextType.TEXT)
        result_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_node = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT)
        ]
        self.assertEqual(result_node, expected_node)

    def test_italicException(self):
        node = TextNode("This is an _italic word.", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_twoitalics(self):
        node1 = TextNode("This is an _italic_ word.", TextType.TEXT)
        node2 = TextNode("This is also an _italic_ word.", TextType.TEXT)
        nodes = [node1, node2]

        result_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        expected_node = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT),
            TextNode("This is also an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT)
        ]
        self.assertEqual(result_nodes, expected_node)

    def test_boldstart(self):
        node = TextNode("**This is a bold** start.", TextType.TEXT)
        result_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_node = [
            TextNode("This is a bold", TextType.BOLD),
            TextNode(" start.", TextType.TEXT)
        ]
        self.assertEqual(result_node, expected_node)

    def test_boldending(self):
        node = TextNode("This is a **bold ending**.", TextType.TEXT)
        result_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_node = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold ending", TextType.BOLD),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(result_node, expected_node)
