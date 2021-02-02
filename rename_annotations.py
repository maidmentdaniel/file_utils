import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def rename_annotations(
        src="/home/intel2/surion/dev/darknet/data/images",
        cls_ls=['person'],
        mode_ls=['test', 'train', 'validation'],
        index=0, label='person'):
    print("class list:\t\t", cls_ls)
    for cls in cls_ls:
        print("processing class:\t", cls)
        for mode in mode_ls:
            print("\tprocessing mode:\t", mode)
            mode_obj = os.scandir(join(src, cls, mode))
            for entry in mode_obj:
                filetype = entry.name.split('.')[-1]
                img_id = entry.name.split('.')[0]
                if(filetype == 'txt'):
                    print(entry.name)
                    #open annotation file
                    annot_f = open(entry.path, 'r')
                    #create list of annotations
                    annot_ls = [line.strip() for line in annot_f]
                    annot_f.close()
                    #reopen annotation file for rewriting
                    annot_f = open(entry.path, 'w')
                    for annot in annot_ls:
                        temp_annot = annot.split(' ')
                        if(temp_annot[0].isdigit()):
                            print("\t\t is digit")
                            if(int(temp_annot[0]) == index):
                                temp_annot[0] = label
                        annot_f.write(' '.join(temp_annot)+'\n')
                    annot_f.close()
    return None
    
if __name__ == "__main__":
