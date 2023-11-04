import tkinter as tk
import math

def calculate(entry_massa_giek, entry_massa_last, entry_hoek_A, result_label):
    massa_giek = float(entry_massa_giek.get())
    massa_last = float(entry_massa_last.get())
    hoek_A = float(entry_hoek_A.get())

    hoek_Y = bereken_hoek_Y(hoek_A)
    Fb, hoek_X, Fa, hoek_Z = bereken_force_en_moment(hoek_A, hoek_Y, massa_giek, massa_last)

    result_text = f"Hoek Y: {hoek_Y:.2f}\nHoek X: {hoek_X:.2f}\nForce B: {Fb:.2f}\nForce A: {Fa:.2f}\nhoek Z: {hoek_Z:.2f}"
    result_label.config(text=result_text)

def bereken_hoek_Y(hoek_A):
    # Berekeningen voor hoek Y
    # Driehoek ABC, driehoek ADC, driekhoek AEC en driekhoek DEC

    # Schuine zijde berekenen van driehoek ABC
    AC = math.sqrt(10**2 + 1.5**2)

    # Hoek A1 berekenen
    hoek_A1 = math.degrees(math.atan(1.5/10))

    # Hoek A2 berekenen
    hoek_A2 = hoek_A - hoek_A1

    AD = 5.71725

    # Zijde AE berekenen
    AE = math.cos(math.radians(hoek_A2)) * AC

    # Zijde EC berekenen
    EC = math.sin(math.radians(hoek_A2)) * AC

    # Zijde DE berekenen
    DE = AE - AD

    # Hoek Y berekenen
    hoek_Y = math.degrees(math.atan(DE/EC))

    return hoek_Y

def bereken_force_en_moment(hoek_A, hoek_Y, massa_giek, massa_last):
    # Berekeningen voor Force en Moment

    hoek_X = 90 - hoek_A - hoek_Y

    a = massa_last * 35 * math.cos(math.radians(hoek_A)) + massa_giek * 16 * math.cos(math.radians(hoek_A))
    b = 10 * math.sin(math.radians(hoek_X))
    c = 1.5 * math.cos(math.radians(hoek_X))

    Fb = a / (b + c)

    # Berekeningen voor Fb (x-direction) en Fb (y-direction)
    Fb_x = Fb * math.cos(math.radians(hoek_X))
    Fb_y = Fb * math.sin(math.radians(hoek_X))

    # Berekeningen voor Fax en Fay
    Fax = -Fb_x + massa_giek * math.sin(math.radians(hoek_A)) + massa_last * math.sin(math.radians(hoek_A))
    Fay = Fb_y * math.sin(math.radians(hoek_X)) - massa_giek * math.cos(math.radians(hoek_A)) - massa_last * math.cos(math.radians(hoek_A))

    # Berekeningen voor hoek Z en Fa
    hoek_Z = math.degrees(math.atan(abs(Fay) / abs(Fax)))

    Fa = Fay / math.sin(math.radians(hoek_Z))

    return Fb, hoek_X, Fa, hoek_Z

root = tk.Tk()
root.title("Giek Berekeningen")
root.geometry("300x400")

label_massa_giek = tk.Label(root, text="Massa giek:")
label_massa_giek.grid(row=0, column=0)
entry_massa_giek = tk.Entry(root)
entry_massa_giek.grid(row=0, column=1)

label_massa_last = tk.Label(root, text="Massa last:")
label_massa_last.grid(row=1, column=0)
entry_massa_last = tk.Entry(root)
entry_massa_last.grid(row=1, column=1)

label_hoek_A = tk.Label(root, text="Hoek A:")
label_hoek_A.grid(row=2, column=0)
entry_hoek_A = tk.Entry(root)
entry_hoek_A.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Bereken", command=lambda: calculate(entry_massa_giek, entry_massa_last, entry_hoek_A, result_label))
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()



