import os
import shutil
from copystatic import copy_site

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_site("./static", "./public")

if __name__ == "__main__":
    main()
