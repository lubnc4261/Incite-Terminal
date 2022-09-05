#imports used in this file
import os
import platform
import sys
import getpass
from pathlib import Path



#importing modules from the imports folder
from imports import CustomFont as Beauty

from lib.help import help

# import commands | handling them as custom external modules at the moment
from lib.info import info
from lib.time import time
from lib.ip import ip
from lib.tasklist import tasklist
from lib.clear import clear
from lib.connections import connections
from lib.googlepass import googlepass
from lib.ls import ls
from lib.cls import cls
from lib.exit import exit
from lib.hostname import hostname
from lib.taskkill import taskkill
from lib.title import title
from lib.tree import tree
from lib.cat import cat
from lib.show import show
from lib.cd import cd
from lib.man import man
from lib.mkdir import mkdir
from lib.rmdir import rmdir
from lib.touch import touch
from lib.rmfile import rmfile
from lib.users import users
from lib.create import create

# change terminal name

sys.stdout.write("\x1b]2;Incite Terminal v 2.0\x07")

#checking if incite is run as admin

from lib.adminchecker import is_process_user_an_admin



aktuell = os.getcwd()
datei = __file__
normal = "normal"

defaultValue = "5" #set empty parameter as None will raise a error, init own defaultValue 



def indexExists(list,index) -> bool:
    """
    New function to check for an exception to 
    bypass problems in the mainfunction
    """
    try:
        list[index]
        return True
    except IndexError:
        return False

def commandRunner(command):
    a = command.split(" ") #splitting user input into the parameters
    if Path(aktuell+"/lib/"+a[0]+".py").is_file():
        #try:
        #if a[0] and a[1] != None:
        if indexExists(a, 0) == True and indexExists(a, 1) == True and indexExists(a, 2) == False:
            #ls size
            #eval(a[0]+"(\""+a[1]+","+defaultValue+"\")")
            eval(a[0])(a[1], defaultValue)

        #except IndexError:

        #if a[0] != None and a[1] is None:
        #else:
        elif indexExists(a, 0) == True and indexExists(a, 1) == False and indexExists(a, 2) == False:

            #eval(a[0]+"(\""+normal+","+defaultValue+"\")")
            # ls
            eval(a[0])("normal", defaultValue)

        elif indexExists(a, 0) == True and indexExists(a, 1) == True and indexExists(a, 2) == True:
            #eval(a[0]+"(\""+a[1]+","+a[2]+"\")") 
            eval(a[0])(a[1], a[2])

    else:
        res = a[0].lower()
        if res == "help":
            eval("help()")
        else:

            
            print(Beauty.Fore.RED + "Unknown command" + Beauty.Fore.RESET)

        
    commandinput()
    




def main():

    # When i run the programm in default console the colours are color codes and not in color

    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Linux":
        os.system("clear")
    if platform.system() == "Darwin":
        os.system("clear")

    # but after a call of "clear" it all works again :-)

    print(Beauty.Fore.MAGENTA +"_________ _        _______ __________________ _______  "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"\__   __/( (    /|(  ____ \\__   __/\__   __/(  ____ \ "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"   ) (   |  \  ( || (    \/   ) (      ) (   | (    \/ "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"   | |   |   \ | || |         | |      | |   | (__     "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"   | |   | (\ \) || |         | |      | |   |  __)    "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"   | |   | | \   || |         | |      | |   | (       "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"___) (___| )  \  || (____/\___) (___   | |   | (____/\ "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"\_______/|/    )_)(_______/\_______/   )_(   (_______/ "+ Beauty.Fore.RESET)
    print(Beauty.Fore.MAGENTA +"                                                       "+ Beauty.Fore.RESET)
    if platform.system() == "Windows":
        print(Beauty.Fore.YELLOW +"OS : Windows"+ Beauty.Fore.RESET)
    if platform.system() == "Darwin":
        print(Beauty.Fore.YELLOW +"OS : Mac"+ Beauty.Fore.RESET)
    if platform.system() == "Linux":
        print(Beauty.Fore.YELLOW +"OS : Linux"+ Beauty.Fore.RESET)
    if platform.system() == "Java":
        print(Beauty.Fore.YELLOW +"OS : Java"+ Beauty.Fore.RESET)
    print(" ")
    print(" ")
    print("Python based Command Prompt" + Beauty.Fore.CYAN + " [Version 2.0]" + Beauty.Fore.RESET)
    print("Created by lubnc4261")
    print("---------------------------------------------------")
    print(Beauty.Fore.BLUE + "File: " + __file__ + Beauty.Fore.RESET)
    print("---------------------------------------------------")
    if is_process_user_an_admin(os.getpid()) == True:
        print(Beauty.Fore.GREEN + "Programm has administrator permissions" + Beauty.Fore.RESET)
    if is_process_user_an_admin(os.getpid()) == False:
        print(Beauty.Fore.YELLOW + "Programm has no administrator permissions - some features might not work" + Beauty.Fore.RESET)
    print(" ")
    commandinput()


def commandinput():
    try:

        command = input(Beauty.Fore.MAGENTA + "\n" +  getpass.getuser() + " " + os.getcwd() + " "  r"$ " " " + Beauty.Fore.RESET)
        commandRunner(command)

    except KeyboardInterrupt:
        print(Beauty.Fore.GREEN + "Quitting ..." + Beauty.Fore.RESET)
        raise SystemExit

            

if __name__ == "__main__":
    main()





