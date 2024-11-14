import requests

url = "https://api.scrapingdog.com/linkedin/?api_key={PASSKEY}&url=&dynamic=false&type=profile&linkId=eileenkaur"

response = requests.get(url)

print(response.status_code)

print(response.json())