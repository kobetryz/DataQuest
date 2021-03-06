import requests
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

params = {"per_page": 50, "page": 1}
headers = {"Authorization": "token 1a69994d902d905d430f995ee92c67b1db24266d"}

response = requests.get("https://api.github.com/users", headers=headers, params=params)
user = response.json()
pp.pprint(user)