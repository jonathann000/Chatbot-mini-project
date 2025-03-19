import requests

def get_api_key(service, filepath):
    try:
        with open(filepath, "r") as file:
            for line in file:
                key, value = line.strip().split("=") 
                if key == service:
                    return value
    except FileNotFoundError:
        print(f"API key file '{filepath}' not found.")
    except ValueError:
        print("Invalid API key format in file. Use KEY=VALUE format.")
    
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

    
def get_filtered_weather_data(data, days):
    location_name = data["location"]["name"]
    country = data["location"]["country"]
    '''
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]
    '''

    print(f"{days}-days Weather Forecast for {location_name}, {country}:")

    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        max_temp = day["day"]["maxtemp_c"]
        min_temp = day["day"]["mintemp_c"]
        condition = day["day"]["condition"]["text"]
        chance_of_rain = day["day"]["daily_chance_of_rain"]

        print(f"\nDate: {date}")
        print(f"- Condition: {condition}")
        print(f"- Max Temp: {max_temp}°C, Min Temp: {min_temp}°C")
        print(f"- Risk of Rain: {chance_of_rain}%")
        print("-------------------------------------------------")

def weather_app(location, days):
    API_KEY = get_api_key("WEATHER_API","apikey.txt") 
    weather_data = get_weather_data(API_KEY, location, days)
    get_filtered_weather_data(weather_data, days)



