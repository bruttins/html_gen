import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_emptyline(self):
        md = """

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_listmiddle(self):
        md = """
This is **bolded** paragraph

- This is a list
- with items

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "- This is a list\n- with items",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_blocktype_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)
    def test_blocktype_unorderedlist(self):
        self.assertEqual(block_to_block_type("- This is a list item.\n- As is this."), BlockType.UNORDERED_LIST)
    def test_blocktype_orderedlist(self):    
        self.assertEqual(block_to_block_type("1. This is a numbered list item.\n2. This as well."), BlockType.ORDERED_LIST)
    def test_blocktype_code(self):    
        self.assertEqual(block_to_block_type("```python\nprint('Hello, World!')\n```"), BlockType.CODE)
    def test_blocktype_quote(self):    
        self.assertEqual(block_to_block_type("> This is a blockquote."), BlockType.QUOTE)
    def test_blocktype_heading1(self):    
        self.assertEqual(block_to_block_type("# This is a heading."), BlockType.HEADING)
    def test_blocktype_heading2(self):    
        self.assertEqual(block_to_block_type("###### This is a heading."), BlockType.HEADING)
    def test_blocktype_invalidheading(self):    
        self.assertEqual(block_to_block_type("####### This is not a heading."), BlockType.PARAGRAPH)
    def test_blocktype_missingwhitespace(self):    
        self.assertEqual(block_to_block_type("1.This is a wrong ordered-list-entry."), BlockType.PARAGRAPH)
    def test_blocktype_wrong_order(self):     
        self.assertEqual(block_to_block_type("2. Wrong Order.\n1. As you see."), BlockType.PARAGRAPH)
    def test_blocktype_malformed_lists(self):    
        self.assertEqual(block_to_block_type("1. This List.\n3. Just skips a number."), BlockType.PARAGRAPH)