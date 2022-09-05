import psutil
from imports import CustomFont as Beauty


defaultValue = "5"

def checkExistence(option:int) -> bool:
    if psutil.Process(option) == True:
        return True
    else:
        return False

def taskkill(option, option2):

    if option is not None and option2 == defaultValue:

        try:
            p = psutil.Process(option)
            p.kill()

        except ValueError:
            print(Beauty.Fore.YELLOW + "Process ID has to be a number"+ Beauty.Fore.RESET)

        except psutil.NoSuchProcess:
            print("PID does not exist")


    #elif option == False and option2 == defaultValue:
        #print("PID does not exist")

    else:
        print("Wrong command usage, please check the man page")

        

