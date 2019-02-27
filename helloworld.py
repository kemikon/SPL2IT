'''names = ["ostap", "peter", "robert", "clarissa", "Magdalena", "Nicolas", "Lukas"]
for name in names:
    print(name)

def nameFunk (fname):
    print(fname + " is your name")

nameFunk("Ostap ")
nameFunk("Filipenko")'''

class Ostap:
    def __init__(self, age, height, wight, school):
        self.age = age
        self.height = height
        self.wight = wight
        self.school = school

o = Ostap(15,170,65, "HTL-Leoben")
print(o.age)