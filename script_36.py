import sys
import pathlib
import os
import re
import shutil

def scan(filename, text='python'):
    with open(filename) as f:
        for line in f:
            if re.search(text, line, re.I):
                return True
    return False

def search_and_copy(f_substr, src_path, dest_path):
    path = pathlib.Path(src_path)
    files = path.glob('**/{}*'.format(f_substr))

    for file in (str(f) for f in files):
        if scan(str(file), 'python'):
            print('The file: "{}" contains text: "python" in it. copying ...'
                  .format(file))
            try:
                shutil.copy(file, dest_path)
            except FileNotFoundError as e:
                print('Target directory not found: ' + dest_path)

if __name__ == '__main__':
    f_substr, src_path, dest_path = sys.argv[1:4]
    search_and_copy(f_substr, src_path, dest_path)
