import getpass
from imports import CustomFont as Beauty

defaultValue = "5"

def hostname(options: str, options2 :str):
    if options == "normal" and options2 == defaultValue:

        print(getpass.getuser())

    else:
        print(Beauty.Fore.RED+ "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

def hostname_man():
    print(Beauty.Style.DIM +"Command Manual: hostname" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("hostname: - prints out the current logged user\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("works like whoami by showing the current logged user\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")
        
