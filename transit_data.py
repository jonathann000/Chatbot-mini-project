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
        print(response.url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transit directions: {e}")
        return None

def get_filtered_response(data, location, destination):
    from_ = data["routes"][0]["legs"][0]["start_address"]
    to_ = data["routes"][0]["legs"][0]["end_address"]
    print(f"To walk from {from_} to {to_}, please follow the steps")
    i = 0

    try: 
        for step in data["routes"][0]["legs"][0]["steps"]:
            travel_mode = step["travel_mode"]
            if travel_mode == "WALKING":
                i += 1
                print(f"Step {i}:")
                distance = step["distance"]["text"]
                print(f" Walk {distance}")
                print(f" {step['html_instructions']}")


            elif travel_mode == "TRANSIT":
                i += 1
                transit_details = step["transit_details"]
                try:
                    line_name = transit_details["line"]["name"]
                except:
                    line_name = transit_details["line"]["short_name"]
                vehicle_type = transit_details["line"]["vehicle"]["type"]
                departure_stop = transit_details["departure_stop"]["name"]
                arrival_stop = transit_details["arrival_stop"]["name"]
                departure_time = transit_details["departure_time"]["text"]
                arrival_time = transit_details["arrival_time"]["text"]
                print(f"Step {i}:")
                print(f" Take {vehicle_type} ({line_name})")
                print(f" From: {departure_stop} at {departure_time}")
                print(f" To: {arrival_stop} at {arrival_time}")
                print(f" Duration: {step['duration']['text']}")
    except: 
        print(f"I was unable to find a route from {location} to {destination}")

def transit_app(location, destination):
    api_key = get_api_key("GOOGLE_API","apikey.txt")
    response = get_transit_directions(api_key, location, destination)
    get_filtered_response(response, location, destination)