# weather.py
import requests
import json

def get_weather(city):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=j1")
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None

