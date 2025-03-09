import psycopg2
import re

def connect_db():
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="postgres",
    )

def ChatBot():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM locations")
    locations = [row[0] for row in cursor.fetchall()]  # Extract values from tuples
    conn.close()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM foods")
    foods = [row[0] for row in cursor.fetchall()]  # Extract values from tuples
    conn.close()
    
    print("Hello! I am chatbot. I am here to help you with your queries.")
    print("Please enter your query.")
    query = input()
    query_type = analyze_input(query)
    print("You asked me about", query_type)
    if query_type == "restaurant":
            query = query.lower()
            location = None
            food_type = None
            for loc in locations:
                if loc.lower() in query:
                    location = loc
                    break
            for food in foods:
                if food.lower() in query:
                    food_type = food
                    break
            restaurant_query(query, location, food_type)
    elif query_type == "weather":
        query = query.lower()
        location = None
        day = None
        for loc in locations:
            if loc.lower() in query:
                location = loc
                break
        if "today" in query:
            day = "today"
        elif "tomorrow" in query:
            day = "tomorrow"
        elif "next week" in query:
            day = "next_week"
        weather_query(query, location, day)
    else:
        print("Sorry, I can't help you with that query.")

def analyze_input(question):
    question = question.lower()
    
    keyword_mapping = {
        "weather": ["weather", "forecast", "temperature", "rain", "sunny"],
        "restaurant": ["restaurant", "food", "eat", "cuisine", "dining", "hungry"],
        "public transport": ["tram", "bus", "metro", "train", "transport"]
    }
    
    for category, keywords in keyword_mapping.items():
        if any(re.search(r'\b' + keyword + r'\b', question) for keyword in keywords):
            return category
    
    return "other"
    
def weather_query(query, location, day):
    if location is None:
        location = input("What location are you interested in? ")
    if day is None:
        day = input("What day are you interested in? ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Weather WHERE LOWER(location_) LIKE LOWER(%s) AND LOWER(date_) LIKE LOWER(%s)", (location, day))
    results = cursor.fetchall()
    conn.close()

    if results:
        print("Here is the weather forecast for", location, "for", day)
        for row in results:
            print(f"- {row[2]}: {row[3]}")
    else:
        print("Sorry, I don't have any weather information for that location and time.")

# Function to query restaurant information
def restaurant_query(query, location, food_type):
    query = query.lower()
    if location is None:
        location = input("What location are you looking for restaurants in? ")
    if food_type is None:
        food_type = input("What type of food are you interested in? ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name_ FROM Restaurants WHERE LOWER(rest_location) LIKE LOWER(%s) AND LOWER(food_type) LIKE LOWER(%s)", (location, food_type))
    results = cursor.fetchall()

    conn.close()

    if results:
        print("Here are some restaurants that match your query:")
        for row in results:
            print(f"- {row[0]}")
    else:
        print("Sorry, no restaurants match your search criteria.")

connect_db()  
ChatBot()
