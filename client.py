import requests

r = requests.get("http://127.0.0.1:5000/")
print(r.status_code)
print(r.text)

out_data = {"name": "Ann Ables",
            "test_value": 130}
r = requests.post("http://127.0.0.1:5000/hdl_check",
                  json = out_data)
print(r.status_code)
print(r.text)

route = "http://127.0.0.1:5000/add/2/3"
r = requests.get(route)
print(r.status_code)
print(r.text)
