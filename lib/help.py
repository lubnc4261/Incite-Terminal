from imports import CustomFont as Beauty

defaultValue = "5"



def help(option1, option2):
    if option1 is not None and option2 == defaultValue:
        print(Beauty.Fore.CYAN +"""

        ------------------------------------------------------
        For more informations on a command use the man command
        ------------------------------------------------------

        """+ Beauty.Fore.RESET)

        print("""

        cat [file]                                  - Open a textformat file
        cd [path] / [jump] <basedirectory>          - Changes the directory incite works in
        clear / cls                                 - Clears the terminal window
        connections                                 - List all connections established by programms
        create [sysinfo]                            - System Informations file
        exit                                        - Close the program 
        googlepass                                  - Get saved Google Chrome passwords
        hostname                                    - Returns the current logged in user
        info [programm, cpu, gpu. io. os, python    - Informations of a argument
        mac, ram, storage]
        ip                                          - Get interface informations
        ls / [size] / [ext]                         - List contents of the diretory
        man                                         - Manual command for each command
        mkdir [name]                                - Create a folder
        rmdir [name]                                - Remove a folder
        rmfile [name]                               - Remove a file
        show [image]                                - Opens a image
        taskkill [PID]                              - Kill a task
        tasklist                                    - Returns all running tasks
        time                                        - Returns time related informations
        title                                       - Change the incite window name
        touch [name]                                - Create a empty file
        tree                                        - Tree like directory visualisation
        users                                       - Returns all accounts on the pc
        

        """)
    else:
        print(Beauty.Fore.RED + "Wrong command usage, type help" + Beauty.Fore.RESET)

def help_man():
    print("Use help to list all available commands")