import os
import sys
import json
from colorama import Style, Fore 
from hashlib import md5


def generate_cache_name(dirPath: str):
    encoded = dirPath.encode()
    hashsum = md5(encoded).hexdigest()
    return os.path.join('cache', hashsum)


def write_cache(cache_name: str, dirDict: dict):
    with open(cache_name, "w+") as f:
        json.dump(dirDict, f)
    

def read_cache(cache_name: str):
    cache = {}
    if os.path.isfile(cache_name):
        with open(cache_name, "r") as f:
            cache = json.load(f)
    return cache
        

def compare_versions(dirOld: dict, dirNew: dict):
    old_copy, new_copy = dirOld.copy(), dirNew.copy()
    updated_list = []
    deleted_list = []
    created_list = dirNew.copy()
    for name in dirOld:
        if name not in dirNew.keys():
            deleted_list.append(name)
        elif dirOld[name] != dirNew[name]:
            updated_list.append(name)
            del created_list[name]
        else:
            del created_list[name]


    if created_list:
        print("Created")
        for name in new_copy:
            print(f"{Fore.GREEN}\t{name}{Style.RESET_ALL}")
    
    if deleted_list:
        print("Deleted")
        for name in deleted_list:
            print(f"{Fore.RED}\t{name}{Style.RESET_ALL}")

    if updated_list:
        print("Updated")
        for name in updated_list:
            print(f"{Fore.BLUE}\t{name}{Style.RESET_ALL}")


def scan_dir(dirPath: str): 
    if not os.path.isdir(dirPath):
        print(f"{dirPath} is not a directory")
        exit()

    res = {}

    for root, dirs, files in os.walk(dirPath):
        for name in files:
            filePath = os.path.join(root, name)
            res[filePath] = os.path.getmtime(filePath)
        for name in dirs:
            res[os.path.join(root, name)] = ""

    return res

   
if __name__ == '__main__':
    dirsPath = []
    if len(sys.argv) > 1:
        dirsPath = sys.argv[1:] 
    else:
        dirPath = input("Directory path: ")

    for dirPath in dirsPath: 
        print(f"Directory {dirPath}")
        dirDict = scan_dir(dirPath)
        
        cache_name = generate_cache_name(dirPath)
        dirOld = read_cache(cache_name)
        compare_versions(dirOld, dirDict)
        write_cache(cache_name, dirDict)
        print("\n\n")

