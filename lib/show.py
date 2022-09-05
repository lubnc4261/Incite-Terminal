import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from imports import CustomFont as Beauty
from pathlib import Path
import os

defaultValue = "5"

imageError = "cannot identify image file"

def show(path, options2:str):

    if path is not None and options2 == defaultValue:

        if Path(os.getcwd() + "/"+ path).is_file():
            try:

                #image_window = tk.Tk()
                #image_window.title(path)
                #img = ImageTk.PhotoImage(Image.open(path))
                #panel = tk.Label(image_window, image=img)
                #panel.pack(side="bottom", fill="both", expand="yes")
                #image_window.mainloop()

                root = tk.Tk()

                root.title("Displaying " + path)

                tabcontroll = ttk.Notebook(root)

                tab1 = ttk.Frame(tabcontroll)
                tab2 = ttk.Frame(tabcontroll)

                tabcontroll.add(tab1, text="Image")
                tabcontroll.add(tab2, text="Info")

                tabcontroll.pack(expand=1, fill="both")

                img = ImageTk.PhotoImage(Image.open(path))
                panel = ttk.Label(tab1, image=img)
                panel.pack(side="bottom", fill="both", expand="yes")


                root.mainloop()



            except PermissionError:
                print(Beauty.Fore.RED + "Missing Permissions to open the image" + Beauty.Fore.RESET)

            # Checking if the error contains the words for a PIL.UnidentifiedImageError (imageError string) since i dont know how to except it

            except Exception as e:
                if imageError in str(e):
                    print(Beauty.Fore.YELLOW + "This file is not a image" + Beauty.Fore.RESET)
                    root.destroy() # removing the empty tkinter window


        else:
            print(Beauty.Fore.RED + "File not found" + Beauty.Fore.RESET)

    elif path is None and options2 is defaultValue or not defaultValue:
        print(Beauty.Fore.RED + "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

    else:
        print(Beauty.Fore.YELLOW + "Too much parameters given" + Beauty.Fore.YELLOW)
    
def show_man():
    print(Beauty.Style.DIM +"Command Manual: show" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("ls <path>.<extension> : - Opens the image in a seperate window\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Image Viewer\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("Raises PermissionError on missing permissions to open the file")
    print("Raises an Exception when the file is not an image")
    print("")

