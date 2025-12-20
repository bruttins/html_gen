from enum import Enum

def markdown_to_blocks(markdown):
    blocks = []
    splitblocks = markdown.split("\n\n")
    for block in splitblocks:
        block = block.strip()
        if block != "":
            blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(md_block):
    if md_block.startswith(("# ","## ","### ","#### ","##### ", "###### "):
        return BlockType.HEADING
    elif md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE
    elif #how to catch every line?
