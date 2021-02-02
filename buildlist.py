import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def buildlist(src):
    if(isdir(src)):
        print("Building list of images in:")
        print(src)
        wd = os.scandir(src)
        for mode in wd:
            if(mode.is_dir()):
                length = len(os.listdir(mode.path))
                print()
                bar = Bar(f'Building {mode.name}:\t', max=length)
                file = open(join(src, mode.name+'.txt'), 'w+')
                mode_dir = os.scandir(mode.path)
                for entry in mode_dir:
                    if(entry.is_file() and entry.name.split('.')[-1] == 'jpg'):
                        file.write(entry.path+'\n')
                    bar.next()
                file.close()
    else:
        print(src, "is not a directory.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build the image list for each sub directory in --src')
    parser.add_argument("--src", required=True,
                        help="Source path.")
    arg = parser.parse_args()
    buildlist(arg.src)
