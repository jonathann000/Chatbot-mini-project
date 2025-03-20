import psycopg2
import re
import numpy as np
import joblib
from langchain_nomic.embeddings import NomicEmbeddings
from transit_data import transit_app
from weather_data import weather_app
from nlp_script import nlp_app, nlp_location
from places_data import places_app
from context import load_chat_context, update_chat_context, reset_chat_context

# Load the pretrained classifier
classifier = joblib.load('trained_classifier_model.pkl')

# Initialize embedding model
embedding_model = NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local")

def ChatBot():
    reset_chat_context()
    print("Hello! I am chatbot. I am here to help you with your queries.")
    print("Please enter your query.")
    while(True):
        query = input()
        query_type = analyze_input(query)

        if query == "exit":
            break
        
        if query_type == "restaurant":
            location = load_chat_context()["places"]["location"]
            place_type = load_chat_context()["places"]["place_type"]
            query_location = nlp_location(query)
            if query_location is not None:
                location = query_location
            if location is None:
                print("What location are you interested in?")
                location = input()
            update_chat_context("places", "location", location)
            places_app(location, place_type)
            
        elif query_type == "weather":
            location = load_chat_context()["weather"]["location"]
            day = load_chat_context()["weather"]["day"]
            query_location = nlp_location(query)
            if query_location is not None:
                location = query_location
            if location is None:
                print("What location are you interested in?")
                location = input()
            if "today" in query:
                day = "1"
            elif "tomorrow" in query:
                day = "2"
            elif "next week" in query:
                day = "3"
            elif day is None:
                print("What day are you interested in?")
                day = input()
            update_chat_context("weather", "location", location)
            weather_app(location, day)
        elif query_type == "transport":
            #departure, arrival = None, None
            arrival = load_chat_context()["transport"]["location"]
            query_departure, query_arrival = nlp_app(query)
            if query_arrival is not None:
                arrival = query_arrival
            if query_departure is not None:
                departure = query_departure
            if departure is None:
                print("Please enter the departure location")
                departure = input()
            if arrival is None:
                print("Please enter the arrival location")
                arrival = input()
            print(f"from: {departure}, to: {arrival}")
            update_chat_context("transport", "departure", departure)
            update_chat_context("transport", "arrival", arrival)
            transit_app(departure, arrival)
            update_chat_context("transport", "location", arrival)
            
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
    
ChatBot()
