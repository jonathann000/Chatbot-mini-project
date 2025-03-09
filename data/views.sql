CREATE VIEW locations AS
SELECT location_ as "location" FROM Weather
UNION
SELECT rest_location as "location" FROM Restaurants;

CREATE VIEW Time AS
SELECT time_ FROM Weather;

CREATE VIEW foods AS
SELECT food_type FROM Restaurants;


