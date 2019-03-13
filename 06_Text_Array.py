text = "Diese Mitteilung beschreibt, wie jene Organisation der gewerblichen Wirtschaft, die Ihre personenbezogenen Daten verarbeitet („wir“), diese Verarbeitung als alleiniger Verantwortlicher vornimmt. Um Ihnen eine Orientierung zu erleichtern, sind wesentliche Teile dieser Mitteilung nach dem Kreis der Betroffenen gegliedert. Um sich darüber zu informieren, wie wir Ihre personenbezogenen Daten verarbeiten, lesen Sie daher bitte den bzw. die auf Sie zutreffenden Abschnitt(e) unten."
text = text.replace("!", ".")
text = text.replace("?", ".")
texte = text.split(".")
te = []
for e in texte:
    woerter = e.split(" ")
    te.append(len(woerter))
    print(len(woerter))

for

print(texte)
print(len(texte))
print(te)
