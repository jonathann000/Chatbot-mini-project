CREATE TABLE Weather (
    location_ TEXT NOT NULL,
    date_ TEXT NOT NULL,  
    CHECK (date_ IN ('today', 'tomorrow', 'next_week')),  
    time_ TIME NOT NULL,    
    weather_type TEXT NOT NULL,    
    PRIMARY KEY(location_, date_, time_)
);

CREATE TABLE Restaurants (
    rest_location TEXT NOT NULL,
    food_type TEXT NOT NULL,
    name_ TEXT NOT NULL,
    PRIMARY KEY(rest_location, food_type, name_)
);

CREATE TABLE Trains (
    train_id SERIAL PRIMARY KEY,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    departure_location TEXT NOT NULL,
    arrival_location TEXT NOT NULL
);

