import os
from imports import CustomFont as Beauty

defaultValue = "5"

def ls(options: str, option2: str):
    """
    Lists all files in the directory
    """
    try:

        #extend = options.split(",")

        if options == "normal" and option2 == defaultValue:


            for i in os.listdir():
                if os.path.isdir(i) == True:
                    print(i + "         <dir>")
                else:
                    print(i)
                #print(i)

        elif options == "size" and option2 == defaultValue:
            for i in os.listdir():
                print("File: " + i + " | " +"Size in bytes: "+ str(os.path.getsize(i)))

        elif options == "ext" and type(option2) == str:     #making sure the extension is a string
            arr_txt = [x for x in os.listdir() if x.endswith(option2)]
            if len(arr_txt) == 0:
                print(Beauty.Fore.YELLOW + "0 Files with that extension found" + Beauty.Fore.RESET)
            else:
                print(arr_txt)

        else:
            print(Beauty.Fore.RED + "Wrong command usage, please check the man site"+ Beauty.Fore.RESET)

        

    except PermissionError as permerror:
        print(permerror)

def ls_man():
    print(Beauty.Style.DIM +"Command Manual: ls" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("ls : - Lists all Files and Folders in the directory")
    print("ls [size] : - Returns the size of all files in the directory in Bytes")
    print("ls [ext] <extension> : - Only returns the files with the matching extension\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Delivers an overview over all files of a directory with an user influenced output\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")
