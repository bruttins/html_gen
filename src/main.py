import os
import sys
import shutil
from copystatic import copy_site
from generate_page import generate_page_recursively

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    copy_site("./static", "./docs")
    
    generate_page_recursively(basepath, "content", "template.html", "docs")

if __name__ == "__main__":
    main()
