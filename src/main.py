import os
import shutil
from copystatic import copy_site
from generate_page import generate_page

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_site("./static", "./public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
