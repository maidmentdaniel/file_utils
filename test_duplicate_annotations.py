import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def test_duplicate_annotations(src):
    length = len(os.listdir(src))/2
    if(os.path.isdir(src)):
        dir_obj = os.scandir(src)
        for entry in dir_obj:
            f_nm = entry.name
            ftype = f_nm.split('.')[-1]
            if(ftype == 'txt'):
                annot_ls = []
                annot_f = open(entry.path, 'r')
                [annot_ls.append(line.strip()) for line in annot_f]
                annot_f.close()
                annot_ls_clean = list(dict.fromkeys(annot_ls))
                if(len(annot_ls_clean)<len(annot_ls)):
                    print(f_nm, f"has {len(annot_ls)-len(annot_ls_clean)} duplicates")
    else:
        print(src, "does not exist.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True)
    arg = parser.parse_args()
    test_duplicate_annotations(arg.src)
