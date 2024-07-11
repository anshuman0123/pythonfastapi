import requests

url = "https://realstonks.p.rapidapi.com/stocks/NSEI/advanced"

headers = {
	"x-rapidapi-key": "436f0d612dmsh48462212ca9933ep16a5f9jsnd71d154e3d10",
	"x-rapidapi-host": "realstonks.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response)