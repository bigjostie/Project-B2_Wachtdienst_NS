__author__ = 'Team Cor'

import csv
import datetime

monteur_bestand = "gegevens\monteurs.csv"
monteurs_string = []

def bereken_monteur():
    try:
        f = open(monteur_bestand, 'r')
        monteurs = csv.reader(f, delimiter=',')
        print("Geef aan op welke tijd de automaat gemaakt moet worden.")
        print("Alleen de volgende ingave word geaccepteerd: HH:MM (00:00).")
        print("Tevens kan je \"nu\" intypen om de huidige tijd van jouw computer te gebruiken")
        tijd = input("Voer de tijd in:")
        if tijd == "nu":
            tijd = datetime.datetime.now()
            print(tijd)

        for monteur in monteurs:
            monteurs_string.append([monteur[0] + " " + monteur[1], monteur[2], monteur[3], monteur[4], monteur[5], monteur[6], monteur[7], monteur[8]])
    except:
        print("Error!")
bereken_monteur()

for test in monteurs_string:
    print(test)

"""
Er moet nog een functie gescreven worden dat de locaties nu automatisch naar de database/csv bestand gaan en hierin worden opgeslagen.
"""