import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if not extract_markdown_images(node.text):
                new_nodes.append(node)
            else:
                images = extract_markdown_images(node.text)
                original_text = node.text
                for image in images:
                    markdown = f"![{image[0]}]({image[1]})"
                    sections = original_text.split(markdown, 1)
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    if len(sections) != 2:
                        raise ValueError("Invalid Markdown")
                    else:
                        new_nodes.append(TextNode(image[0], TextType.IMAGE,image[1]))
                    original_text = sections[1]
                if len(original_text) > 0:
                    new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if not extract_markdown_links(node.text):
                new_nodes.append(node)
            else:
                links = extract_markdown_links(node.text)
                original_text = node.text
                for link in links:
                    markdown = f"[{link[0]}]({link[1]})"
                    sections = original_text.split(markdown, 1)
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    if len(sections) != 2:                         
                        raise ValueError("Invalid Markdown")
                    else:
                        new_nodes.append(TextNode(link[0], TextType.LINK,link[1]))
                    original_text = sections[1]
                if len(original_text) > 0:
                    new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
