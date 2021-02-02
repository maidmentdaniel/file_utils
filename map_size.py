import os
from os.path import getsize, isdir, isfile, join
from os import mkdir
import shutil
import subprocess
import sys
from progress.bar import Bar

def mapsize(path, tabstr, ignore_ls=[]):
    size = 0
    pathname = tabstr+path.split('/')[-1]
    if(isdir(path)):
        cwd_obj = os.scandir(path)
        print(pathname)
        for cwd_entry in cwd_obj:
            if(cwd_entry.name not in ignore_ls):
                size += mapsize(cwd_entry.path, tabstr+'\t')
        if(size>10**9):print(tabstr, f"{size/(10**9):6.1f}GB")
        elif(size<10**9):print(tabstr, f"{size/(10**6):6.1f}MB")
    elif(isfile(path)):
        size = getsize(path)
    return size
