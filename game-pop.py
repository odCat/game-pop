import requests
import json

r = requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")
print(r)
print(json.loads(r.text)['players'])

