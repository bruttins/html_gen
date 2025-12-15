from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_list = node.text.split(delimiter)
            if len(split_list) >1 and len(split_list) % 2 == 0:
                raise Exception("Invalid Markdown, please set proper delimiter.")
            for index, block in enumerate(split_list):
                if index % 2 == 0:
                    if block == "":
                        pass
                    else:
                        new_node = TextNode(block, TextType.TEXT)
                        new_nodes.append(new_node)                
                else:
                    new_node = TextNode(block, text_type)
                    new_nodes.append(new_node)
    return new_nodes
