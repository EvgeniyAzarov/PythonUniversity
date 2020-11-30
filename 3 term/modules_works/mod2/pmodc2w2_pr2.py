from os import listdir
from os.path import isfile, join, getmtime
from shutil import copyfile
import sys


def sync(dir1, dir2):
    files1 = [f for f in listdir(dir1) if isfile(join(dir1, f))]
    files2 = [f for f in listdir(dir2) if isfile(join(dir2, f))]
    
    for f in files1:
        if not f in files2:
           copyfile(join(dir1, f), join(dir2, f)) 
    
    for f in files2:
        if not f in files1:
           copyfile(join(dir2, f), join(dir1, f)) 
        else:
            f1 = join(dir1, f)
            f2 = join(dir2, f)
            
            if getmtime(f1) > getmtime(f2):
                copyfile(f1, f2)
            else:
                copyfile(f2, f1)
            
    
if __name__ == '__main__':
    path1 = sys.argv[1] 
    path2 = sys.argv[2]

    sync(path1, path2)
