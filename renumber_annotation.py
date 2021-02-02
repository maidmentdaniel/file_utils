import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def renumber_annotation(src, current='1', new='2'):
    print("Processing:", src)
    length = len(os.listdir(src))/2
    bar = Bar('Replacing', max=length)
    if(os.path.isdir(src)):
        dir_obj = os.scandir(src)
        for entry in dir_obj:
            f_nm = entry.name
            ftype = f_nm.split('.')[-1]
            if(ftype == 'txt'):
                annot_ls = []
                annot_f = open(entry.path, 'r')
                [annot_ls.append(line.strip().split(' ')) for line in annot_f]
                annot_f.close()
                annot_f = open(entry.path, 'w')
                for annot in annot_ls:
                    if(annot[0]==current):
                        annot[0] = new
                    annot_f.write(' '.join(annot)+'\n')
                annot_f.close()
                bar.next()
    else:
        print(src, "does not exist.")
    return None
if __name__ == "__main__":
