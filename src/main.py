import os
import shutil
from copystatic import copy_site
from generate_page import generate_page_recursively

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_site("./static", "./public")
    
    generate_page_recursively("content", "template.html", "public")

if __name__ == "__main__":
    main()
