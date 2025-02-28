import os
import time
import logging

ip_list = ['10.35.38.2', '10.35.38.1', '10.35.38.10', '10.35.38.11', '10.35.38.4']
i = 0

logging.basicConfig(format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M",)

print("Started logging:")

name_list = ['RoboRio', 'Radio', 'Upper Coprocessor', 'Lower Coprocessor', 'FMS']
devip_dict = dict(zip(ip_list, name_list))

for ip in ip_list:

    response = os.popen(f"ping -n 1 -w 50 {ip}").read()
    if "Received = 1" in response:
        i = i + 1
        print(f"UP {ip} Ping Successful, {devip_dict[ip]} is UP!")

    elif "Destination net unreachable." in response:
        logging.warning(f"TIMED OUT {ip} {devip_dict[ip]} Response was Timed Out, Retrying")
        response = os.popen(f"ping -n 1 {ip}").read()

        if "Received = 1" in response:
            i = i + 1
            print(f"UP {ip} Ping Successful, {devip_dict[ip]} is UP!")

        elif "Destination net unreachable." in response:
            logging.error(f"TIMED OUT {ip}, {devip_dict[ip]} is DOWN!")

print("=======================================================================")

if i == len(ip_list):
    print("All Hosts Active")

else:
    miss = len(ip_list) - i
    length = len(ip_list)
    print(f"Finished with {miss} out of {length} host(s) down.")