import requests
import json

request = requests.post("http://127.0.0.1:8080/getmessages", json={
    "sender": "vdfink",
    "receiver": "vdfink"
}, verify=False)

print(request.json())