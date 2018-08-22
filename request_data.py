import requests
import json

URL = 'http://127.0.0.1:8000/api/{ISBN}'
ISBN = '0062380877'

response = requests.get(URL.format(ISBN=ISBN))
json_res = response.json()

print(json.dumps(json_res, indent=4))
print(json_res['title'])
print(json_res['author'])
print(json_res['year'])
print(json_res['isbn'])
