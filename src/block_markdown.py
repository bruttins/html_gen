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

def all_lines_start_with_num(block):
    lines = block.split("\n")
    expected_num = 1
    for line in lines:
        if not line.startswith(f"{expected_num}. "):
            return False
        expected_num += 1
    return True

def block_to_block_type(md_block):
    lines = md_block.split("\n")
    if md_block.startswith(("# ","## ","### ","#### ","##### ", "###### ")):
        return BlockType.HEADING
    elif md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all_lines_start_with_num(md_block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
