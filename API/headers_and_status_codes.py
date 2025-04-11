import requests
import os
from dotenv import load_dotenv

load_dotenv()


url = f"https://api.openweathermap.org/data/2.5/weather"

city_name = "Yangon"
api_key = os.getenv("open_weather_api_key")

query_params = {"q": city_name, "appid": api_key}
# headers = {"accept": "application/json"}
headers = {"accept": "application/xml"}

response = requests.get(url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == requests.codes.ok:
    print("The server responded succesfully!")
elif response.status_code == requests.codes.not_found:
    print("Oops, that API could not be found!")

# Check if the server did not accept the request
if response.status_code == 406:
    print("The server can not respond in XML")

    # Print the accepted content types
    print(
        "These are the content types the server accepts: "
        + response.headers.get("accept")
    )
else:
    print(response.text)

# Print the response content-type header
print(response.headers.get("content-type"))

# Print the response accept header
print(response.headers.get("accept"))
