import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class LoopbackServiceList:
    def __init__(self):
        headers = ({"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"})
        auth = HTTPBasicAuth('admin','admin')
        services = requests.get('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service?fields=name;device;dummy', headers=headers, verify=False, auth=HTTPBasicAuth('admin','admin'))
        self.service_list = json.loads(services.text)['loopback-service:loopback-service']

    def service_by_device(self, search_device):
        return_list = list()
        for service in self.service_list:
            if search_device in service['device']:
                return_list.append(service['name'])
        return return_list
