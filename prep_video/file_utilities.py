import os
from os import path
from os.path import join

def delete_duplicates(src):
    dir_obj = os.scandir(src)
    for entry in dir_obj:
        filenm = entry.name.split('.')[0]
        filetyp= entry.name.split('.')[-1]
        if(filenm[-4:] == '_002'):
            print("deleting:\t", entry.path)
            os.remove(entry.path)
        elif(filenm[-4:] == '_001'):
            print("deleting:\t", entry.path)
            os.remove(entry.path)
        elif(filetyp == 'txt'):
            print("deleting:\t", entry.path)
            os.remove(entry.path)


if __name__ == "__main__":
    # delete_duplicates("")
