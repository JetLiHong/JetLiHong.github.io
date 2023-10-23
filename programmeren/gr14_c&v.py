import tkinter as tk
import math

def bereken_cirkel_en_vierkanten(radius):

    # Berekeningen voor de cirkel 
    # oppervlak cirkel = (pi*r^2)

    # Berekeningen voor het omsluitende vierkant
    # zijde vierkant = 2*r
    # oppervlak vierkant = zijde vierkant^2

    # Berekeningen voor het ingesloten vierkant
    # zijde omsluitende vierkant = BC = 2*r (voor het gemak 2)
    # zijde ingesloten vierkant = DE
    # middelpunt is A
    # AE is r (voor het gemak 1)
    # AC (antwoord door Pythagoras = wortel 2)
    # DE = (AE*BC)/AC = wortel 2

    cirkel_oppervlak = math.pi * radius**2
    omsluitend_vierkant_zijde = 2 * radius
    omsluitend_vierkant_oppervlak = omsluitend_vierkant_zijde**2
    ingesloten_vierkant_zijde = radius * math.sqrt(2)
    ingesloten_vierkant_oppervlak = ingesloten_vierkant_zijde**2

    return cirkel_oppervlak, omsluitend_vierkant_zijde, omsluitend_vierkant_oppervlak, ingesloten_vierkant_zijde, ingesloten_vierkant_oppervlak

def buttonCallback():
    try:
        radius = float(inputwaarde.get())
        cirkel_oppervlak, omsluitend_vierkant_zijde, omsluitend_vierkant_oppervlak, ingesloten_vierkant_zijde, ingesloten_vierkant_oppervlak = bereken_cirkel_en_vierkanten(
            radius)

        label_4.config(
            text=f"Oppervlak van de cirkel: {cirkel_oppervlak:.2f}\nAfmetingen van het omsluitende vierkant: Zijde = {omsluitend_vierkant_zijde:.2f}, Oppervlak = {omsluitend_vierkant_oppervlak:.2f}\nAfmetingen van het ingesloten vierkant: Zijde = {ingesloten_vierkant_zijde:.2f}, Oppervlak = {ingesloten_vierkant_oppervlak:.2f}")
    except ValueError:
        label_4.config(text="Fout in invoer: Voer een geldig getal in voor de straal.")

root = tk.Tk()
root.title("cirkel en vierkant")
root.geometry("600x250")

waarde_string = tk.StringVar(value="0.0")
label0 = tk.Label(root, text="radius")
label0.grid(row=3, column=0)

inputwaarde = tk.Entry(root, textvariable=waarde_string)  # getalinvoerveld
inputwaarde.grid(row=3, column=1)

label = tk.Label(root, text="Bereken de oppervlakte van de cirkel")
label.grid(row=7, column=0, columnspan=3)

label2 = tk.Label(root, text="Bereken de afmetingen en oppervlakte van het omsluitende vierkant")
label2.grid(row=8, column=0, columnspan=3)
label3 = tk.Label(root, text="Bereken de afmetingen en oppervlakte van het ingesloten vierkant")
label3.grid(row=9, column=0, columnspan=3)

button = tk.Button(root, text="Bereken", command=buttonCallback)
button.grid(row=10, column=0, columnspan=4)  


# Uitvoerveld
label_4 = tk.Label(root, text="")
label_5 = tk.Label(root, text="")

label_4.grid(row=4, column=1)
label_5.grid(row=5, column=1)

root.mainloop()

