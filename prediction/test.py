import requests

url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"

querystring = {"pnrNumber":"1234567890"}

headers = {
	"X-RapidAPI-Key": "879ed47731msh46609248785db50p155c42jsn98db0d5f30fb",
	"X-RapidAPI-Host": "irctc1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())