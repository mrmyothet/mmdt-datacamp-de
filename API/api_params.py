import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Add the `include_track` parameter
query_params = {"artist": "Deep Purple", "include_track": True}

url = f"https://api.openweathermap.org/data/2.5/weather"

city_name = "Yangon"
api_key = os.getenv("open_weather_api_key")

query_params = {"q": city_name, "appid": api_key}

response = requests.get(url, params=query_params)

# Print the response URL
print(response.url)

print(response.text)
