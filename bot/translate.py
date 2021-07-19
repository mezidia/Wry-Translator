import requests

url = "https://nlp-translation.p.rapidapi.com/v1/translate"

querystring = {"text":"Hello, world!!","to":"es","from":"en"}

headers = {'x-rapidapi-host': 'nlp-translation.p.rapidapi.com'}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)