# Import the correct exception class
import requests
from requests.exceptions import ConnectionError, HTTPError
import time

url = "http://wronghost:3000/albums"
try:
    r = requests.get(url)
    print(r.status_code)

# Use the imported class to intercept the connection error
except ConnectionError as conn_err:
    print(f"Connection Error! {conn_err}.")


url = "http://localhost:3000/albums/"
try:
    r = requests.get(url)

    # Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)

# Intercept the error
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")


longestTrackLength = 0
longestTrackTitle = ""
headers = {"Authorization": "Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3"}
page_number = 1

while True:
    params = {"page": page_number, "per_page": 500}
    response = requests.get(
        "http://localhost:3000/tracks", params=params, headers=headers
    )
    response.raise_for_status()
    response_data = response.json()

    print(f"Fetching tracks page {page_number}")

    if len(response_data["results"]) == 0:
        break

    for track in response_data["results"]:
        if track["Length"] > longestTrackLength:
            longestTrackLength = track["Length"]
            longestTrackTitle = track["Name"]

    page_number = page_number + 1

    # Add your fix here
    time.sleep(3)

print("The longest track in my music library is: " + longestTrackTitle)
