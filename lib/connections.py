import psutil
import socket

from imports import CustomFont as Beauty

defaultValue = "5"

def connections(options: str, options2:str):
    """
    List all connections used by Programms
    """

    if options == "normal" and options2 == defaultValue:
        print("list all established connections from programms")
        lc = psutil.net_connections('inet')
        for c in lc:
            (ip, port) = c.laddr
            if ip == '0.0.0.0' or ip == '::':
                if c.type == socket.SOCK_STREAM and c.status == psutil.CONN_LISTEN:
                    proto_s = 'tcp'
                elif c.type == socket.SOCK_DGRAM:
                    proto_s = 'udp'
                else:
                    continue
                pid_s = str(c.pid) if c.pid else '(unknown)'
                msg = 'PID {} is listening on port {}/{} for all IPs.'
                msg = msg.format(pid_s, port, proto_s)
                print(msg)

    else:
        print(Beauty.Fore.RED + "Too much parameters, please check the man site"+ Beauty.Fore.RESET)

def connections_man():
    print(Beauty.Style.DIM +"Command Manual: connections" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("connections : - Outputs all connections made by programms\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("Connection lister\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")