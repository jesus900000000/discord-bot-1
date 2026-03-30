import requests
import time
import os

#Variables:
url = 'https://discord.com/api/v9/channels/1486199330795688107/messages'

payload = {
    'content': str(int(time.time() * 1000))
}


header = {
    'authorization': os.environ["AUTH"]
}


while True:
    try:
        r = requests.post(url, data=payload, headers=header,timeout=10)
        print("Sent:",r.status_code)
        payload = {
        'content': str(int(time.time() * 1000))
        }
    except requests.exceptions.RequestException as e:
        print("Network error", e)
        time.sleep(5)
        continue
    time.sleep(2)