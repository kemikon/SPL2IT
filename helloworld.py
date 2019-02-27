'''names = ["ostap", "peter", "robert", "clarissa", "Magdalena", "Nicolas", "Lukas"]
for name in names:
    print(name)

def nameFunk (fname):
    print(fname + " is your name")

nameFunk("Ostap ")
nameFunk("Filipenko")'''

class Ostap:
    def __init__(self, age, height, weight, school):
        self.age = age
        self.height = height
        self.weight = weight
        self.school = school

    def theMessage(self):
        print("my age is : " , self.age)
    	print("my height is : " , self.height)
        print("my wight is : " ,self.weight)
        print("I attend : " + self.school)

o = Ostap(15,170,65, "HTL-Leoben")
print("Your Name is Ostap")
o.theMessage()