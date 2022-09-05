import platform
import os

from imports import CustomFont as Beauty

defaultValue = "5"

def cls(options: str, options2:str):
    """
    Using the System integrated function to clear the Terminal
    """

    if options == "normal" and options2 == defaultValue:

        try:
            if platform.system() == "Windows":
                os.system("cls")
            if platform.system() == "Linux":
                os.system("clear")
            if platform.system() == "Darwin":
                os.system("clear")
        except Exception as error:
            print("Clear not possible: "+str(error))

    else:
        print(Beauty.Fore.RED + "Too much parameters, please check the man site"+ Beauty.Fore.RESET)

def cls_man():
    print(Beauty.Style.DIM +"Command Manual: clear / cls" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("clear : - Clears the whole terminal window")
    print("cls: - Clears the whole terminal window\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Super simple terminal clearer\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")