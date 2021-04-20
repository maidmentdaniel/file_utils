import cv2
import os
import sys
import argparse
from os.path import join
import numpy as np
from numpy import random
import shutil
import uuid
from progress.bar import Bar
import shutil
import time

formatlist = ('avi', 'mkv', 'mp4', 'dav')

def update_progress(label, progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\r{0}: [{1}] {2}% {3}".format(label, "#"*block + "-"*(barLength-block), round(progress*100, 4), status)
    sys.stdout.write(text)
    sys.stdout.flush()

def extractImages(pathIn, pathOut, vidnm):
    count = 0
    N = get_frame_count(pathIn)
    if(N < 10):
        frame_skip = 1
    elif(10 <= N < 100):
        frame_skip = 2
    elif(100 <= N < 1000):
        frame_skip = 20
    else:
        frame_skip = 50
    bar = Bar("Extracting", max=N)
    vidcap = cv2.VideoCapture(pathIn)
    while(vidcap.grab()):
        if(count%frame_skip==0):
            flag, image = vidcap.retrieve()
            imagenm = vidnm + f"_frame_{count}.jpg"
            cv2.imwrite(join(pathOut, imagenm), image)     # save frame as JPEG file
        count += 1
        bar.next()
    bar.finish()

def recursive_dir_extract(src_path, target_path):
    if(not os.path.isdir(target_path)):
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

def get_frame_count(path):
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def src_extract(src_ls, target_dir):
    for src in src_ls:
        if(not os.path.isdir(src)):
            print(src_dir, 'is not a path')
            sys.exit(0)
    for src in src_ls:
        length = len(os.listdir(src))
        print(length)
        print(f"{join(*src.split('/')[-2:])}")
        count = 0
        for entry in os.scandir(src):
            if(entry.is_file()):
                if(not os.path.isdir(join(target_dir, entry.name.split('.')[0]))):
                    id = str(uuid.uuid4())
                    os.mkdir(join(target_dir, id))
                    target_path = join(target_dir, id)
                    print("Processing", entry.name, '\nas', id, '\n')
                    extractImages(entry.path, target_path, id)
                    ftype = entry.name.split('.')[-1]
                    print("Copying", entry.name, 'to:\n', join(src, id+'.'+ftype), '\n')
                    shutil.move(entry.path, join(src, id+'.'+ftype))
            count += 1
            update_progress("Files Processed", count/length)
    return True



def gen_file_list(src_path):
    filename = join(src_path, "test_data.txt")
    file = open(filename, 'w+')
    src_dir = os.scandir(src_path)
    for entry in src_dir:
        if(entry.name.split('.')[-1] in ('jpg', 'jpeg', 'png')):
            file.write(os.path.abspath(entry.path)+'\n')
    file.close()

if __name__ == "__main__":
# gen_file_list(target_path)
# cwd = os.path.abspath('.')
# target_path = join(cwd, "extracted_frames")
# recursive_dir_extract(src, target_path)
# gen_file_list(target_path)
# print(os.path.isdir(src))
    src_ls = [
        '/media/ryzen1/5F76-11D9/footage/axis/snippets',
        '/media/ryzen1/5F76-11D9/footage/misc_client/snippets',
        '/media/ryzen1/5F76-11D9/footage/sancor/snippets']
    src_extract(src_ls, '/media/ryzen1/5F76-11D9/footage/extracted_frames')

# get_frame_count('/media/ryzen1/5F76-11D9/footage/axis/snippets/ff817cbd-8223-4bd3-9033-24770cd3c387.mp4')
