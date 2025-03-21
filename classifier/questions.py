import random

# Define example questions for each category
restaurant_questions = [
    "What are the best restaurants near me?",
    "Do you have vegan options?",
    "Is there a gluten-free menu?",
    "What are your hours of operation?",
    "Do I need a reservation?",
    "What is the average price for a meal?",
    "Can I order food online?",
    "Do you offer delivery or takeout?",
    "Is there parking available?",
    "What kind of cuisine do you serve?",
    "Do you accept credit cards?",
    "Are pets allowed in your restaurant?",
    "What is the best time to visit?",
    "Can I host an event at your restaurant?",
    "Do you have outdoor seating?",
    "Do you have a kids' menu?",
    "Is there a waitlist for dinner?",
    "Can I make a reservation for a large group?",
    "Do you have a bar?",
    "Is there Wi-Fi available?",
    "What is your specialty dish?",
    "Do you offer catering services?",
    "Is your restaurant wheelchair accessible?",
    "What are the prices for appetizers?",
    "Do you serve alcohol?",
    "Do you have a dessert menu?",
    "Can I bring my own wine?",
    "Is there a dress code?",
    "Do you have a loyalty program?",
    "Do you offer any daily specials?",
    "Is the restaurant kid-friendly?",
    "Are there any vegan desserts?",
    "Can I make a reservation for a specific time?",
    "Do you accept tips on credit cards?",
    "How long is the wait time for a table?",
    "Do you offer a buffet?",
    "Are there any gluten-free dessert options?",
    "What is the most popular dish?",
    "Do you serve breakfast?",
    "What is your address?",
    "Can I bring my own cake for a birthday?",
    "What kind of drinks do you serve?",
    "Do you offer a takeout menu?",
    "Is there a parking lot?",
    "Do you have any discounts for students?",
    "Do you have a breakfast menu?",
    "Are you open on holidays?",
    "Do you have a kids' play area?",
    "Can I see the wine list?",
    "How do I cancel my reservation?"
]

restaurant_questions += [
    "What are some good restaurants near my location?",
    "Can you recommend a vegan-friendly restaurant?",
    "Where can I find gluten-free dining options?",
    "What time does the restaurant close?",
    "Do I need to book a table in advance?",
    "What is the average cost of a meal at the restaurant?",
    "Can I place an order for delivery?",
    "Does the restaurant provide takeout services?",
    "Is there parking nearby?",
    "What types of cuisine does the restaurant offer?",
    "Can I pay with a credit card?",
    "Are pets allowed in the restaurant?",
    "Is it busy at the restaurant right now?",
    "Can I book a large group reservation?",
    "Does the restaurant offer outdoor seating?",
    "Is there a kids' menu available?",
    "How long is the wait for a table?",
    "Do you offer any special promotions today?",
    "Is there a bar at the restaurant?",
    "Can I bring my own wine for dinner?",
    "Is there a dress code at the restaurant?",
    "Can I make a reservation online?",
    "Is the restaurant wheelchair accessible?",
    "What is the specialty dish of the restaurant?",
    "Are there any vegetarian desserts?",
    "Does the restaurant offer catering?",
    "Is there Wi-Fi available at the restaurant?",
    "Can I cancel my reservation online?",
    "Do you offer breakfast options?",
    "Is the restaurant open on holidays?",
    "Do you offer any loyalty programs?"
]



weather_questions = [
    "What is the weather forecast for today?",
    "Will it rain tomorrow?",
    "What is the current temperature?",
    "Do I need an umbrella today?",
    "Is there a snowstorm expected?",
    "How hot is it outside?",
    "What is the wind speed today?",
    "Will the weather be sunny or cloudy?",
    "Is there a weather warning for my area?",
    "How much snow is expected this week?",
    "What is the UV index today?",
    "Is it going to be windy this afternoon?",
    "Will it be cold at night?",
    "What is the air quality today?",
    "Are there any storms coming?",
    "How long will the rain last?",
    "Will there be thunderstorms later?",
    "What is the humidity level today?",
    "How high is the pollen count today?",
    "What is the chance of precipitation?",
    "Will it be warm enough for a picnic?",
    "How much rain has fallen today?",
    "Is there a chance of snow this weekend?",
    "Will it be clear tonight?",
    "What is the temperature in Celsius/Fahrenheit?",
    "What is the weather like in New York?",
    "Is there a chance of hail today?",
    "What time will the sun set today?",
    "What time does the sun rise tomorrow?",
    "Is there a chance of fog this morning?",
    "What is the weather forecast for next week?",
    "Will there be any heatwaves soon?",
    "Is the weather warm enough for a beach day?",
    "Will there be any frost tonight?",
    "Is it safe to drive in the snow?",
    "Is there a tornado warning?",
    "How cold will it get tonight?",
    "What will the weather be like in 5 days?",
    "Will it be chilly tomorrow?",
    "How much will the temperature drop tonight?",
    "What is the weather in the mountains?",
    "Will it be a good day for hiking?",
    "What is the forecast for the weekend?",
    "Is it going to snow in the city?",
    "What is the air pressure today?",
    "Will it rain over the weekend?",
    "What is the dew point today?",
    "Is there a weather advisory in effect?",
    "Is it foggy outside?",
    "What is the weather like in my city?"
]

weather_questions += [
    "What will the weather be like tomorrow?",
    "How cold will it be this evening?",
    "Is there a chance of rain this weekend?",
    "What's the temperature right now?",
    "Do I need to wear a jacket today?",
    "Is it going to snow tomorrow?",
    "How hot is it expected to get this week?",
    "What is the air quality in the city today?",
    "Will it rain tonight?",
    "What is the wind speed going to be today?",
    "Is there a chance of thunderstorms today?",
    "Will it be sunny tomorrow?",
    "Is it a good day to go hiking?",
    "What will the weather be like next week?",
    "How many inches of snow are expected?",
    "Will it be windy this afternoon?",
    "Is there a weather advisory for the city?",
    "What is the forecast for this evening?",
    "Will there be frost tomorrow morning?",
    "What's the UV index for today?",
    "What time is the sun setting today?",
    "Will it be cloudy this weekend?",
    "What's the dew point right now?",
    "Is it safe to go outside in this weather?",
    "How much rain is expected this week?",
    "Is it going to be hot enough for a picnic?",
    "Will there be any snowstorms this week?",
    "What will the temperature be like in the evening?",
    "Is the weather warm enough for a beach day?",
    "What will the temperature be in the mountains?",
    "Will it be chilly tonight?",
    "What is the air pressure right now?",
    "What's the chance of rain tomorrow afternoon?",
    "How high is the pollen count today?",
    "Will it be foggy in the morning?",
    "Is it safe to travel in this weather?",
    "What is the forecast for the next 5 days?",
    "How much rain has fallen in the past 24 hours?",
    "Is the temperature going to drop tonight?",
    "What is the chance of hail this week?",
    "What's the temperature at the beach today?",
    "Will there be any storms in the evening?",
    "What's the current temperature in Celsius?",
    "Is it going to rain in the next hour?",
    "Is there a weather warning in effect?",
    "What's the weather like in the next 10 days?",
    "How long will the heatwave last?"
]


transport_questions = [
    "What is the nearest bus stop?",
    "How do I get to the airport by public transport?",
    "When is the next train to the city?",
    "Is there a subway station near me?",
    "How much is a bus ticket?",
    "Where can I catch a taxi?",
    "Is there a tram service in this area?",
    "How far is the train station from here?",
    "Can I use my contactless card on the bus?",
    "What time does the last bus leave?",
    "Are there any delays on the metro today?",
    "How do I get to the station from here?",
    "What is the cost of a monthly transport pass?",
    "Are there any night buses available?",
    "Where can I buy tickets for public transport?",
    "Is the train station wheelchair accessible?",
    "What is the nearest airport shuttle?",
    "How long does it take to get to the city center by train?",
    "Is there a bike-sharing program near me?",
    "How often do buses run on Sundays?",
    "Can I bring my pet on public transport?",
    "What time do the trains start operating?",
    "How can I check the bus schedule?",
    "Are there any public transport discounts?",
    "Do I need to change trains to get to the museum?",
    "Where can I park my car near the train station?",
    "Is there a direct bus to the airport?",
    "What is the best way to get to the city center from here?",
    "How far is the nearest metro station?",
    "Are there any free shuttle buses?",
    "Can I use an app to check train times?",
    "How long does the metro ride take?",
    "What is the closest bus stop to the restaurant?",
    "What is the frequency of the trains during rush hour?",
    "Can I bring luggage on the bus?",
    "Is there a transport strike today?",
    "Do I need a ticket for the tram?",
    "Are there parking spaces at the train station?",
    "How do I get to the zoo using public transport?",
    "What are the bus routes in this area?",
    "Is there a transport pass for tourists?",
    "Are there bike lanes near the train station?",
    "How do I change lines on the subway?",
    "Can I pay for my metro ticket with my phone?",
    "Is there a bus that goes to the beach?",
    "How can I get to the nearest park by public transport?"
]

transport_questions += [
    "I need to get to the airport, how do I go?",
    "How can I get to the city center from here?",
    "What is the fastest way to get to the train station?",
    "I want to go to the beach, how do I get there?",
    "How do I get to the nearest bus stop?",
    "I want to travel from New York to Chicago by train, how can I do that?",
    "How do I get from here to the airport?",
    "Can you tell me how to reach the museum using public transport?",
    "What is the best way to get to the zoo?",
    "I need a train from London to Paris, can you help?",
    "How do I get to the nearest metro station?",
    "I want to go to the nearest restaurant, which transport should I take?",
    "What's the quickest way to get to the shopping mall?",
    "How do I get to the airport by bus?",
    "Can I catch a tram from here to the park?",
    "How do I get from here to the hospital?",
    "I want to travel to London from Manchester, what's the easiest route?",
    "How do I get to the nearest bus stop?",
    "What's the best way to get to the museum by public transport?",
    "I'm traveling from Paris to Berlin, what's the best route?",
    "How do I get to the nearest subway station?",
    "Can I get to the airport by train?",
    "How do I get to the train station from here?",
    "I want to go to the beach, what's the best public transport option?",
    "How do I get to the nearest bike station?",
    "Can I take a bus to the city center?",
    "What time does the last bus leave from here?",
    "How do I travel to the concert venue from here?",
    "Can you help me get to the theater by train?",
    "How far is the nearest bus stop from my location?",
    "What is the quickest way to get to the shopping mall from here?",
    "I need to travel to the airport, is there a metro?",
    "What is the best way to reach the train station?",
    "How can I get to the nearest tram station?",
    "Can I take a taxi to the airport from here?",
    "What time do buses leave for the beach?",
    "Can I get a train to the city center from the airport?",
    "How can I get to the museum using public transport?",
    "How far is the nearest subway station?",
    "I'm traveling to the stadium, what's the easiest way to get there?",
    "Can I walk to the metro from here?",
    "I need to get to a concert, what's the best way?",
    "How can I get to the nearest park by train?",
    "How do I travel to the city center from the airport?",
    "Is there a tram to the city center?",
    "I'm heading to the stadium, what's the best public transport?",
    "Can I take a taxi from the station to my hotel?",
    "How do I get to the university by public transport?",
    "Can you tell me the bus route to the shopping mall?"
]


# Label each question with its category
restaurant_labeled = [(q, "restaurant") for q in restaurant_questions]
weather_labeled = [(q, "weather") for q in weather_questions]
transport_labeled = [(q, "transport") for q in transport_questions]

# Shuffle each category independently
random.shuffle(restaurant_labeled)
random.shuffle(weather_labeled)
random.shuffle(transport_labeled)

# Define the split ratio (90% training, 10% testing)
train_ratio = 0.9  

# Compute the split indices
num_train_restaurant = int(len(restaurant_labeled) * train_ratio)
num_train_weather = int(len(weather_labeled) * train_ratio)
num_train_transport = int(len(transport_labeled) * train_ratio)

# Split into training and test sets
train_set = (
    restaurant_labeled[:num_train_restaurant] + 
    weather_labeled[:num_train_weather] + 
    transport_labeled[:num_train_transport]
)

test_set = (
    restaurant_labeled[num_train_restaurant:] + 
    weather_labeled[num_train_weather:] + 
    transport_labeled[num_train_transport:]
)

# Shuffle the final training set to mix categories
random.shuffle(train_set)
random.shuffle(test_set)

# Separate into features (questions) and labels (categories)
train_x, train_y = zip(*train_set)  # Unzips into two lists
test_x, test_y = zip(*test_set)  # Unzips into two lists

# Print checks
print(f"Total training questions: {len(train_x)}")
print(f"Total test questions: {len(test_x)}")
print(f"Restaurant test: {len(restaurant_labeled[num_train_restaurant:])}")
print(f"Weather test: {len(weather_labeled[num_train_weather:])}")
print(f"Transport test: {len(transport_labeled[num_train_transport:])}")

# Show a small sample of the training set
for q, label in zip(train_x[:10], train_y[:10]):
    print(f"Q: {q} -> Category: {label}")

print(len(train_x), len(train_y), len(test_x), len(test_y))
