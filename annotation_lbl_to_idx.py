import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def annotation_lbl_to_idx(src,
                        mode_ls=['test', 'train', 'validation'],
                        class_ls=['person', 'vehicle']):
    for mode in mode_ls:
        if(isdir(join(src, mode))):
            mode_obj = os.scandir(join(src, mode))

            length = len(os.listdir(join(src, mode)))
            bar = Bar(f'Processing {mode}:', max=length)

            for entry in mode_obj:
                filetype = entry.name.split('.')[-1]
                img_id = entry.name.split('.')[0]
                if(filetype == 'txt'):
                    #open annotation file
                    annot_f = open(entry.path, 'r')
                    #create list of annotations
                    annot_ls = [line.strip() for line in annot_f]
                    annot_f.close()
                    #reopen annotation file for rewriting
                    annot_f = open(entry.path, 'w')
                    for annot in annot_ls:
                        temp_annot = annot.split(' ')
                        # print(temp_annot)
                        temp_annot[0] = str(class_ls.index(temp_annot[0]))
                        annot_f.write(' '.join(temp_annot)+'\n')
                        # print(temp_annot)
                    annot_f.close()
                bar.next()
            print()
        else:
            print(join(src, mode), "is not a directory.")
    return None

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Scan through the annotations and convert the class labels to indicies.')
        parser.add_argument("--src", required=True,
                            help="Source path.")
        parser.add_argument("--class_ls", required=True,
                            help='The list of class labels to convert to indices.\nThe list should be passed to match the order given in the .names file',
                            type=lambda s: s.split(','))
        parser.add_argument("--mode_ls", required=True,
                            help='The list of subdirectories to scan through,\nthese will be reflected on the other side\ni.e. test/Truck --> vehicle/test.\nPassed as comma seprated list of strings.',
                            type=lambda s: s.split(','))
        arg = parser.parse_args()
        annotation_lbl_to_idx(arg.src, arg.mode_ls, arg.class_ls)
