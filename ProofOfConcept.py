import os

ip_list = ['192.168.0.1', '8.8.4.4', '1.1.1.1', '4.4.4.4']
i = 0
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        i = i + 1
        print(f"UP {ip} Ping Successful, Host is UP!")
    else:
        print(f"DOWN {ip} Host is DOWN!")
if i == len(ip_list):
    print("All Hosts Active")
else:
    miss = len(ip_list) - i
    print(f"Finished with {miss} host(s) down.")
