import sys

defaultValue = "5"

def title(option:str, option2:str):
    if option == "normal" and option2 == defaultValue:
        print("Wrong command usage, please check the man page")

    if option != "normal" and option2 == defaultValue:
        title = option
        sys.stdout.write("\x1b]2;"+title+"\x07")

    if option != "normal" and option2 != defaultValue:
        print("Wrong command usage, please check the man page")