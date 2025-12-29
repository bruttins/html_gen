import unittest
from md_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# This is a heading
## This is a subheading
### This is a sub-subheading
#### This is a sub-sub-subheading
##### This is a sub-sub-sub-subheading
###### This is a sub-sub-sub-sub-subheading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><h2>This is a subheading</h2><h3>This is a sub-subheading</h3><h4>This is a sub-sub-subheading</h4><h5>This is a sub-sub-sub-subheading</h5><h6>This is a sub-sub-sub-sub-subheading</h6></div>",
        )

    def test_lists(self):
        md = """
- Item 1
- Item 2 with **bold**
- Item 3 with _italic_
- Item 4

1. First item
2. Second item with `code`
3. Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2 with <b>bold</b></li><li>Item 3 with <i>italic</i></li><li>Item 4</li></ul><ol><li>First item</li><li>Second item with <code>code</code></li><li>Third item</li></ol></div>",
        )

    def test_links_and_images(self):
        md = """

Inside a normal Paragraph, we have a [link](http://example.com).

Here's the next paragraph, containing an ![image](http://example.com/image.png)
""" 
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Inside a normal Paragraph, we have a <a href=\"http://example.com\">link</a>.</p><p>Here's the next paragraph, containing an <img src=\"http://example.com/image.png\" /></p></div>",
        )

    def test_blockquotes(self):
        md = """
> This is a blockquote with **bold** text.
> Another line in the blockquote with _italic_ text.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a blockquote with <b>bold</b> text. Another line in the blockquote with <i>italic</i> text.</p></blockquote></div>",
        )

    def test_mixed_content(self):
        md = """
Here is a paragraph with a list:
```
- List item 1
- List item 2
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Here is a paragraph with a list:</p><pre><code>- List item 1\n- List item 2\n</code></pre></div>",
        )

    def test_other_mixed(self):
        md = """
Some introductory text.
```
def example():
    pass
```
1. First item
2. Second item with **bold**

More concluding text with a [link](http://example.com).
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Some introductory text.</p><pre><code>def example():\n    pass\n</code></pre><ol><li>First item</li><li>Second item with <b>bold</b></li></ol><p>More concluding text with a <a href=\"http://example.com\">link</a>.</p></div>",
        )