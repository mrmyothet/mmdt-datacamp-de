import requests

playlists = [
    {"Name": "Rock ballads"},
    {"Name": "My favorite songs"},
    {"Name": "Road Trip"},
]

# POST the playlists array to the API using the json argument
requests.post("http://localhost:3000/playlists/", json=playlists)

# Get the list of all created playlists
response = requests.get("http://localhost:3000/playlists")

# Print the response text to inspect the JSON text
print(response.json)
