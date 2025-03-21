import json
import os

JSON_FILE = "chat_context.json"

def load_chat_context():
    #failsafe, if it cannot find the json file. 
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    else:
        return {
            "transport": {
                "location": None,
                "day": None,
                "departure": None,
                "arrival": None
            },
            "places": {
                "location": None,
                "place_type": "restaurant",
                "radius": 500,
                "number_of_results": 5
            },
            "weather": {
                "location": None,
                "day": None
            }
        }

def save_chat_context(context):
    #saves the new values into the json object
    with open(JSON_FILE, "w") as file:
        json.dump(context, file, indent=4)

def update_chat_context(category, key, value):
    context = load_chat_context()

    # Update the specific category
    if category in context and key in context[category]:
        context[category][key] = value

    #If the key is a shared variable, update all sections
    if key in ["location", "day"]:
        for section in context:
            if key in context[section]:  #Only update if the key exists in the section
                context[section][key] = value

    save_chat_context(context)

def reset_chat_context():
    empty_context = {
            "transport": {
                "location": None,
                "day": None,
                "departure": None,
                "arrival": None
            },
            "places": {
                "location": None,
                "place_type": "restaurant",
                "radius": 500,
                "number_of_results": 5
            },
            "weather": {
                "location": None,
                "day": None
            }
        }
    save_chat_context(empty_context)