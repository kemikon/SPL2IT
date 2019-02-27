import random

anzahl = input("Wie oft soll ich für dich würfeln?")
anzahlAsInt = int(anzahl)
max = anzahlAsInt+1
theNumbers = []
gesetzteZahll = input("Auf welche Zahl setzen Sie?")
gesetzteZahl = int(gesetzteZahll)
anzahlDerZahl = 0

for zahl in range(1,max):
    random.seed
    theNumbers.append(random.randint(1,6))

for number in theNumbers:
    if(gesetzteZahl == number):
        anzahlDerZahl = anzahlDerZahl+1

if(anzahlDerZahl == 0):
    print("Sie haben Verloren")
    print(theNumbers)
else:
    print(theNumbers)
    print("Ihre Zahl kommt " , anzahlDerZahl , " mal vor. Das heisst Sie haben gewonnen")