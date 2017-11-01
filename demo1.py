#!/usr/bin/env python

# Import the necessary modules
from netmiko import ConnectHandler

# Define dictionaries for devices
veos01 = {
    'device_type': 'arista_eos',
    'ip': '127.0.0.1',
    'username': 'admin',
    'password': 'admin',
    'port': 12201,
    'verbose': False
}

veos02 = {
    'device_type': 'arista_eos',
    'ip': '127.0.0.1',
    'username': 'admin',
    'password': 'admin',
    'port': 12202,
    'verbose': False
}

# Create a list of all devices
all_devices = [veos01, veos02]

# Loop over all the devices, retrieve the configuration, and
# write the configuration to a file
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command('show runn')
    formatstr = '{ip}-{port}-{type}.txt'
    filename = formatstr.format(ip=a_device['ip'], port=a_device['port'], type=a_device['device_type'])
    with open(filename,'w') as text_file:
        text_file.write(output)
