import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DeviceList:
    def __init__(self):
        headers = ({"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"})
        auth = HTTPBasicAuth('admin','admin')
        devices = requests.get('https://10.10.20.50:8888/restconf/data/tailf-ncs:devices/device?fields=name;address;authgroup;device-type(cli);ssh(host-key-verification)', headers=headers, verify=False, auth=auth)
        self.device_list = []
        self.ned_ids = set()
        for device in json.loads(devices.text)['tailf-ncs:device']:
            clean_device = device
            clean_device['host-key-verification'] = clean_device['ssh']['host-key-verification']
            del clean_device['ssh']
            ned_id = clean_device['device-type']['cli']['ned-id'].split(':')[0]
            self.ned_ids.add(ned_id)
            clean_device['ned-id'] = ned_id
            del clean_device['device-type']
            self.device_list.append(clean_device)
        self.ned_ids = list(self.ned_ids)

    def device_by_ned_id(self, search_ned):
        return_list = list()
        for device in self.device_list:
            if device['ned-id'] == search_ned:
                return_list.append(device)
        return return_list
