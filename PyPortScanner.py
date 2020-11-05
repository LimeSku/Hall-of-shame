import socket
import time
import subprocess
import sys
import argparse
from datetime import datetime
from colorama import Fore, Back, Style, init

init()
subprocess.call('clear', shell=True)
banner = ( """
_______________.___.   _________                                          
\______   \__  |   |  /   _____/ ____ _____    ____   ____   ___________  
 |     ___//   |   |  \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \ 
 |    |    \____   |  /        \  \___ / __ \|   |  \   |  \  ___/|  | \/ 
 |____|    / ______| /_______  /\___  >____  /___|  /___|  /\___  >__|    
           \/                \/     \/     \/     \/     \/     \/        
						""" + Fore.RED + """
""" + Style.RESET_ALL)
print(banner)
parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Host to scan")
parser.add_argument("-p1", help="Port min")
parser.add_argument("-p2", help="Port max")
args = parser.parse_args()

print(Fore.BLUE)
Ip = args.host
port_min = int(args.p1)
port_max = int(args.p2)
t1 = time.time()




try:
    for port in range(port_min,port_max):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((Ip,port))
        if result == 0:
            print("[*] port {} is open".format(port))
        sock.close()
except socket.gaierror:
    print("Server Unreachable.")
    sys.exit()
except socket.error:
    print("Server Unreachable")
    sys.exit()
except KeyboardInterrupt:
    print("Closing. Bye.")
    sys.exit()
t2 = time.time()
t3 = (t1 - t2)
print("finished in {}.".format(t3))
