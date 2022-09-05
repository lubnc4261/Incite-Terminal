import psutil
from imports import CustomFont as Beauty

defaultValue = "5"

def tasklist(options:str, options2:str):
    if options == "normal" and options2 == defaultValue:
        main()
    
    else:
        print("Wrong command usage, please check the man page")


def main():
    def getListOfProcessSortedByMemory():
        listOfProcObjects = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
                listOfProcObjects.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
        return listOfProcObjects
    def main():
        print("*** Iterate over all running process and print process ID & Name ***")
        for proc in psutil.process_iter():
            try:
                processName = proc.name()
                processID = proc.pid
                print(processName , ' ::: ', processID)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        print('*** Create a list of all running processes ***')
        listOfProcessNames = list()
        for proc in psutil.process_iter():
            pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
            listOfProcessNames.append(pInfoDict)
        for elem in listOfProcessNames:
            print(elem)
        print('*** Top 5 process with highest memory usage ***')
        listOfRunningProcess = getListOfProcessSortedByMemory()
        for elem in listOfRunningProcess[:5] :
            print(elem)

    main()

def tasklist_man():
    print(Beauty.Style.DIM +"Command Manual: tasklist" + Beauty.Style.RESET_ALL)
    print("       ")
    print(Beauty.Style.DIM + "Usage:" + Beauty.Style.RESET_ALL)
    print("tasklist : - Returns all running processes with stats\n")
    print(Beauty.Style.DIM + "Description:" + Beauty.Style.RESET_ALL)
    print("List running processes\n")
    print(Beauty.Style.DIM + "Exceptions:" + Beauty.Style.RESET_ALL)
    print("")
