import os
import random
import requests 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GIPHY_API_KEY")
API_URL = "https://api.giphy.com/v1/gifs/search"

def get_gif(query):
    random_offset = random.randint(0, 15)
    params = {
        "api_key": API_KEY,
        "q": query,
        "limit": 1,
        "rating": 'g'
    } 
    
    response = requests.get(API_URL, params=params)
    result = response.json()

    if result.get("data"):
        return result["data"][0]["images"]["original"]["url"]
    return "No GIF found"