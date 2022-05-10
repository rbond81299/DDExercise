# Loopback Service REST API

If NSO ip is 10.10.20.50 and SSL is enabled in the webui for port 8888 these files work

It let's a user add loopback services, once the learning lab has been completed on an NSO
https://developer.cisco.com/learning/lab/learn-nso-the-easy-way/step/1

## Virutal Env
The required dependencies:
Python3
python packages:
pprint
requests
json
urllib3

to set up the same enviroment
```console
#create venv
python3 -m venv venv

#start the venv
soruce venv/bin/activate

#install dependencies
pip install pprint
pip install json

#run the file
python main_file.py
```
## loopserivce_list.py
Contains a LoopbackServiceList class
When a LoopbackServiceList is created it gets all the current loopback services on the NSO
it has the function service_by_device which takes a device name and returns a list of services for that device

## device_list.py
Contains a DeviceList class
When a DeviceList is created it gets all the current devices along with their:
  host-key-verification
  ned-id
  device-type
  address
  authgroup
It has the function device_by_ned_id which takes a ned-id and returns only the devices that have the ned-id

## main_file.py
contains two functions and a main
create_loopback(name, device, dummy) creates a loopback using the template from step 9 in the lab
delete_loopback(name) deleted a loopback searching for it by name

The main of this file will ask the user what they want to do
1. Remove Loopbacks
  remove all
  remove based on loopback name
  remove based on device name
2. Add Loopbacks
  one new loopback
  based on ned
3. View Loopbacks
  displays a list of all the current loopbacks


