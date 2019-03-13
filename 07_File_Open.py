
dateiname = "teste.txt"
try:
    f = open(dateiname, "r")
except FileNotFoundError:
    print("Datei" + dateiname + "nicht gefunden.")

inhalt = f.read()
print(inhalt)
print("ende")