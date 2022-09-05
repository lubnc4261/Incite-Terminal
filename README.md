# Incite Terminal - [@lubnc4261](https://www.github.com/lubnc4261)



**What is it ?**

Incite Terminal is a python only Command Line Terminal that is made for Windows which supports the most known Commands from the Windows
Terminal and the Unix Terminal in Linux, as well as some other commands I made up by myself.

![showcase](https://github.com/lubnc4261/Incite-Terminal/blob/main/images/showcase.png)

## Dependencies

I created my own small module called CustomFont for this project, so I can keep it free of useless third party modules. It is used
for the color in the terminal
All Dependencies are in <file>
## Path of developement

In this section will I talk about the progress of my program after the time.

### The Beginning

In the early times of the project I didn't really had an idea on what I was doing, since YouTube didn't offered any advanced tutorials 
for
this subject, so the first program was just written in a single file that checked within if conditions what command should be run. 
We can all agree on that this way of checking the user's input and then decide on what to do can only be temporary.
After some time and motivation since I stopped
working on it, I decided to rewrite the whole program that as we know was just a single file with about 1000 lines![1000 lines](https://github.com/lubnc4261/Incite-Terminal/blob/main/images/incite%20old%20lines.png).
I began to think about how I could make the program more advanced and not just letting it stay in the current form. 

### Rewrite

After some brainstorming, the Terminal from Linux came to my mind, where the commands are stored in their own location in the
/urs/bin folder. I decided to also store my commands like that in a folder, but mine is called lib. The only problem at this point
was: **How do i use methods from other files that can have multiple or no parameters ?**. After some research and testings I found
a way that works just fine.

### How does it work ?

We have the launch script that is called incite.py, this script imports all the methods existing from the lib folder that have been
Manually added by calling 
```python
from lib.info import info 
```

this will go to the lib folder and the file  info and then import the method info, note that i coded it that the file and the method
have to be called the same. After all these import lines have been called, the script starts with the **main()** method. This method
will draw the "welcoming screen" of the program and then the method **commandinput()**. At this point, the user can enter the command
he wishes to use. Let's use the show command as an example. The user sends the input show, which will be passed to the **commandRunner(command)**
method. The most important part here is the splitting of the user input at spaces so that we can work with them later in the show method. Now 
it will check if the command is even existing by checking if there is a file with the same name as the command in the lib folder.
After this is completed, and we can go on since show is a valid command it will be checked how much parameters are given so that
we know which one we have to pass and which not to the show method. Assuming that the user input is **show dog.png** it will call the eval function, 
which will run anything within it's parameter brackets as long as it's valid. Since we imported the show command in the first couple
of lines in the incite.py script this is not a problem and will pass the parameters dog.png and the defaultValue parameter which has the
meaning of a placeholder and will be handled as if it is nothing like null, but has to be given to prevent any errors. The next stop
is at the /lib/show.py file, which now works with the parameters it got from the user. Assuming that dog.png is a valid file that exists
in the current working directory of the incite.py script, it will open the image in a new tkinter window.

## Manual 

What would a Terminal be when the user can't check the syntax of each command or just look up what it does before running it. Therefore I 
thought about how to implement a Manual for each command. Since I got the idea of the lib folder from the Linux Terminal, why not also 
stea.. *cought* getting inspired by the Man command which it uses. Like in the Beginning of the Incite Terminal, I wrote a method for
each command that stored a small manual in it in a big file called man.py, but didn't I learn from the past ? Of course, I did, so I
quickly thought of a better idea and came to the conclusion that each command file stores it's own method for the manual. It is pretty 
straight forwarded, just make a method called for, e.g. **show_man()** that will print all its information to the screen. **But how do I 
call these methods when I need them ?**. I used the same principle as in incite.py. I created a man.py file in lib that will eval other methods
by itself by using the parameter **command name**. Since all the man functions in each script is using the <command>_man() syntax 
the eval function is pretty simple:
```python
eval(show_man()) generally
or
eval(command + "_man()") in the man.py
```

## Commands

Command | Description | Info | Example |
----------|-------------|-----|--
`cat [file]` | Adds the content to the Terminal | Has to be a textfile | cat text.txt
`cd ..`  | Changed the working directory | Goes one folder down | cd ..
`cd jump downloads/documents/desktop/videos` | Directly jump to a directory | Windows only | cd jump videos
`clear / cls` | Clear the Terminal | Also removes the "welcoming" | clear
`connections` | List all connections established by programms | Also local ones | connections
`create <sysinfo>` | Save all system informatios in a .txt | Create command made to be expanded | create sysinfo
`exit` | Close the program | - | exit
`googlepass` | List all chrome saved passwords | Can be blank if not **saved** on the machine but saved | googlepass
`hostname` | Returns the current logged-in user | Same as whoami | hostname
`help` | Returns command list | Same as this | help
`info [programm, cpu, gpu. io. os, python, ram, storage]` | Information about <> | Easily to expanded | info cpu
`ip` | List Local and Public Ip Adress | - | Ip
`ls <size/ext>` | List contents of the directory | ls can be used with no parameter | ls ext .py
`man` | Manual Command | - | man cat
`mkdir [name]` | Create a folder | - | mkdir folder
`rmdir [name]` | Remove a folder | - | rmdir folder
`rmfile [name]` | Remove a file | - | rmfile text.txt
`show [image]` | Opens an image | Needs extension | show dog.png
`taskkill [PID]` | Kill a task | Use tasklist to find PID | taskkill 1234
`tasklist` | List all running tasks with PID | - | tasklist
`time` | Returns time related information | - | time
`title` | Rename the Terminal Window | - | title Python 
`touch [name]` | Create an empty textfile | - | touch test.txt 
`tree` | Tree visualisation of the directory | - | tree
`users` | Returns all accounts on the pc | - | users
