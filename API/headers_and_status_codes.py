import requests, os
from dotenv import load_dotenv

load_dotenv()


url = f"https://api.openweathermap.org/data/2.5/weather"

city_name = "Yangon"
api_key = os.getenv("open_weather_api_key")

query_params = {"q": city_name, "appid": api_key}

response = requests.get(url, params=query_params)

# Check the response status code
if response.status_code == 200:
    print("The server responded succesfully!")
elif response.status_code == 404:
    print("Oops, that API could not be found!")
