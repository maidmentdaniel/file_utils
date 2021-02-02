import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse

def multidataset_to_single_dataset(
        src = "/home/intel2/surion/dev/darknet/data/images",
        class_ls = ['person', 'vehicle'],
        mode_ls = ['test', 'train', 'validation']):
    # read .names to get class list,
    # make sure the largest class is in the last class listed.
    cls_ls = class_ls
    print("combining data from:\t\t", cls_ls)
    print("into a compound set in:\t\t", cls_ls[-1])
    for cls in cls_ls[:-1]:
        print("processing class:\t", cls)
        for mode in mode_ls:
            print("\tprocessing mode:\t", mode)

            cur_img_ls_f = open(join(src, cls, mode+'.txt'), 'r')
            trgt_img_ls_f = open(join(src, cls_ls[-1], mode+'.txt'), 'r')

            cur_img_ls = [line.strip().split('/')[-1] for line in cur_img_ls_f.readlines()]
            trgt_img_ls = [line.strip().split('/')[-1] for line in trgt_img_ls_f.readlines()]

            #merge classes:
            #iterate through images in source directory = join(src, cls, mode)
            for cur_img in cur_img_ls:
                #if the current image is already in the target destination
                if(cur_img in trgt_img_ls):
                    #   Build a list of annotations from the annotation file
                    #   corresponding to the considered image in the target directory.
                    trgt_annot_pth = join(src, cls_ls[-1], mode, cur_img.split('.')[0]+'.txt')
                    #open annotation file at target image
                    trgt_annot_f = open(trgt_annot_pth, 'r')
                    #generate a list of existing annotations in the target drectory
                    trgt_annot_ls = [line.strip() for line in trgt_annot_f]
                    trgt_annot_f.close()

                    #   Build a list of the annotations from the annotation file
                    #   corresponding to the considered image in the source directory.
                    cur_annot_pth = join(src, cls, mode, cur_img.split('.')[0]+'.txt')
                    #open annotation file of current image
                    cur_annot_f = open(cur_annot_pth, 'r')
                    #generate list of current image annotations
                    cur_annot_ls = [line.strip() for line in cur_annot_f]
                    cur_annot_f.close()

                    #   Loop through list annotations of source directory and add the
                    #   annotations to the list of annotations in the target directory.
                    for cur_annot in cur_annot_ls:
                        #check if the current annotation list is already in the target annotation list
                        if(not cur_annot in trgt_annot_ls):
                            #if not then append the current annotation to the annotation list
                            trgt_annot_ls.append(cur_annot)
                    #overwrite the target annotation list
                    #open annotation file at target image
                    trgt_annot_f = open(trgt_annot_pth, 'w')
                    for trgt_annot in trgt_annot_ls:
                        # temp_annot = trgt_annot.split(' ')
                        # temp_annot[0] = str(len(cls_ls)-1)
                        trgt_annot_f.write(trgt_annot+'\n')
                    #close the annotation file.
                    trgt_annot_f.close()
                else:
                    cur_img_pth = join(src, cls, mode, cur_img)
                    trgt_img_pth = join(src, cls_ls[-1], mode, cur_img)
                    cur_annot_pth = join(src, cls, mode, cur_img.split('.')[0]+'.txt')
                    trgt_annot_pth = join(src, cls_ls[-1], mode, cur_img.split('.')[0]+'.txt')
                    #move the current image annotation to the target location
                    os.rename(cur_img_pth, trgt_img_pth)
                    #move the annotation
                    os.rename(cur_annot_pth, trgt_annot_pth)

            cur_img_ls_f.close()
            trgt_img_ls_f.close()

    return None

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Take a collection of classes and combine them into a single.')
        parser.add_argument("--src", required=True,
                            help="Source path.")
        parser.add_argument("--class_ls", required=True,
                            help='The list of classes to combine.\ni.e. \'person\', \'vehicle\'',
                            type=lambda s: s.split(','))
        parser.add_argument("--mode_ls", required=True,
                            help='The list of subdirectories to scan through,\nthese will be reflected on the other side\ni.e. test/Truck --> vehicle/test.\nPassed as comma seprated list of strings.',
                            type=lambda s: s.split(','))
        arg = parser.parse_args()
        multidataset_to_single_dataset(arg.src, arg.class_ls, arg.mode_ls)
