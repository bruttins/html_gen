import os
import shutil

def copy_site(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    src_content = os.listdir(src)
    for entry in src_content:
        src_entry = os.path.join(src, entry)
        dest_entry = os.path.join(dest, entry)
        if os.path.isfile(src_entry):
            shutil.copy(src_entry, dest_entry)
        elif os.path.isdir(src_entry):
            if not os.path.exists(dest_entry):
                os.mkdir(dest_entry)
            copy_site(src_entry, dest_entry)
