from PIL import Image, ImageTk
from tkinter import filedialog
import base64
import requests
import time

filename = filedialog.askopenfilename()
if filename == "":
    exit()

with open(filename, "rb") as image_file:
    b64_bytes = base64.b64encode(image_file.read())
b64_string = str(b64_bytes, encoding='utf-8')

out_json = {"image" : b64_string,
            "net_id": "slr71",
            "id_no": 1}

r = requests.post("http://vcm-21170.vm.duke.edu/add_image", json=out_json)
print(r.status_code)
print(r.text)

time.sleep(5)
r = requests.get("http://vcm-21170.vm.duke.edu/get_image/slr71/1")

image_bytes = base64.b64decode(r.text)
with open("watermark.png", "wb") as out_file:
    out_file.write(image_bytes)