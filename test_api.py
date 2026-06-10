import requests

API_KEY = "372502943e5e63478d3c76b66c17dbd5"

city = "Bengaluru"

url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"

response = requests.get(url)

print(response.json())