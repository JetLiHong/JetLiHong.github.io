#2 using dictionary

import tkinter as tk 
import time
import datetime
import pytz

#define window
root = tk.Tk()
root.title("Groep3 klok")
root.geometry("1000x750")

#2 dictionary
# cities = {
    # "Rotterdam": "Europe/Amsterdam",
    # "Tokyo": "Asia/Tokyo",
    # "New York": "America/New_York",
#}

#2 dictionary: Create labels for each time zone
# labels = {}
# for i, (city, tz) in enumerate(cities.items()):
    # labels[city] = tk.Label(root, text=city, font=("Arial", 50))
    # labels[city].grid(row=i, column=0)


def tijdsaanduiding():

    # Get the current time as a datetime object
    current_time = datetime.datetime.now()  

    label.config(text=current_time.strftime("%H:%M:%S"))
    label3.config(text=current_time.astimezone(pytz.timezone("Asia/Tokyo")).strftime("%H:%M:%S"))
    label5.config(text=current_time.astimezone(pytz.timezone("America/New_York")).strftime("%H:%M:%S"))
    
    #2 dictionary
    # for city, label in labels.items():
        # timezone = pytz.timezone(cities[city])
        # current_time = datetime.now(timezone).strftime("%H:%M:%S")
        # label.config(text=f"{city}: {current_time}")


    # Schedule the function to run every second
    root.after(1000, tijdsaanduiding)

label = tk.Label(root, text="tijd", font=("Arial", 70, "bold"))
label.grid(row=0, column=0)
label2 = tk.Label(root, text="Rotterdam", font=("Arial", 50))
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="tijd", font=("Arial", 70, "bold"))
label3.grid(row=2, column=0)
label4 = tk.Label(root, text="Tokyo", font=("Arial", 50))
label4.grid(row=3, column=0)

label5 = tk.Label(root, text="tijd", font=("Arial", 70, "bold"))
label5.grid(row=4, column=0)
label6 = tk.Label(root, text="New York", font=("Arial", 50))
label6.grid(row=5, column=0)

tijdsaanduiding()

root.mainloop()
