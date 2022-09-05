
import os
import getpass
import platform

from imports import CustomFont as Beauty

defaultValue = "5"

  

def cd(options:str, options2:str):
    if options == ".." and options2 == defaultValue:
        a = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        os.chdir(a)

    if options == "normal" and options2 == defaultValue:
        print(Beauty.Fore.YELLOW + "Missing folder" + Beauty.Fore.RESET)
    elif options is not None and options2 == defaultValue:
        try:
            
            os.chdir(os.getcwd() + "/" +options)

        except NotADirectoryError:
            print("This directory does not exist")

        except PermissionError:
            print(Beauty.Fore.YELLOW + "Missing permissions to change directory, maybe start as admin" + Beauty.Fore.RESET)

    elif options == "jump" and options2 == "downloads":
        if platform.system() == "Windows":
            os.chdir("c:\\Users\\" + getpass.getuser() + "\\downloads")
        if platform.system() != "Windows":
            print(Beauty.Fore.RED + "OS not supported jet !" + Beauty.Fore.RESET)

    elif options == "jump" and options2 == "documents":
        if platform.system() == "Windows":
            os.chdir("c:\\Users\\" + getpass.getuser() + "\\documents")
        if platform.system() != "Windows":
            print(Beauty.Fore.RED + "OS not supported jet !" + Beauty.Fore.RESET)

    elif options == "jump" and options2 == "desktop":
        if platform.system() == "Windows":
            os.chdir("c:\\Users\\" + getpass.getuser() + "\\desktop")
        if platform.system() != "Windows":
            print(Beauty.Fore.RED + "OS not supported jet !" + Beauty.Fore.RESET)

    elif options == "jump" and options2 == "videos":
        if platform.system() == "Windows":
            os.chdir("c:\\Users\\" + getpass.getuser() + "\\videos")
        if platform.system() != "Windows":
            print(Beauty.Fore.RED + "OS not supported jet !" + Beauty.Fore.RESET)
    
    else:
        print(Beauty.Fore.YELLOW + "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

def cd_man():
    print(Beauty.Style.DIM +"Command Manual: cd" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("cd .. : - Changes directory to one down")
    print("cd [path] : - Path has to be a folder within the current directory")
    print("cd jump [downloads/documents/desktop/videos : - Directly jumps to the userfolder\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("A basic command to navigate in directories\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("Raises PermissionError when its missing permissions to change the directory")