import json
import requests

# Load the JSON file
with open(r'C:\Users\marco\.vscode\python\projects\columbia\assingments\json\project\res\memory.json') as file:
    config = json.load(file)

# Extract the URL from the JSON data
url = config.get('j1')

# Make the GET request
response = requests.get(config[url])

# Check if the request was successful
if response.status_code == 200:
    # Print the response JSON
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
