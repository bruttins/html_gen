from enum import Enum

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    current = []
    in_code = False
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped.strip().startswith("```"):
            if in_code:
                current.append(stripped)
                blocks.append("\n".join(current).strip())
                current = []
                in_code = False
            else:
                if current:
                    blocks.append("\n".join(current).strip())
                    current = []
                in_code = True
                current.append(stripped)
            continue
        if in_code:
            current.append(stripped)
            continue
        if not stripped.strip():
            if current:
                blocks.append("\n".join(current).strip())
                current = []
            continue
        if stripped.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
            if current:
                blocks.append("\n".join(current).strip())
                current = []
            blocks.append(stripped)
            continue
        current.append(stripped)
    if current:
        blocks.append("\n".join(current).strip())

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
