import psutil
from imports import CustomFont as Beauty

defaultValue = "5"
userss = psutil.users()

def users(option1:str, option2:str):
    if option1 == "normal" and option2 == defaultValue:
        print(Beauty.Fore.GREEN + "Users associated with this System: " + Beauty.Fore.GREEN)
        for user in userss:
            username = user.name
            print(username)


    else:
        print(Beauty.Fore.RED+ "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

def users_man():
    print(Beauty.Style.DIM +"Command Manual: users" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("users: - prints existing system users\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("List all existing user accounts\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")