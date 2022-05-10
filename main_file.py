from device_list import DeviceList
from loopservice_list import LoopbackServiceList
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# creates a loopback using the loopback service created in lab
def create_loopback(name, device, dummy):
    body = '{{"loopback-service:loopback-service":[{{"name": "{name}","device": "{device}","dummy": "{dummy}"}}]}}'.format(name=name, device=device, dummy=dummy)
    headers = ({"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"})
    auth = HTTPBasicAuth('admin','admin')
    services = requests.patch('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service', headers=headers, verify=False, auth=HTTPBasicAuth('admin','admin'), data=body)


# deletes the loopback service based on it's name
def delete_loopback(name):
    headers = ({"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"})
    auth = HTTPBasicAuth('admin','admin')
    services = requests.delete('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service={0}'.format(name), headers=headers, verify=False, auth=HTTPBasicAuth('admin','admin'))



if __name__ == "__main__":
    print("What would you like to do?")
    choice = ''
    while choice != "4":
        loopbackservices = LoopbackServiceList()
        devices = DeviceList()
        choice = input("1.Remove Loopback(s)\n2.Add Loopback(s)\n3.View Loopback(s)\n4.Exit\n[1,2,3,4]:")
        if choice == "1":
            next_choice = input("1.Remove All Loopback(s)\n2.Remove Based on Name\n3.Remove Based on Device\n4.Exit\n[1,2,3,4]:")
            if next_choice == "1":
                #remove all loopbacks
                print('removing all loopbacks')
                for service in loopbackservices.service_list:
                    delete_loopback(service['name'])
            elif next_choice == "2":
                for index, service in enumerate(loopbackservices.service_list):
                    print('{0}: {1}'.format(index, service['name']))
                index  = int(input("Which Service?[index]: "))
                loopback_name = loopbackservices.service_list[index]['name']
                print('removing loopback {0}'.format(loopback_name))
                delete_loopback(loopback_name)
            elif next_choice == "3":
                for index, device in enumerate(devices.device_list):
                    print("{0}: {1}".format(index, device['name']))
                index = int(input("Which Device?[index]: "))
                device_name = devices.device_list[index]['name']
                print('removing loopbacks on {0}'.format(device_name))
                for service_name in loopbackservices.service_by_device(device_name):
                    delete_loopback(service_name)
        elif choice == "2":
            next_choice = input("1.Add One Loopback(s)\n2.Add Based on NED\n3.Exit\n[1,2,3]:")
            if next_choice == "1":
                print("which device?")
                for index, device in enumerate(devices.device_list):
                    print("{0}: {1}".format(index, device['name']))
                index = int(input("Which Device?[index]: "))
                name = input("Name: ")
                dummy = input("Dummy: ")
                print("Creating Loopback for {0}".format(devices.device_list[index]['name']))
                create_loopback(name, devices.device_list[index]['name'], dummy) 
            elif next_choice == "2":
                print("which NED?")
                for index, ned_id in enumerate(devices.ned_ids):
                    print("{0}: {1}".format(index, ned_id))
                index = int(input(""))
                for device in devices.device_by_ned_id(devices.ned_ids[index]):
                    print('Device {0}'.format(device['name']))
                    name = input("Name: ")
                    dummy = input("Dummy: ")
                    print("Creating Loopback for {0}".format(device['name']))
                    create_loopback(name, device['name'], dummy)
        elif choice == "3":
             pprint(loopbackservices.service_list)

