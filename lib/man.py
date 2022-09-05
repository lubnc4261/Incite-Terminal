from imports import CustomFont as Beauty
from pathlib import Path

from lib.cat import cat_man
from lib.cd import cd_man
from lib.clear import clear_man
from lib.connections import connections_man
from lib.exit import exit_man
from lib.googlepass import googlepass_man
from lib.hostname import hostname_man
from lib.info import info_man
from lib.cls import cls_man
from lib.ip import ip_man
from lib.ls import ls_man
from lib.show import show_man
from lib.tasklist import tasklist_man
from lib.tree import tree_man
from lib.time import time_man
from lib.mkdir import mkdir_man
from lib.rmdir import rmdir_man
from lib.touch import touch_man
from lib.rmfile import rmfile_man
from lib.users import users_man
from lib.create import create_man
from lib.help import help_man

defaultValue = "5"
commands = ["cat", "cd", "clear", "cls", "create", "connections", "exit", "googlepass", "hostname", "info", "ip", "ls", "show", "tasklist", "tree", "time", "mkdir", "rmdir", "touch", "rmfile", "users", "help"]



def man(options:str, options2:str):
    if options in commands and options2 == defaultValue:
        try:

            eval(options + "_man()")

        except NameError:
            print(Beauty.Fore.YELLOW + "Command doesnt exist" + Beauty.Fore.RESET)

    elif options in commands and options2 != defaultValue:
        print(Beauty.Fore.YELLOW + "Wrong command usage: man [command]"+ Beauty.Fore.RESET)


    elif options not in commands and options2 == defaultValue:

        print("This is the manual of the Terminal here you can look up the usage as well as the description of all commands \nto check the manual for a command use: man [command]")

    elif options not in commands and options2 != defaultValue:
        
        print(Beauty.Fore.YELLOW + "Wrong command usage: man [command]"+ Beauty.Fore.RESET)