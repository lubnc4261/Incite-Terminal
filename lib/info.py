from imports import CustomFont as Beauty
import platform
import psutil
from tabulate import tabulate
import GPUtil
import getpass
import platform
import os
import subprocess
import distutils.spawn
import re
import uuid
import shutil


total, used, free = shutil.disk_usage("/")
svmem = psutil.virtual_memory()
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
uname = platform.uname()
currentdir = os.getcwd()
appid = os.getpid()
net_io = psutil.net_io_counters()
disk_io = psutil.disk_io_counters()
gpus = GPUtil.getGPUs()
cpufreq = psutil.cpu_freq()
defaultValue = "5"


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

infos = ["programm", "cpu", "gpu", "io", "os", "python", "mac", "ram", "storage"]

def info(options: str, options2:str):
    if options.lower() not in infos and options2 == defaultValue:
        print(Beauty.Fore.YELLOW + "Info point does not exist" + Beauty.Fore.RESET)

    if options.lower() not in infos and options2 is not defaultValue:
        print(Beauty.Fore.YELLOW + "Wrong command usage, please check man site" + Beauty.Fore.RESET)

    if options.lower() in infos and options2 == defaultValue:
        if options.lower() == "programm" and options2 == defaultValue:

            print("Programm Information")
            print(" ")
            print('Location = ')
            print('__file__ = ')
            print("Version = 2.0")
            print("Creator = lubnc4261")
            print("Published on Github = https://github.com/lubnc4261/Incite-Terminal")
            print("Made in Python 3.9.1 64-bit")

        if options.lower() == "cpu" and options2 == defaultValue:

            print("Cpu Informations")
            print(" ")
            print(f"Processor: {platform.processor()}")
            print("Physical cores:", psutil.cpu_count(logical=False))
            print("Total cores:", psutil.cpu_count(logical=True))
            print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

        if options.lower() == "gpu" and options2 == defaultValue: 

            print("="*40, "GPU Details", "="*40)
            list_gpus = []
            for gpu in gpus:
                gpu_id = gpu.id
                gpu_name = gpu.name
                gpu_load = f"{gpu.load*100}%"
                gpu_free_memory = f"{gpu.memoryFree}MB"
                gpu_used_memory = f"{gpu.memoryUsed}MB"
                gpu_total_memory = f"{gpu.memoryTotal}MB"
                gpu_temperature = f"{gpu.temperature} °C"
                gpu_uuid = gpu.uuid
                list_gpus.append((
                    gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                    gpu_total_memory, gpu_temperature, gpu_uuid
            ))

            print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                        "temperature", "uuid")))

        if options.lower() == "io" and options2 == defaultValue:

            print("Total Data send / recieved since boot")
            print("---------------------------------------------------")
            print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
            print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
            print(" ")
            print("Total Data read / wrote since boot")
            print("---------------------------------------------------")
            print(f"Total read: {get_size(disk_io.read_bytes)}")
            print(f"Total write: {get_size(disk_io.write_bytes)}")

        if options.lower() == "os" and options2 == defaultValue:
            print("System Informations")
            print(" ")
            print("User Account Name: ", getpass.getuser())
            print("Current Directory: ", currentdir)
            print("Process ID: ", appid)
            print(f"System: {uname.system}")
            print(f"Node Name: {uname.node}")
            print(f"Release: {uname.release}")
            print(f"Version: {uname.version}")
            print(f"Machine: {uname.machine}")
            print(f"Processor: {uname.processor}")
            if platform.system() == 'Windows':
             print("UUID ID: ",current_machine_id)
            if platform.system() != 'Windows':
                print(" ")

        if options.lower() == "python" and options2 == defaultValue:
            if distutils.spawn.find_executable("python.exe"):
                a = distutils.spawn.find_executable("python.exe")
                print(a)

                print ('Version      :', platform.python_version())
                print ('Version tuple:', platform.python_version_tuple())
                print ('Compiler     :', platform.python_compiler())
                print ('Build        :', platform.python_build())

            else:
                print(Beauty.Fore.YELLOW + "Python can not get located" + Beauty.Fore.RESET)

        if options.lower() == "mac" and options2 == defaultValue:
            print ("MAC Adress : ", end="")
            print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

        if options.lower() == "ram" and options2 == defaultValue:
            print("Random Application Memory Informations")
            print(" ")
            print(f"Total: {get_size(svmem.total)}")
            print(f"Available: {get_size(svmem.available)}")
            print(f"Used: {get_size(svmem.used)}")
            print(f"Percentage: {svmem.percent}%")

        if options.lower() == "storage" and options2 == defaultValue:
            print("Main Storage / OS Installation")
            print(" ")
            print("Total: %d GiB" % (total // (2**30)))
            print("Used: %d GiB" % (used // (2**30)))
            print("Free: %d GiB" % (free // (2**30)))

def info_man():
    print(Beauty.Style.DIM +"Command Manual: hostname" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("hostname [ram/mac/storage/io/os/cpu/gpu/python/programm] : - Delivers informations\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Prints out the informations for the provided subcategory. If gpu returns nothing then there is no external gpu used\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")
