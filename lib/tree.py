from email.policy import default
from pathlib import Path
from itertools import islice
import os
from imports import CustomFont as Beauty


defaultValue = "5"
space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '
def main(dir_path: Path, level: int=-1, limit_to_directories: bool=False,
         length_limit: int=1000000):
    
    """Given a directory Path object print a visual tree structure"""
    dir_path = Path(dir_path) # accept string coerceable to Path
    files = 0
    directories = 0
    def inner(dir_path: Path, prefix: str='', level=-1):
        nonlocal files, directories
        if not level: 
            return # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else: 
            contents = list(dir_path.iterdir())
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space 
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                yield prefix + pointer + path.name
                files += 1
    print(dir_path.name)
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        print(line)
    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')
    print(f'\n{directories} directories' + (f', {files} files' if files else ''))

def tree(option:str, option2:int):
    if option == "normal" and option2 == defaultValue:
        main(Path.home() / os.getcwd())

    else:
        print(Beauty.Fore.RED + "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

def tree_man():
    print(Beauty.Style.DIM +"Command Manual: tree" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("tree : - List all files of the current directory in a tree format\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Directory content lister\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")
