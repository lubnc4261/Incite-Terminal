from imports import CustomFont as Beauty
defaultValue = "5"

def quitter():
    try:
        print(Beauty.Fore.GREEN + "Quitting ..." + Beauty.Fore.RESET)
        raise SystemExit

    except Exception as Error:
        print(Error)

    finally:
        raise SystemExit


def exit(options: str, options2:str):
    """
    Exiting the Programm
    """
    if options == "normal" and options2 == defaultValue:
        quitter()

    else:
        quitter()

def exit_man():
    print(Beauty.Style.DIM +"Command Manual: exit" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("exit: - Closes the programm\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Command to leave the programm\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("Catches Exceptions but closes in every case")
        