#!/usr/bin/env python

# Import the necessary modules
import napalm
import json

# Define dictionaries for devices
veos01 = {
    'hostname': '127.0.0.1',
    'username': 'admin',
    'password': 'admin',
    'optional_args': { 'port': 14431 }
}

veos02 = {
    'hostname': '127.0.0.1',
    'username': 'admin',
    'password': 'admin',
    'optional_args': { 'port': 14432 }
}

# Create a list of all devices
all_devices = [veos01, veos02]

# Loop over all the devices, retrieve the configuration, and
# write the configuration to a file
for a_device in all_devices:
    driver = napalm.get_network_driver('eos')
    device = driver(**a_device)
    device.open()
    output = json.dumps(device.get_config(retrieve=u'running'))
    formatstr = '{ip}-{port}-{type}.json'
    filename = formatstr.format(ip=a_device['hostname'], port=a_device['optional_args']['port'], type='arista_eos')
    with open(filename,'w') as text_file:
        text_file.write(output)
    device.close()
