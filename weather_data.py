import requests

def get_api_key(filepath):
    try:
        with open(filepath, "r") as file:
            return file.readline().strip() 
    except FileNotFoundError:
        print("API key file not found.")
        return None

def get_weather_data(api_key, location, days):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": location,
        "days": days,
        "aqi": "no",
        "alerts": "no"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()   
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

    
def get_filtered_weather_data(data):
    location_name = data["location"]["name"]
    country = data["location"]["country"]
    '''
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]
    '''

    print(f"3-Day Weather Forecast for {location_name}, {country}:")

    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        max_temp = day["day"]["maxtemp_c"]
        min_temp = day["day"]["mintemp_c"]
        condition = day["day"]["condition"]["text"]
        chance_of_rain = day["day"]["daily_chance_of_rain"]

        print(f"\nDate: {date}")
        print(f"- Condition: {condition}")
        print(f"- Max Temp: {max_temp}°C, Min Temp: {min_temp}°C")
        print(f"- Chance of Rain: {chance_of_rain}%")
        print("-------------------------------------------------")


API_KEY = get_api_key("DesignOfAI-ass7/apikey.txt") 
location = "London"
days = 3
weather_data = get_weather_data(API_KEY, location, days)
get_filtered_weather_data(weather_data)

