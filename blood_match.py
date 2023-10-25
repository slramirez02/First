import requests
import json

r = requests.get("http://vcm-33934.vm.duke.edu:5002/get_patients/slr71")
print(r.status_code)

p1 = requests.get("http://vcm-33934.vm.duke.edu:5002/get_blood_type/F4")
print(p1.status_code)
print(p1.text)

p2 = requests.get("http://vcm-33934.vm.duke.edu:5002/get_blood_type/M4")
print(p2.status_code)
print(p2.text)

in_data = {"Name": "slr71", "Match": "No"}

res = requests.post("http://vcm-33934.vm.duke.edu:5002/match_check", json = in_data)
print(res.status_code)
print(res.text)