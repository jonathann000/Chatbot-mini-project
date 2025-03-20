import requests
import json


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
        print("Invalid API key format in file.") 


def get_coordinates(api_key, location):
    
    # GOOGLE Places requires coordinates. We use google geocoding API to convert location to coords.
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
    "address": location, 
    "key": api_key
    }

    try:
        response = requests.get(geocode_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "OK":
            lat = data["results"][0]["geometry"]["location"]["lat"]
            lng = data["results"][0]["geometry"]["location"]["lng"]
            return lat, lng
        else:
            print(f"Geocoding failed: {data['status']} - {data.get('error_message', '')}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_nearby_places(api_key, location, radius, type_, numberOfResults):
    
    lat, long = get_coordinates(api_key, location)

    if lat is None or long is None:
        print("Could not determine coordinates. Exiting.")
        return None
    
    base_url = "https://places.googleapis.com/v1/places:searchNearby"
    
    # GOOGLE Places requires request.post instead of get.
    # Request payload
    payload = {
        "includedTypes": [type_],
        "maxResultCount": numberOfResults,
        "locationRestriction": {
            "circle": {
                "center": {"latitude": lat, "longitude": long},
                "radius": float(radius)
            }
        }
    }
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.regularOpeningHours,places.rating"
    }

    try:
        response = requests.post(base_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        #print(response.json())  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching nearby {type_}(s): {e}")
        return None

def get_filtered_response(data, type_, numberOfResults):
    i = 0
    try:
        for places in data["places"]:
            i += 1 
            loc = places["formattedAddress"]
            name = places["displayName"]["text"]
            rating = places["rating"]
            opennow = places["regularOpeningHours"]["openNow"]
            #currently unused
            #schedule = places["regularOpeningHours"]["weekdayDescriptions"]
            print(f"Here is result {i}: It's a place called {name}, with a rating of {rating}")
            if(opennow):
                print(f"{name} is currently open!")
            else: 
                print(f"{name} is unfortunately not open right now")
            print("--------------------")
    except: 
        print(f"I couldnt find {numberOfResults} result(s) matching {type_}")
        print("Would like")
            
def places_app(location, type_, numberOfResults = 5, radius = 500):
    api_key = get_api_key("GOOGLE_API", "apikey.txt") 
    response = get_nearby_places(api_key, location, radius, type_, numberOfResults)
    get_filtered_response(response, type_, numberOfResults)

    
places_app("chalmers", 500, "restaurant", 3)