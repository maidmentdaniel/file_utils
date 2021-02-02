import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def backup_files(src, dest, cwd):
    length = len(os.listdir(src))
    bar = Bar('Copying', max=length)
    count = 0
    prgrs = 0
    fail_f = open(join(cwd, 'failure.txt'), 'w')
    if(os.path.isdir(src)):
        src_obj = os.scandir(src)
        for entry in src_obj:
            bar.next()
            if(os.path.isfile(entry.path)):
                if(not os.path.exists(join(dest, entry.name))):
                    try:
                        shutil.copy(entry.path, join(dest, entry.name))
                    except:
                        print(entry.name, "copy failed.")
                        fail_f.write(entry.path + '\n')
                else:print(entry.name, "already exists at destination.")
            else: print(entry.name, 'is not a file.')
    else:
        print(src, "is not a directory.")

    fail_f.close()
    bar.finish()

def backup_annotations(src):
    if(os.path.isdir(src)):
        backup_dir = join(src, 'backup_annotations')
        if(not os.path.isdir(backup_dir)):
            os.mkdir(backup_dir)
        dir_obj = os.scandir(src)
        print("scanning:", src)
        for entry in dir_obj:
            f_nm = entry.name
            ftype = f_nm.split('.')[-1]
            if(ftype == 'txt'):
                shutil.copy(entry.path, join(backup_dir, f_nm))
    else: print(src, "does not exist.")
    return None

if __name__ == "__main__":
    cur_dir = os.getcwd()

    # multidataset_to_single_dataset(src, mode_ls = ['validation'])

    # rename_annotations(src, cls_ls=["person"], mode_ls=["train"])

    # buildlist(join(src, "person"))
    # buildlist(join(src, "vehicle"))

    # rename_annotations(src, cls_ls=["person"],
    #                     mode_ls=['test', 'validation'],
    #                     index=0, label='vehicle')

    # check_annotations(src, cls="person", mode_ls=['test', 'train', 'validation'])

    # annotation_lbl_to_idx(src, cls_ls=['person'],
    #                     mode_ls=['test', 'train'],
    #                     lbl_ls=['person', 'vehicle'])
    # backup_files(src, dest, cur_dir)

    src = "/home/intel2/surion/dev/darknet/data/images/person/train"
    renumber_annotation(src, '2', '1')
    # combine_class_dataset(cur_dir, src,
                        # 'vehicle', ['Truck', 'Car'],
                        # mode_ls=["test", 'train'])
