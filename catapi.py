import requests
response = requests.get("https://api.thecatapi.com")
print(response.text)