try:
    f = open("test.txt", "r")
except FileNotFoundError:
    print("Datei name.txt nicht gefunden.")