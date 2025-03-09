-- Insert data into Weather table
INSERT INTO Weather (location_, date_, time_, weather_type) VALUES
('New York', 'today', '08:00:00', 'sunny'),
('New York', 'today', '14:00:00', 'partly cloudy'),
('New York', 'tomorrow', '09:30:00', 'rainy'),
('New York', 'next_week', '12:15:00', 'snowy'),

('Los Angeles', 'today', '09:00:00', 'cloudy'),
('Los Angeles', 'today', '15:00:00', 'sunny'),
('Los Angeles', 'tomorrow', '10:00:00', 'clear'),
('Los Angeles', 'next_week', '18:45:00', 'hazy'),

('Chicago', 'today', '07:30:00', 'windy'),
('Chicago', 'today', '13:20:00', 'chilly'),
('Chicago', 'tomorrow', '11:00:00', 'snowy'),
('Chicago', 'next_week', '21:00:00', 'clear'),

('Houston', 'today', '10:15:00', 'sunny'),
('Houston', 'today', '16:30:00', 'stormy'),
('Houston', 'tomorrow', '07:45:00', 'cloudy'),
('Houston', 'next_week', '23:10:00', 'humid'),

('Miami', 'today', '06:45:00', 'rainy'),
('Miami', 'today', '12:00:00', 'sunny'),
('Miami', 'tomorrow', '14:30:00', 'stormy'),
('Miami', 'next_week', '19:20:00', 'clear'),

('Seattle', 'today', '11:00:00', 'stormy'),
('Seattle', 'today', '17:10:00', 'rainy'),
('Seattle', 'tomorrow', '09:50:00', 'cloudy'),
('Seattle', 'next_week', '22:00:00', 'foggy'),

('Denver', 'today', '09:30:00', 'windy'),
('Denver', 'today', '18:00:00', 'clear'),
('Denver', 'tomorrow', '08:40:00', 'chilly'),
('Denver', 'next_week', '20:10:00', 'snowy'),

('Boston', 'today', '12:00:00', 'clear'),
('Boston', 'today', '19:20:00', 'cloudy'),
('Boston', 'tomorrow', '10:50:00', 'sunny'),
('Boston', 'next_week', '17:30:00', 'windy'),

('San Francisco', 'today', '07:00:00', 'chilly'),
('San Francisco', 'today', '13:30:00', 'foggy'),
('San Francisco', 'tomorrow', '11:15:00', 'clear'),
('San Francisco', 'next_week', '15:40:00', 'sunny'),

('Dallas', 'today', '08:45:00', 'sunny'),
('Dallas', 'today', '16:45:00', 'partly cloudy'),
('Dallas', 'tomorrow', '10:20:00', 'rainy'),
('Dallas', 'next_week', '20:30:00', 'windy'),

('Atlanta', 'today', '10:30:00', 'sunny'),
('Atlanta', 'tomorrow', '17:20:00', 'humid'),
('Atlanta', 'next_week', '08:10:00', 'foggy'),
('Atlanta', 'next_week', '14:50:00', 'clear'),

('Phoenix', 'today', '09:15:00', 'windy'),
('Phoenix', 'tomorrow', '18:30:00', 'hot'),
('Phoenix', 'next_week', '07:55:00', 'clear'),
('Phoenix', 'next_week', '22:30:00', 'cloudy'),

('Philadelphia', 'today', '07:50:00', 'cloudy'),
('Philadelphia', 'tomorrow', '15:15:00', 'rainy'),
('Philadelphia', 'next_week', '12:40:00', 'sunny'),
('Philadelphia', 'next_week', '19:00:00', 'stormy'),

('San Diego', 'today', '08:20:00', 'windy'),
('San Diego', 'tomorrow', '14:50:00', 'hazy'),
('San Diego', 'next_week', '09:30:00', 'clear'),
('San Diego', 'next_week', '16:00:00', 'sunny'),

('Las Vegas', 'today', '06:30:00', 'sunny'),
('Las Vegas', 'tomorrow', '17:00:00', 'hot'),
('Las Vegas', 'next_week', '11:30:00', 'cloudy'),
('Las Vegas', 'next_week', '20:20:00', 'clear'),

('Portland', 'today', '11:45:00', 'sunny'),
('Portland', 'tomorrow', '18:10:00', 'foggy'),
('Portland', 'next_week', '07:45:00', 'rainy'),
('Portland', 'next_week', '23:00:00', 'stormy'),

('Austin', 'today', '09:00:00', 'cloudy'),
('Austin', 'tomorrow', '16:20:00', 'windy'),
('Austin', 'next_week', '10:50:00', 'sunny'),
('Austin', 'next_week', '21:40:00', 'rainy'),

('Detroit', 'today', '07:10:00', 'still'),
('Detroit', 'today', '15:30:00', 'chilly'),
('Detroit', 'tomorrow', '12:25:00', 'cloudy'),
('Detroit', 'next_week', '19:10:00', 'snowy'),

('Nashville', 'today', '10:50:00', 'gött'),
('Nashville', 'today', '14:15:00', 'clear'),
('Nashville', 'tomorrow', '09:40:00', 'windy'),
('Nashville', 'next_week', '18:00:00', 'cloudy'),

('Minneapolis', 'next_week', '08:40:00', 'sunny'),
('Minneapolis', 'next_week', '13:20:00', 'snowy'),
('Minneapolis', 'next_week', '11:10:00', 'cloudy'),
('Minneapolis', 'next_week', '17:45:00', 'chilly');


-- Insert data into Restaurants table
INSERT INTO Restaurants (rest_location, food_type, name_) VALUES
('New York', 'Italian', 'La Ristorante'),
('Los Angeles', 'Mexican', 'El Tacos'),
('Chicago', 'Steakhouse', 'Big Beef'),
('Houston', 'BBQ', 'Smoky Ribs'),
('Miami', 'Seafood', 'Tasty Prawn'),
('Seattle', 'Asian', 'Little bit of China'),
('Denver', 'Vegan', 'Taste of Green'),
('Boston', 'American', 'Big Bacon, Bigger Beers'),
('San Francisco', 'French', 'La Baguette'),
('Dallas', 'Tex-Mex', 'Nacho Libre'),
('Atlanta', 'Southern', 'Eagle Fried Chicken'),
('Phoenix', 'Southwestern', 'Cactus Grill'),
('Philadelphia', 'Cheesesteak', 'Cheese Please'),
('San Diego', 'Sushi', 'Fishy Business'),
('Las Vegas', 'Buffet', 'Poker and Plates'),
('Portland', 'Organic', 'Green Leaf'),
('Austin', 'BBQ', 'Spicy Smoke'),
('Detroit', 'Mediterranean', 'Olive Oil'),
('Nashville', 'Hot Chicken', 'Hot Hot Hot'),
('Minneapolis', 'Nordic', 'Viking Feast');

-- Insert data into Trains table
INSERT INTO Trains (departure_time, arrival_time, departure_location, arrival_location) VALUES
('08:00:00', '10:30:00', 'New York', 'Boston'),
('09:00:00', '11:45:00', 'Los Angeles', 'San Francisco'),
('10:00:00', '12:30:00', 'Chicago', 'Detroit'),
('11:00:00', '13:15:00', 'Houston', 'Austin'),
('12:00:00', '14:00:00', 'Miami', 'Atlanta'),
('13:00:00', '15:30:00', 'Seattle', 'Portland'),
('14:00:00', '16:45:00', 'Denver', 'Phoenix'),
('15:00:00', '17:30:00', 'Boston', 'New York'),
('16:00:00', '18:15:00', 'San Francisco', 'Los Angeles'),
('17:00:00', '19:00:00', 'Detroit', 'Chicago'),
('18:00:00', '20:30:00', 'Austin', 'Houston'),
('19:00:00', '21:45:00', 'Atlanta', 'Miami'),
('20:00:00', '22:15:00', 'Phoenix', 'Las Vegas'),
('21:00:00', '23:30:00', 'Portland', 'Seattle'),
('22:00:00', '00:30:00', 'Las Vegas', 'Los Angeles'),
('23:00:00', '01:00:00', 'Nashville', 'Minneapolis'),
('00:00:00', '02:00:00', 'Minneapolis', 'Nashville');

