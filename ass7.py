import psycopg2
import re
import numpy as np
import joblib
from langchain_nomic.embeddings import NomicEmbeddings

# Load the pretrained classifier
classifier = joblib.load('trained_classifier_model.pkl')

# Initialize embedding model
embedding_model = NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local")

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
    locations = [row[0] for row in cursor.fetchall()] 
    conn.close()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM foods")
    foods = [row[0] for row in cursor.fetchall()]  
    conn.close()

    print("Hello! I am chatbot. I am here to help you with your queries.")
    print("Please enter your query.")
    while(True):
        query = input()
        query_type = analyze_input(query)

        if query == "exit":
            break
        if(query_type == "restaurant" or query_type == "weather" or query_type == "transport"):
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
            break
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
            break
        elif query_type == "transport":
            query = query.lower()
            departure, arrival = None, None
            for loc in locations:
                if "from " + loc.lower() in query:
                    departure = loc
                if "to " + loc.lower() in query:
                    arrival = loc
            train_query(departure, arrival)
            break
        else:
            print("Sorry, I can't help you with that query.")
            print("Maybe try again?")
            print("Or if you want to exit, please write exit")

def analyze_input(question):
    question = question.lower()

    # Generate embeddings for the question
    question_embedding = np.array([embedding_model.embed_query(question)])

    # Predict the query type using the classifier
    predicted_category = classifier.predict(question_embedding)[0]

    # Return the predicted category
    return predicted_category
    
def weather_query(query, location, day):
    if location is None:
        print("What location are you interested in?")
        location = input()
    if day is None:
        print("What day are you interested in?")
        day = input()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Weather WHERE LOWER(location_) %% LOWER(%s) AND LOWER(date_) %% LOWER(%s)", (location, day))
    results = cursor.fetchall()
    conn.close()

    if results:
        print("Here is the weather forecast in", location, "for", day)
        for row in results:
            print(f"- {row[2]}: {row[3]}")
    else:
        print("Sorry, I don't have any weather information for that location and time.")

def restaurant_query(query, location, food_type):
    query = query.lower()
    if location is None:
        print("What location are you looking for restaurants in?")
        location = input()
    if food_type is None:
        print("What type of food are you interested in?")
        food_type = input()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name_ FROM Restaurants WHERE LOWER(rest_location) %% LOWER(%s) AND LOWER(food_type) %% LOWER(%s)", (location, food_type))
    results = cursor.fetchall()

    conn.close()

    if results:
        print("Here are some restaurants that match your query:")
        for row in results:
            print(f"- {row[0]}")
    else:
        print("Sorry, no restaurants match your search criteria.")

def train_query(departure, arrival):
    if departure is None:
        print("What is the departure station? ")
        departure = input()
    if arrival is None:
        print("What is the arrival station?")
        arrival = input()

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Trains WHERE LOWER(departure_location) %% LOWER(%s) AND LOWER(arrival_location) %% LOWER(%s)", (departure, arrival))
    results = cursor.fetchall()
    conn.close()

    if results:
        print("Here are the train schedules for your query:")
        for row in results:
            print(f"{row[3]} to {row[4]} - Departure Time: {row[2]}")
    else:
        print(f'Sorry, no trains match your search criteria. {departure} to {arrival}')

connect_db()  
ChatBot()
