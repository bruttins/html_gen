import unittest
from markdownsplit import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_all(self):
        text = "Some **bold** and some _italic_ and some `code` and an ![image](https://img.png) and a [link](https://link.com)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and some ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and some ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
            ],
            nodes,
        )

    def test_text_to_textnodes_bold(self):
        text = "Some **bold** text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_text_to_textnodes(self):
        text = "Some _italic_ text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_text_to_textnodes_code(self):
        text = "Some `code` text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_text_to_textnodes_boldanditalic(self):
        text = "Some **bold** and _italic_ text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_text_to_textnodes_italicandbold(self):
        text = "Some _italic_ and **bold** text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_boldandimage(self):
        text = "Some **bold** and an ![image](https://img.png) text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )
    
    def test_text_to_textnodes_imageandlink(self):
        text = "An ![image](https://img.png) and a [link](https://link.com) text."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("An ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_text_to_textnodes_mixedup(self):
        text = "Some ![image](https://img.png) with **bold** and a [link](https://link.com) but also `code` and _italic_."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Some ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" but also ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )