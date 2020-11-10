import os
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
    with open(cache_name, "r") as f:
        cache = json.load(f)
    return cache
        

def compare_versions(dirOld, dirNew):
    pass


if __name__ == '__main__':
    dirPath = input("Directory path: ")
    dirDict = {}

    if not os.path.isdir(dirPath):
        print(f"{dirPath} is not a directory")
        exit()

    for root, dirs, files in os.walk(dirPath):
        for name in files:
            filePath = os.path.join(root, name)
            dirDict[filePath] = os.path.getctime(filePath)
        for name in dirs:
            dirDict[name] = ""

    cache_name = generate_cache_name(dirPath)

    dirOld = read_cache(cache_name)
    print(dirOld)
    compare_versions(dirDict, dirOld)
    
    write_cache(cache_name, dirDict)

