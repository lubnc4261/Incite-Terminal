from datetime import datetime, date
from imports import CustomFont as Beauty

weekNumber = date.today().isocalendar()[1]
defaultValue = "5"

def time(option:str, option2:str):
    if option == "normal" and option2 == defaultValue:

        print("System Time = ", datetime.today().strftime("%c"))
        print(" ")
        print ('Week number:', weekNumber)

    else:
        print("Wrong command usage, please check the man page")

def time_man():
    print(Beauty.Style.DIM +"Command Manual: time" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("time : - Returns the time with the weeknumber of the year\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Delivers time informations\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")
