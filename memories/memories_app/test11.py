import requests
from datetime import date
today = date.today()

url = 'https://hooks.zapier.com/hooks/catch/3139720/oiudlwg'
myobj = {'email': 'test4@example.com', 'date':today}

x = requests.post(url, data = myobj)

# print(x.text)