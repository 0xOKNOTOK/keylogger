#!/usr/bin/python3
try:
    import subprocess
    import keyboard
    import socket

except ModuleNotFoundError:
    packages = ["keyboard","socket","pynput"]
    for package in packages:
        print("package" + "" + package)
        subprocess.call("pip install " + ' '.join(package), shell=True)
        
    

finally:
    def err_handler():
        exit()
    

    USER_MAC = "" #Currently string could be int.
    USER_HOSTNAME = socket.gethostname()
    USER_IP = socket.gethostbyname(USER_HOSTNAME)
    print(USER_HOSTNAME + '' + USER_IP)
    def get_device_info(interface):#Specific interface required, perhaps scan for multiple if possible.
        #try:
            
        #except:
            #err_handler()
        return interface
