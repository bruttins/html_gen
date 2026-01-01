import unittest
from extract_md_title import extract_title

class TextExtractMDTitle(unittest.TestCase):
    def test_normalMDStructure(self):
        md = """
# Big Title
## First Topic
This is just paragraph-text and some **inline-markdown**.
"""
        extracted = extract_title(md)
        title = "Big Title"
        self.assertEqual(extracted, title)

    def test_empty_firstline(self):
        md = """

# Big Title
## First Topic
This is just paragraph-text and some **inline-markdown**.
""" 
        extracted = extract_title(md)
        title = "Big Title"
        self.assertEqual(extracted, title)

    def test_normalMDStructure_emptyspaces(self):
        md = """
#   Big Title
## First Topic
This is just paragraph-text and some **inline-markdown**.
""" 
        extracted = extract_title(md)
        title = "Big Title"
        self.assertEqual(extracted, title)  

    def test_noh1(self):
        md = """
## First Topic
This is just paragraph-text and some **inline-markdown**.
""" 
        with self.assertRaises(Exception):
            extract_title(md)

    def test_h2first(self):
        md = """
## First Topic
# Big Title
This is just paragraph-text and some **inline-markdown**.
""" 
        extracted = extract_title(md)
        title = "Big Title"
        self.assertEqual(extracted, title)  
