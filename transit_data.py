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


def get_transit_directions(api_key, origin, destination):
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": "transit", 
        "key": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transit directions: {e}")
        return None

def get_filtered_response(data):
    from_ = data["routes"][0]["legs"][0]["start_address"]
    to_ = data["routes"][0]["legs"][0]["end_address"]

    for steps in data["routes"][0]["legs"][0][]


    print(f"You want to travel from {from_} to {to_}?")

api_key = get_api_key("GOOGLE_API","DesignOfAI-ass7/apikey.txt") 
response = get_transit_directions(api_key, "lindholmen", "chalmers")
get_filtered_response(response)
