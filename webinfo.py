import requests
import pandas as pd

url = 'https://www.tecnm.mx/json/tecnm_institutos.json'
response = requests.get(url)
data = response.json()

# Let's preview
print(type(data))
print(len(data))
print(data[0])