import os
import time
import logging

ip_list = ['192.168.0.1', '8.8.4.4', '4.4.4.4', '1.1.1.1', '1.2.3.4']
i = 0
logging.basicConfig(format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M",)
print("Started logging:")

for ip in ip_list:
    response = os.popen(f"ping -n 1 -w 50 {ip}").read()
    if "Received = 1" in response:
        i = i + 1
        print(f"UP {ip} Ping Successful, Host is UP!")
    elif "Request timed out." in response:
        print(f"TIMED OUT {ip} Host Response was Timed Out, Retrying")
        response = os.popen(f"ping -n 1 {ip}").read()
        if "Received = 1" in response:
            i = i + 1
            print(f"UP {ip} Ping Successful, Host is UP!")
        elif "Request timed out." in response:
            logging.error(f"TIMED OUT {ip} Host is DOWN!")
print("=======================================================================")
if i == len(ip_list):
    print("All Hosts Active")
else:
    miss = len(ip_list) - i
    length = len(ip_list)
    print(f"Finished with {miss} out of {length} host(s) down.")
