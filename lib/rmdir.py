import os
from imports import CustomFont  as Beauty

defaultValue = "5"

def rmdir(option1:str, option2:str):
    if option1 is not None and option2 == defaultValue:
        try:
            if option1 == "normal":
                print(Beauty.Fore.YELLOW + "Missing folder name" + Beauty.Fore.RESET)
            else:

                os.rmdir(option1)
                if os.path.isdir(option1) == False:
                    print(Beauty.Fore.GREEN + "Operation completed successfully" + Beauty.Fore.RESET)
                else:
                    print(Beauty.Fore.YELLOW + "An error occured" + Beauty.Fore.RESET)
        
        except PermissionError:
            print(Beauty.Fore.RED + "Missing permissions to delete a folder" + Beauty.Fore.RESET)

        except OSError:
            print(Beauty.Fore.YELLOW + "OS restriction, action stopped")

    if option1 is None and option2 == defaultValue:
        print(Beauty.Fore.YELLOW + "Missing folder name" + Beauty.Fore.RESET)

    if option1 is None and option2 != defaultValue:
        print(Beauty.Fore.YELLOW + "Missing folder name" + Beauty.Fore.RESET)

    if option1 is None and option2 is None:
        print(Beauty.Fore.YELLOW + "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

def rmdir_man():
    print(Beauty.Style.DIM +"Command Manual: rmdir" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("rmdir <name> : - Deletes a folder\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Folder deletion command\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("Raises PermissionError permissions are missing")
    print("Raises OSError when there is a OS related error")

