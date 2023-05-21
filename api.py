import requests
import json
import creds

ingredients = ['"Tuna"', "Cheese"]  # List of ingredients to search for

# API credentials
api_id = creds.api_id
api_key =  creds.api_key

# API endpoint and parameters
url = "https://api.edamam.com/search"
params = {
    "q": " ".join(ingredients),  # Join the ingredients with spaces
    "app_id": api_id,
    "app_key": api_key,
    "from": 0,  # Start index of the results
    "to": 10,   # Number of results to retrieve
}

# Send GET request
response = requests.get(url, params=params)

# Parse response as JSON
data = json.loads(response.text)

# Extract recipe information
for recipe in data["hits"]:
    recipe_details = recipe["recipe"]
    recipe_name = recipe_details["label"]
    recipe_url = recipe_details["url"]
    print(f"Recipe: {recipe_name}")
    print(f"URL: {recipe_url}")
    print("-----")