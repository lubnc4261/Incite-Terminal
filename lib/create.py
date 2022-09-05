from imports import CustomFont as Beauty
defaultValue = "5"

try:
    import platform
    import sys
    import os
    import getpass
    import psutil
    import GPUtil
    import datetime
    import subprocess
    import socket
    import shutil
    import re
    import uuid
    import wmi


    from urllib.request import urlopen
    from requests import get
    from datetime import datetime, timezone, timedelta, date
    from os import system, name
    from tabulate import tabulate

except ModuleNotFoundError as moduleError:
    print(moduleError)
    input

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def main():

    # start

    n = datetime.now()
    f = open("SysInfo-Output.txt", "a")
    f.write("Informations from  : %s \n" %n )
    f.write(60*"*"+ "\n")
    f.write("    \n")

    # User Account Name

    uname = platform.uname()

    a = getpass.getuser()

    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

    disk_io = psutil.disk_io_counters()

    net_io = psutil.net_io_counters()

    cpufreq = psutil.cpu_freq()

    svmem = psutil.virtual_memory()

    c = wmi.WMI()    

    my_system = c.Win32_ComputerSystem()[0]

    f.write("------------------------")
    f.write("OS Informations")
    f.write("------------------------" + "\n")

    f.write("  \n")

    f.write("User Account Name: %a \n" %a)

    # System

    f.write(f"System: {uname.system}\n")

    f.write(platform.win32_edition())
    f.write("\n")

    # Node Name

    f.write(f"Node Name: {uname.node}\n")

    # OS Release

    f.write(f"Release: {uname.release}\n")

    # Version

    f.write(f"Version: {uname.version}\n")

    # Machine

    f.write(f"Machine: {uname.machine}\n")

    # SystemType

    f.write(f"SystemType: {my_system.SystemType}\n")

    # Manufacturer

    f.write(f"Manufacturer: {my_system.Manufacturer}\n")


    if platform.system() == "Windows":
        f.write("UUID ID: " + current_machine_id + "\n")

    f.write(" \n")


    f.write("------------------------")
    f.write("CPU Informations")
    f.write("------------------------"+"\n")

    f.write(" \n")

    # Processor

    f.write(f"Processor: {uname.processor}\n")

    # Cores

    #f.write(f"Physical Cores: " , psutil.cpu_count(logical=False) + "  \n")
    # Max Frequenzy

    f.write(f"Max Frequency: {cpufreq.max:.2f}Mhz\n")

    # Mix Frequency

    f.write(f"Min Frequency: {cpufreq.min:.2f}Mhz\n")

    # Current Frequency

    f.write(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")

    f.write(" \n")

    f.write("------------------------")
    f.write("IO Informations")
    f.write("------------------------\n")

    f.write(" \n")

    # Recieved / Send

    f.write(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
    f.write(f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n")

    f.write(" \n")

    # Read / Write

    f.write(f"Total read: {get_size(disk_io.read_bytes)}\n")
    f.write(f"Total write: {get_size(disk_io.write_bytes)}\n")

    f.write(" \n")

    f.write("------------------------")
    f.write("RAM Informations")
    f.write("------------------------" + "\n")

    f.write(" \n")

    # Total Size

    f.write(f"Total: {get_size(svmem.total)}\n")

    # Available

    f.write(f"Available: {get_size(svmem.available)}\n")

    # Used

    f.write(f"Used: {get_size(svmem.used)}\n")

    f.write(f"Percentage: {svmem.percent}%\n")

    f.write(" \n")

    f.write(" \n")

    f.write("------------------------")
    f.write("IP Informations")
    f.write("------------------------" + "\n")

    host_name = socket.gethostname()

    host_ip = socket.gethostbyname(host_name)

    ip = get('https://api.ipify.org').text

    f.write(" \n")
    
    # Domain Name

    f.write("Domain Host Name = " + socket.getfqdn() + " \n")

    # Local IP

    f.write("Local IP = " + host_ip + " \n")

    # Public IP

    f.write('Public IP = ' + ip + " \n")

    f.write("  \n")

    f.write("------------------------")
    f.write("MAC Informations")
    f.write("------------------------" + "\n")

    f.write(" \n")

    f.write("MAC Adress : ")
    f.write(':'.join(re.findall('..', '%012x' % uuid.getnode())))

    f.write(" \n")
    f.write("  \n")

    f.write("------------------------")
    f.write("GPU Informations")
    f.write("------------------------" + "\n")

    f.write(" \n")


    list_gpus = []
    gpus = GPUtil.getGPUs()
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

    f.write(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                    "temperature", "uuid")))

    f.write(" \n")
    f.write("  \n")
    f.close()


def create(options1, options2):
    if options1 == "sysinfo" and options2 == defaultValue:
        main()

    else:
        print(Beauty.Fore.YELLOW + "Wrong command usage, please check the man page" + Beauty.Fore.RESET)


if __name__ == "__main__":
    main()

def create_man():
    print(Beauty.Style.DIM +"Command Manual: create" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("create [sysinfo]: - Create a .txt with system informations\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Get system informations\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("Integrated GPU won't be listed ")
        