import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def combine_class_dataset(src, dst_path, new_class, cur_class_ls, mode_ls=["test", "validation", "train"]):
    print('Scanning:', src)
    if(not isdir(src)):
        print(src, 'is not a directory')
        return None
    cwd_obj = os.scandir(src)
    if(not isdir(join(dst_path,new_class))):
        print("making directory:", join(dst_path,new_class))
        mkdir(join(dst_path, new_class))
    for mode in mode_ls:
        if(not isdir(join(dst_path,new_class, mode))):
            print("making directory:", join(dst_path,new_class, mode))
            mkdir(join(dst_path,new_class, mode))
    print(src.split('/')[-1])
    for cwd_entry in cwd_obj:
        if(cwd_entry.is_dir() and cwd_entry.name in mode_ls):
            print('\t',cwd_entry.name)
            mode_obj = os.scandir(cwd_entry.path)
            for mode_entry in mode_obj:
                if(mode_entry.is_dir() and mode_entry.name in cur_class_ls):

                    # print('\t\t',mode_entry.name)
                    class_obj = os.scandir(mode_entry.path)
                    # progress bar intialised here
                    length = len(os.listdir(mode_entry.path))
                    bar = Bar(f'\t{mode_entry.name}:\t', max=length)
                    for entry in class_obj:
                        id, type = entry.name.split('.')
                        target_path = join(dst_path, new_class, cwd_entry.name)
                        if(type =='jpg' or type =='jpeg'):
                            # copy jpeg to desination
                            target_path = join(dst_path, new_class, cwd_entry.name)
                            if(not isfile(target_path)):
                                os.rename(entry.path, join(target_path, entry.name))
                        elif(type =='txt'):
                            src_annot_file = open(entry.path, 'r')
                            dst_annot_file = open(join(target_path, entry.name), 'a+')
                            for line in src_annot_file:
                                cl, x1, x2, y1, y2 = line.strip().split(' ')
                                x1, x2, y1, y2 = map(float, [x1, x2, y1, y2])
                                xc = (x1+x2)/2
                                yc = (y1+y2)/2
                                w = x2-x1
                                h = y2-y1
                                re_annot = f"{new_class} {xc:} {yc:} {w:} {h:}\n"
                                dst_annot_file.write(re_annot)
                            src_annot_file.close()
                            dst_annot_file.close()
                        bar.next()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take a collection of classes and combine them into a single.')
    parser.add_argument("--src", required=True,
                        help="Source path.")
    parser.add_argument("--dst", required=True,
                        help='Destination path.')
    parser.add_argument("--new_class", required=True,
                        help='The name of the new combined class\ni.e. \'vehicle\' is the combined class of \'truck\'and \'car\'.')
    parser.add_argument("--cur_class_ls", required=True,
                        help='List of classes to combine. Passed as comma separated list of strings, i.e., \'Truck\',\'Car\'',
                        type=lambda s: s.split(','))
    parser.add_argument("--mode_ls", required=True,
                        help='The list of subdirectories to scan through,\nthese will be reflected on the other side\ni.e. test/Truck --> vehicle/test.\nPassed as comma seprated list of strings.',
                        type=lambda s: s.split(','))
    arg = parser.parse_args()
    combine_class_dataset(arg.src, arg.dst, arg.new_class, arg.cur_class_ls,
                         arg.mode_ls)
