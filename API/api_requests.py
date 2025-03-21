# Import the requests package
import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

# Pass the API URL to the get function
# response = requests.get("http://localhost:3000/lyrics")

# Print out the text attribute of the response object
# print(response.text)

city_name = "Yangon"

load_dotenv()
api_key = os.getenv("open_weather_api_key")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    data = response.json()

    print(response.url)

    df = pd.DataFrame(data["weather"])
    print(df)
    # df.to_json("yangon_weather.json")


except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError:
    print("The response was not valid JSON.")
