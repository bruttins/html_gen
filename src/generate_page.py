import os
from md_to_html import markdown_to_html_node
from htmlnode import HTMLNode
from extract_md_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as f:
        from_file = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()

    root = markdown_to_html_node(from_file)
    html_content = root.to_html()
    title = extract_title(from_file)

    full_html = template_file.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    dirpath = os.path.dirname(dest_path)
    if dirpath != "" and not os.path.exists(dirpath):
        os.makedirs(dirpath)
    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_page_recursively(dir_path_content, template_path, dest_dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path_content):
        for filename in filenames:
            if filename.endswith(".md"):
                from_path = os.path.join(dirpath, filename)
                dest_path = os.path.join(dest_dir_path, os.path.relpath(from_path, dir_path_content))
                dest_path = dest_path[:-3] + ".html"
                generate_page(from_path, template_path, dest_path)
