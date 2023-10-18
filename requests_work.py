import requests
import json

# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# print(type(r))
# print(r.status_code)
# print(r.text)
# branches = r.json()
# print(type(branches))
# for branch in branches:
#     print(branch["name"])
print("200")
out_data = {
    "name": "Samuel Ramirez",
    "net_id": "slr71",
    "e-mail": "lucas.ramirez@duke.edu"
}

in_data = {
    "user": "slr71",
    "message": "Hello"
}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=in_data)
g = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/slr71")
#r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)

print(g.status_code)
print(g.text)
#print(r.status_code)
#print(r.text)


