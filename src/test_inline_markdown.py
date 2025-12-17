import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

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

