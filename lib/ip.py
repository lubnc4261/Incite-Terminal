import socket
from urllib import request
from requests import get
import requests
from imports import CustomFont as Beauty
import psutil

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
if_addrs = psutil.net_if_addrs()
defaultValue = "5"
ippub = get('https://api.ipify.org').text

def ip(options: str, options2 :str):
    """
    Returns the global and local ip
    """
    if options == "normal" and options2 == defaultValue:

        try:

        
            print('Public IP = ', ippub)
        except requests.exceptions.ConnectionError as e:
            print(e)

        finally:
            print("Domain Host Name = ", socket.getfqdn())
            print("Local IP = ", host_ip)

    elif options == "all" and options2 == defaultValue:
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(" ")
                print(f"=== Interface: {interface_name} ===")
                print(" ")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")


    elif options != "normal" or "all" and options2 != defaultValue:
        print(Beauty.Fore.RED+ "Wrong command usage, please check the man page" + Beauty.Fore.RESET)

    else:
        print(Beauty.Fore.RED + "Too much parameters given" + Beauty.Fore.RESET)

def ip_man():
    print(Beauty.Style.DIM +"Command Manual: ip" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("ip : - Returns the local and global ip address")
    print("ip [all] : - Returns all interface informations\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Delivers multiple interface informations\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("Excepts an ip downtime for the global ip API")
