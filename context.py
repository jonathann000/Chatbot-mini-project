import json
import os

JSON_FILE = "chat_context.json"

def load_chat_context():
    """Loads the conversation context from a JSON file."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    else:
        return {
            "transport": {
                "location": None,
                "day": None,
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
    """Saves the updated conversation context back to the JSON file."""
    with open(JSON_FILE, "w") as file:
        json.dump(context, file, indent=4)

def update_chat_context(category, key, value):
    """
    Updates a specific field in the chat context.
    If the key is a shared variable (like 'location' or 'day'), update all categories.
    """
    context = load_chat_context()

    # Update the specific category
    if category in context and key in context[category]:
        context[category][key] = value

    # If the key is a shared variable, update all sections
    if key in ["location", "day"]:
        for section in context:
            if key in context[section]:  # Only update if the key exists in the section
                context[section][key] = value

    save_chat_context(context)

def reset_chat_context():
    empty_context = {
            "transport": {
                "location": None,
                "day": None,
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