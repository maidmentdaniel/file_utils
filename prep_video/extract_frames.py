import cv2
import os
import sys
import argparse
from os.path import join
import numpy as np
from numpy import random
import shutil

formatlist = ('avi', 'mkv', 'mp4', 'dav')

def extractImages(pathIn, pathOut, vidnm, frame_n = 30):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    while(vidcap.grab()):
        if(count%frame_n==0):
            flag, image = vidcap.retrieve()
            imagenm = vidnm + f"_frame_{count}.jpg"
            cv2.imwrite(join(pathOut, imagenm), image)     # save frame as JPEG file
        count += 1

def recursive_dir_extract(src_path, target_path):
    if(not  os.path.isdir(target_path)):
        print("making directory:", target_path)
        os.mkdir(target_path)
    if(src_path == target_path):
        print("attempted to scan target")
    else:
        src_dir = os.scandir(src_path)
        for entry in src_dir:
            if(entry.is_dir()):
                print("processing directory:", entry.name)
                recursive_dir_extract(entry.path, target_path)
            elif(entry.is_file()):
                filetype = entry.name.split('.')[-1]
                filename = entry.name.split('.')[0]
                if(filetype in formatlist):
                    print("proccessing:\n" + entry.name)
                    # 900 = 30[f/s]*60[s/min]*(1/2) ==> 2 frames per minute processed
                    extractImages(entry.path, target_path, entry.name, 225)
        src_dir.close()

def gen_file_list(src_path):
    filename = join(src_path, "test_data.txt")
    file = open(filename, 'w+')
    src_dir = os.scandir(src_path)
    for entry in src_dir:
        if(entry.name.split('.')[-1] in ('jpg', 'jpeg', 'png')):
            file.write(os.path.abspath(entry.path)+'\n')
    file.close()

if __name__ == "__main__":
    src = "E:\\surion_footage_3"
    target_path = "C:\\dev\\extracted_frames_3\\"
    # gen_file_list(target_path)
# cwd = os.path.abspath('.')
# target_path = join(cwd, "extracted_frames")
recursive_dir_extract(src, target_path)
gen_file_list(target_path)
# print(os.path.isdir(src))
