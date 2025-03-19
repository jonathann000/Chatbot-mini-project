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
        print("Invalid API key format in file.") 


def get_nearby_places(api_key, location, radius, type_):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": type_,
        "key": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        print(response.url)
        print(response.json())  # Print full API response for debugging
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching nearby {type_}(s): {e}")
        return None

#def get_filtered_response(data):
api_key = get_api_key("GOOGLE_API","DesignOfAI-ass7/apikey.txt") 
response = get_nearby_places(api_key, "chalmers", "1000", "restaurant")
#get_filtered_response(response)

    
    