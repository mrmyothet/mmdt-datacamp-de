import requests, os
from dotenv import load_dotenv

load_dotenv()

url = f"https://api.openweathermap.org/data/2.5/weather"

city_name = "Yangon"
api_key = os.getenv("open_weather_api_key")

query_params = {"q": city_name, "appid": api_key}
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, params=query_params)

# Check if the status code on the response object matches a successful response
if response.status_code == 200:
    print("Success!")
# Check if the status code indicates a failed authentication attempt
elif response.status_code == 401:
    print("Authentication failed")
else:
    print("Another error occurred")


# Create a headers dictionary containing and set the API key using the correct key and value
headers = {"Authorization": "Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3"}
# Add the headers dictionary to the requests.get() call using the correct function argument
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success!")
elif response.status_code == 401:
    print("Authentication failed")
else:
    print("Another error occurred")
