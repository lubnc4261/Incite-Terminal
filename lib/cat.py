from imports import CustomFont as Beauty
from pathlib import Path
import os

defaultValue = "5"


#cwd is path von mainscript nutzen zum prüfen in zeile 26 

def cat(options :str, options2: str):


    if options is not None and options2 == defaultValue:
        if Path(os.getcwd() + "/" + options).is_file():

            try:
                with open(options) as f:
                    lines = f.readlines()
                    print(lines)
                f.close()

            except PermissionError:
                print(Beauty.Fore.RED +"No Permissions to open that file" + Beauty.Fore.RESET)

            except UnicodeDecodeError:
                print(Beauty.Fore.RED +"File has to be a text document"+ Beauty.Fore.RESET)

        else:
            print(Beauty.Fore.RED +"File could not be found"+ Beauty.Fore.RESET)

    else:
        print(Beauty.Fore.RED + "Too much parameters, please check the man site"+ Beauty.Fore.RESET)


def cat_man():
        print(Beauty.Style.DIM +"Command Manual: cat" + Beauty.Style.RESET_ALL)
        print("       ")
        print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
        print("cat [file] : - File has to be typed with the extension ")
        print("             - File has to be in the current directory \n")
        print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
        print("The command is reading all the lines raw and returns them afterwards \n")
        print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
        print("Raises PermissionError on missing permissions to open the file")
        print("Raises UnicodeDecodeError when the file is no in text format")
        

