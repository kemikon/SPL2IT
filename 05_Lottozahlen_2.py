import random

lottozahlen = []
for i in range(1,46):
    lottozahlen.append(i)

gezogeneZahlen = []
random.seed()

print("Lottoziehungen:")
tipps = input("welche Zahlen möchten Sie tippen?")
zahlen = tipps.split(",")
zahlen = [int(i) for i in zahlen]

#for i in range(1,7):
#    gezogeneZahlen.append(random.randint(1,45))

#for q in gezogeneZahlen:
#    for w in gezogeneZahlen:
#        if(w == q):
#            gezogeneZahlen.remove(w)
#            gezogeneZahlen.append(random.randint(1,45))

#for z in gezogeneZahlen:
#    for zahlOfLotto in lottozahlen:
#        if(z == zahlOfLotto):
#            lottozahlen.remove(z)

zahlen.sort()
l = 0
while zahlen != gezogeneZahlen:
    l = l+1
    lottozahlen = []
    gezogeneZahlen = []
    for i in range(1,46):
        lottozahlen.append(i)
    for i in range (1,7):
        i = random.randint(0,len(lottozahlen)-1)
        x = lottozahlen.pop(i)
        gezogeneZahlen.append(x)
    
    gezogeneZahlen.sort()
    
    #print(gezogeneZahlen)
    if(zahlen == gezogeneZahlen):
        break


print(gezogeneZahlen)
print(lottozahlen)
print(zahlen)
print(l, "Versuche")


