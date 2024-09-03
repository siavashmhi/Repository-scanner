# you have to run this command ==> terraform output -json | python3 automation.py

from sys import stdin
from json import loads as json_loads
import configparser

json_data = stdin.read()
data = json_loads(json_data)

cp = configparser.ConfigParser()
cp["all"] = {}

for hostname, ip in data["server_ips"]["value"].items():
    cp["all"][f"{hostname} ansible_host"] = f"{ip}"

with open("inventory.ini", 'w') as f:
    cp.write(f)
