from markdownsplit import text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode
from textnode import text_node_to_html_node

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
    return HTMLNode(tag, children=children)

def paragraph_node(block):
    children = inline_helper(block)
    return HTMLNode("p", children=children)

def code_node(block):
    #DON'T USE INLINE_HELPER!

def quote_node(block):
    #prepare text
    children = inline_helper(text)
    return HTMLNode(

def unordered_list_node(block):
    #prepare list-text
    children = inline_helper(text)
    return HTMLNode(

def ordered_list_node(block):
    #prepare list-text
    children = inline_helper(text)
    return HTMLNode(

def blockloop(blocks):
    nodes = []
    for block in blocks:
        blocktype = block_to_block_type(block)
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
