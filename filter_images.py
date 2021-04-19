import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar
import argparse
import json
import numpy as np

coco_names = [ 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
         'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
         'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
         'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
         'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
         'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
         'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
         'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
         'hair drier', 'toothbrush' ]

check_ls = ['person', 'car', 'truck', 'bus', 'dog']

def filter_images_by_label(src):
    print("Scanning source:", src)
    if(not isdir(src)):
        print(src, "does not exit.")
    else:
        src_obj = os.scandir(src)
        for i, entry in enumerate(src_obj):
            ftype = entry.name.split('.')[-1]
            if(len(entry.name.split('.')[:-1])>1):
                fnm = '.'.join(entry.name.split('.')[:-1])
            else:
                fnm = entry.name.split('.')[0]
            if(ftype=='txt'):
                annot_f = open(entry.path, 'r')
                annot_ls = [line.strip().split(' ') for line in annot_f]
                annot_f.close()
                class_ls = [coco_names[int(annot[0])] for annot in annot_ls]
                print(fnm, class_ls)
                if(not any(item in check_ls for item in class_ls)):
                    os.remove(join(src, fnm+'.jpg'))
                    os.remove(entry.path)
            elif(ftype=='jpg'):
                if(not isfile(join(src, fnm+'.txt'))):
                    os.remove(entry.path)
    return None

def filter_images_by_source(src, dst):
    np.random.seed(1000)
    print("Scanning source:", src)
    if(not isdir(src)):
        print(src, "does not exit.")
    else:
        dir_ls = os.listdir(src)
        image_ls = []
        for entry in dir_ls:
            if(entry.split('.')[-1] == 'jpg'):
                image_ls.append(entry)
        N = len(image_ls)
        n_ls = np.random.randint(0, N, int(0.025*N))
        for i in n_ls:
            shutil.copy(join(src, image_ls[i]), join(dst, image_ls[i]))
    return None
    #     src_ls = [['_'.join(fnm.split('_')[0:-2]), fnm.split('_')[-2], fnm.split('_')[-1]] for fnm in dir_ls]
    #     src_dict = {}
    #
    #     for entry in src_ls:
    #         if(entry[0] in src_dict.keys()):
    #             src_dict[entry[0]] +=1
    #         else:
    #             src_dict[entry[0]] = 1
    #
    #     i = 0
    #     while(i<len(src_ls)-1):
    #         dict_key = src_ls[i][0]
    #         pre_dict_key = src_ls[i-1][0]
    #         dict_value = src_dict[dict_key]
    #         n = np.random.randint(0, dict_value)
    #         if(dict_value>1 and dict_key==pre_dict_key):
    #             for j in
    #             # print(pre_dict_key, True)
    #             print(pre_dict_key, dict_value, n)
    #             i = i-1+dict_value
    #         i += 1
    #             # for j in range(pre_dict_key):
    #
    #         #     print(src_dict[src_ls[i][0]])
    #         #     print(src_dict[src_ls[i-1][0]])
    #
    # return None
if __name__ =="__main__":
    src = "C:\\dev\\extracted_frames_1\\extracted_frames_2"
    dst = "C:\\dev\\extracted_frames_1\\exctracted_frames_2_filtered"
    filter_images_by_source(src, dst)

    # filter_images_by_label(src)
