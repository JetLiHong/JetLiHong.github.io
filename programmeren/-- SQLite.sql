CREATE TABLE time_zones (
    city TEXT PRIMARY KEY,
    time_zone TEXT
);

-- Insert data into the table
INSERT INTO time_zones (city, time_zone)
VALUES
    ('Rotterdam', 'Europe/Amsterdam'),
    ('New York', 'America/New_York'),
    ('Tokyo', 'Asia/Tokyo');
