import requests
server = "http://127.0.0.1:5000"

out_dict = {"name": "Patient one", "id": 101, "blood_type": "O+"}
r = requests.post(server + "/new_patient", json=out_dict)
print(r.text)
print(r.status_code)

test_data = {"id": 101,
             "test_name": "HDL",
             "test_result": 63}
r = requests.post(server + "/add_test", json=test_data)
print(r.text)
print(r.status_code)

r = requests.get(server + "/get_results/101")
print(r.text)
print(r.status_code)

r = requests.get(server + "/get_full_db")
print(r.text)
print(r.status_code)
