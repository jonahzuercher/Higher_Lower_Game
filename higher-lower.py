import random
import time
import os
from fillWithSpaces import fill

#Zeigt Rekorde an
def rekorde():
    for i in range(100):
        print("\n")
    myFile = open("./data/rekorde.txt")
    myText = myFile.read()
    myFile.close()
        
    print(myText)  

#Schreibt Rekorde
def writeRec(name, rekord):
    myFile = open("./data/rekorde.txt", "a")
    myFile.write("**"+fill.Spaces(name, 28)+"**"+fill.Spaces(rekord,8)+"**\n")
    myFile.write("******************************************\n")
    myFile.close()

#Funktion um Spiel zu starten
def spielen():
    running = True
    #löscht existierendes Rekordfile (sortiert)
    os.remove("./data/rekorde.txt")

    #Erstellt Rekordfile neu (sortiert)    
    myFile = open("./data/rekorde.txt", "w")
    myFile.write("""******************************************
**!----------Rekorde---------!** Punkte **
******************************************\n""")
    myFile.close()
    
    rekord = 0

    #Werte einlesen
    wahl1 = ""
    wahl2 = ""
    myFile = open("./data/higher_lower.txt")
    myText = myFile.readlines()
    myFile.close()

    while running:
        #Zufällige Auswahl von Begriffen mit dazugehörigem Wert wert10 = Wort, wert11 = Zahl
        wert1 = myText[random.randint(0,99)]

        wert1 = wert1.split(":")

        wert2 = myText[random.randint(0,99)]

        wert2 = wert2.split(":")

        #Begriffe
        wert10 = wert1[0]
        wert20 = wert2[0]
        if wert10 == wert20:
            choice()
                
        wert10 = "\""+wert10+"\""
        wert20 = "\""+wert20+"\""

        #Zahlenwerte
        wert11 = wert1[1]
        wert21 = wert2[1]
        #Definitiver Zahlenwert
        wert11 = int(wert11)
        wert21 = int(wert21)

        #Benutzerabfrage
        print("|-----------------------------------|")
        print("|     Was wurde mehr gegoogelt?     |")
        print("|-----------------------------------|")
        print("| (1)",fill.Spaces(wert10, 25),"    |")
        print("|-----------------------------------|")
        print("|",fill.Spaces("oder", 33),"|")
        print("|-----------------------------------|")
        print("| (2)",fill.Spaces(wert20, 25),"    |")
        print("|-----------------------------------|")
        print("|   Bitte wählen sie \"1\" oder \"2\"   |")
        print("------------------------------------|")

        eingabe = 0

        #Eingabe des Benutzers abfragen und abgleichen   
        try:
            eingabe = int(input("Eingabe: "))
            if eingabe == 1 or eingabe == 2:
                pass
            else:
                print("Ihre Eingabe ist ungültig!")
                time.sleep(2)
                for i in range(3):
                    print("\n")
                continue
            
            if eingabe == 1:
                if wert11 > wert21:
                    print("Richtig!   +1P\n\n")
                    rekord += 1
                    time.sleep(0.5)
                elif wert11 == wert21:
                    print("Richtig (Beide Werte gleichgross)   +1P\n\n")
                    rekord += 1
                    time.sleep(0.5)
                else:
                    print("Falsch!")
                    running = False
                    
            if eingabe == 2:
                if wert21 > wert11:
                    print("Richtig!   +1P\n\n")
                    rekord +=1
                    time.sleep(0.5)
                elif wert21 == wert11:
                    print("Richtig (Beide Werte gleichgross)   +1P\n\n")
                    rekord += 1
                    time.sleep(0.5)
                else:
                    print("Falsch!")
                    running = False
                
            

        except ValueError:
            print("Ihre Eingabe ist ungültig!")
            time.sleep(2)
            for i in range(3):
                print("\n")

    print("Rekord = ",rekord,"\n")
    name = input("Geben sie Ihren Namen ein: ")

    #Schreibt Rekord in File(unsortiert)
    myFile = open("./data/rekordfile.txt", "a")
    myFile.write(str(rekord)+","+name+"\n")
    myFile.close()

    #Schreibt Rekord in File (sortiert)
    with open("./data/rekordfile.txt") as textFile:
        lines = [line.split(",") for line in textFile]
        
    lines.sort(reverse=True)

    for i in range(len(lines)):
        name = lines[i][1]
        name = name.replace("\n", "")
        rekord = lines[i][0]
        writeRec(name, rekord)

    #Noch eine Runde?
    nochmal = input("Wollen sie nochmal Spielen?\n (J)a  /  (N)ein: ")

    if nochmal.lower() == "j" or nochmal.lower() == "":
        print("\n\n\n\n")
        spielen()
    else:
        pass
    
    #Rekorde abfragen/anzeigen
    rekordFile = input("Wollen sie die Rekorde sehen?\n (J)a  /  (N)ein: ")

    if rekordFile.lower() == "j" or rekordFile.lower() == "":
        rekorde()
    
    else:
        pass

    beenden = input("\n\nZum Beenden <Enter> drücken!")
    exit()

#Aufruf des Spiels
spielen()
