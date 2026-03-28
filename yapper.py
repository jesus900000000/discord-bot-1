import requests
import time
import os

payload = {
    'content': str(int(time.time() * 1000))
}


header = {
    'authorization': os.environ["AUTH"]
}


while True:
    r = requests.post('https://discord.com/api/v9/channels/1486199330795688107/messages', data=payload, headers=header)
    time.sleep(2)
    payload = {
        'content': str(int(time.time() * 1000))
    }
    print('running...')
