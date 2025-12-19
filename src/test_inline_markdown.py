import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_image(self):
        matches = extract_markdown_images(
            "Here is just one ![image with alt text](https://picy.png) you can use."
        )
        self.assertListEqual([("image with alt text", "https://picy.png")], matches)

    def test_image_noalttext(self):
        matches = extract_markdown_images(
            "Here is no alt text ![](https://picy.png) you can use."
        )   
        self.assertListEqual([("", "https://picy.png")], matches)

    def test_image_nolink(self):
        matches = extract_markdown_images(
            "Here is just one ![image with alt text]() you can use."
        )   
        self.assertListEqual([("image with alt text", "")], matches)

    def test_image_neither(self):
        matches = extract_markdown_images(
            "Here is just one Image ! you can use."
        )
        self.assertListEqual([], matches)

    def test_image_multiple(self):
        matches = extract_markdown_images(
            "Here is an ![image with alt text](https://picy.png) you can use, and here is ![another](https://picy2.png)."
        )   
        self.assertListEqual([("image with alt text", "https://picy.png"), ("another", "https://picy2.png"),], matches)

    def test_link(self):
        matches = extract_markdown_links(
            "Here is just one [link with alt text](https://picy.png) you can use."
        )
        self.assertListEqual([("link with alt text", "https://picy.png")], matches)

    def test_link_noalttext(self):
        matches = extract_markdown_links(
            "Here is no alt text [](https://picy.png) you can use."
        )
        self.assertListEqual([("", "https://picy.png")], matches)

    def test_link_nolink(self):
        matches = extract_markdown_links(
            "Here is just one [link with alt text]() you can use."
        )
        self.assertListEqual([("link with alt text", "")], matches)

    def test_link_neither(self):
        matches = extract_markdown_links(
            "Here is just one link you can use."
        )
        self.assertListEqual([], matches)

    def test_link_multiple(self):
        matches = extract_markdown_links(
            "Here is an [link with alt text](https://picy.png) you can use, and here is [another](https://picy2.png)."
        )
        self.assertListEqual([("link with alt text", "https://picy.png"), ("another", "https://picy2.png"),], matches)

    def test_links_ignore_images(self):
        matches = extract_markdown_links("Here is an image ![alt](https://picy.png).")
        self.assertListEqual([], matches)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://img.png) and another ![second image](https://img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://img.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_notext(self):
        node = TextNode(
            "![Just an image](https://img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Just an image", TextType.IMAGE, "https://img.png")
            ],
            new_nodes,
        )

    def test_split_images_nomarkdown(self):
        node = TextNode(
            "This is just text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is just text.", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
            ],
            new_nodes,
        )

    def test_split_image_markdownfirst(self):
        node = TextNode(
            "![This image](https://img.png) comes first.",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This image", TextType.IMAGE, "https://img.png"),
                TextNode(" comes first.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_markdownmiddle(self):
        node = TextNode(
            "This is text with an ![image](https://img.png) in the middle.",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" in the middle.", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_textintheend(self):
        node = TextNode(
            "This is text with an ![image](https://img.png) and another ![second image](https://img.png) and more text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://img.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://img.png"
                ),
                TextNode(" and more text.", TextType.TEXT),
            ],
            new_nodes,
        )
