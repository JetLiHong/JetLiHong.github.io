import tkinter as tk
import time
import pytz
import sqlite3
from datetime import datetime

# Function to fetch city-time zone mappings from the database
def get_city_time_zones():
    connection = sqlite3.connect("city_time_zones.db")  # Replace with your database file name
    cursor = connection.cursor()
    cursor.execute("SELECT city, time_zone FROM time_zones")
    data = cursor.fetchall()
    connection.close()
    return dict(data)

# Function to update the time for all clocks
def update_time():
    for city, zone in time_zones.items():
        current_time = time.strftime(
            "%H:%M:%S",
            time.gmtime(
                time.time() + pytz.timezone(zone).utcoffset(datetime.now()).seconds
            ),
        )
        clock_labels[city].config(text=f"{city}: {current_time}")
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("World Clocks")
root.geometry("800x300")

# Retrieve city-time zone mappings from the database
time_zones = get_city_time_zones()

# Create a dictionary to store labels for each city's clock
clock_labels = {}

# Create and display clock labels for each city
for i, (city, _) in enumerate(time_zones.items()):
    font_style = ("Arial", 20)  # Default font style for other cities
    if city == "Rotterdam":
        font_style = ("Arial", 50, "bold")  # Bold and bigger for Rotterdam
    label = tk.Label(root, text=f"{city}:", font=font_style)
    label.grid(row=i + 1, column=0, padx=10, pady=10)
    clock_labels[city] = label

# Start updating the time
update_time()

# Run the application
root.mainloop()

