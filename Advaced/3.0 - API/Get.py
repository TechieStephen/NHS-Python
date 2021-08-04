import json
import requests


try:
    api_request = requests.get("https://jsonplaceholder.typicode.com/users")
    global result
    result = json.loads(api_request.content)
except:
    result = 'Error.......'

print(result[0].get("name"))