import json
import ssl
import sys
from urllib.request import urlopen

myssl = ssl.create_default_context()
myssl.check_hostname = False
myssl.verify_mode = ssl.CERT_NONE

state = json.load(
  urlopen('<CIRCLE_URL>', context=myssl)
)

devices = {p['uid']: p for p in state['devices']}

all_devices = []

for u in state['users']:
    if u['relatedDevices']:
        for device in u['relatedDevices']:
            all_devices.append({
                'name': u['name'],
                **devices[device['uid']]
            })

json.dump(all_devices, sys.stdout, indent=2)
