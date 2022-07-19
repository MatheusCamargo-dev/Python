import requests
import time
while True:
    payload = {
        'content': ""
    }
    header = {
        'authorization': ''
    }
    r = requests.post("", 
    data=payload, headers=header)
    time.sleep(30)