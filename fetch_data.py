# import required modules
import requests,json
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
api_key =os.getenv("OPENWEATHER_API_KEY") 
#input_city = "Kolkata"
def get_weather(input_city):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    url=f"{base_url}?q={input_city}&appid={api_key}"
    r = requests.get(url)
    data = r.json()
    return data

# make a function to get the above data

def get_weather_data(city):
    """Process weather data and return a pandas DataFrame + error message."""
    data = get_weather(city)

    # API error handling
    if not isinstance(data, dict) or data.get("cod") != 200:
        return None, f"Error: {data.get('message', 'Unknown error')}"

    try:
        weather_data = {
            'City': data['name'],
            'Country': data['sys']['country'],
            'Longitude': data['coord']['lon'],
            'Latitude': data['coord']['lat'],
            'Weather Description': data['weather'][0]['description'],
            'Temperature (°C)': round(data['main']['temp'] - 273.15, 2),
            'Pressure (hPa)': data['main']['pressure'],
            'Humidity (%)': data['main']['humidity'],
            'Wind Speed (m/s)': data['wind']['speed'],
            'Wind Direction (°)': data['wind'].get('deg', None),
            'Cloudiness (%)': data['clouds']['all'],
            'Sunrise (UTC)': pd.to_datetime(data['sys']['sunrise'], unit='s'),
            'Sunset (UTC)': pd.to_datetime(data['sys']['sunset'], unit='s')
        }

        df = pd.DataFrame([weather_data])
        return df, None

    except Exception as e:
        return None, f"Processing error: {str(e)}"
