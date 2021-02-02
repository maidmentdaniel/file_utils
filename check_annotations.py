import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def check_annotations(src, cls, mode_ls=["test", "validation", "train"]):
    print("processing:", cls)
    for mode in mode_ls:
        print("processing:\t", mode)
        trgt_pth = join(src, cls, mode)
        if(not os.path.exists(trgt_pth)):
            print(trgt_pth, "does not exist")
        else:
            dir_obj = os.scandir(trgt_pth)
            for entry in dir_obj:
                filetype = entry.name.split('.')[-1]
                if(filetype == 'txt'):
                    annot_f = open(entry.path, 'r')
                    annot_ls = [line.strip().split(' ') for line in annot_f]
                    annot_f.close()
                    for annot in annot_ls:
                        # print(annot)
                        if(annot[0].isdigit()):
                            print(entry.path, "has digital annotations")
    return None

if __name__ == "__main__":
