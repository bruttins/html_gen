from markdownsplit import text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType

def inline_helper(text):
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children

def heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level:].lstrip()
    tag = f"h{level}"
    children = inline_helper(text)
    return ParentNode(tag, children=children)

def paragraph_node(block):
    lines = block.split("\n")
    text = " ".join(line.strip() for line in lines)
    children = inline_helper(text)
    return ParentNode("p", children=children)

def code_node(block):
    if block.startswith("```"):
        lines = block.split("\n")
        inner = "\n".join(lines[1:-1]) + "\n"
    else:
        inner = block
    text_node = TextNode(inner, TextType.TEXT)
    code_child = text_node_to_html_node(text_node)
    code_node = ParentNode("code", children=[code_child])
    return ParentNode("pre", children=[code_node])
    
def quote_node(block):
    lines = block.split("\n")
    new_block = []
    for line in lines:
        if not line.strip():
            continue
        if line.startswith(">"):
            clean_line = line[1:].lstrip()
        else:
            clean_line = line
        new_block.append(clean_line)
    text = " ".join(new_block)
    inline_children = inline_helper(text)
    return ParentNode("blockquote", children=inline_children)

def unordered_list_node(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        if not line.strip():
            continue
        clean_line = line.lstrip("- ")
        grandchildren = inline_helper(clean_line)
        children.append(ParentNode("li", children=grandchildren))
    return ParentNode("ul", children=children)

def ordered_list_node(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        if not line.strip():
            continue
        dot_index = line.find(". ")
        if dot_index == -1:
            continue
        clean_line = line[dot_index + 2:]
        grandchildren = inline_helper(clean_line)
        children.append(ParentNode("li", children=grandchildren))
    return ParentNode("ol", children=children)


def blockloop(blocks):
    nodes = []
    for block in blocks:
        btype = block_to_block_type(block)
        if btype == BlockType.HEADING:
            nodes.append(heading_node(block))
        elif btype == BlockType.PARAGRAPH:
            nodes.append(paragraph_node(block))
        elif btype == BlockType.CODE:
            nodes.append(code_node(block))
        elif btype == BlockType.QUOTE:
            nodes.append(quote_node(block))
        elif btype == BlockType.UNORDERED_LIST:
            nodes.append(unordered_list_node(block))
        elif btype == BlockType.ORDERED_LIST:
            nodes.append(ordered_list_node(block))
    return nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = blockloop(blocks)
    return ParentNode("div", children=children)
