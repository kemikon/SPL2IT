import random

lottozahlen = []
for i in range(1,46):
    lottozahlen.append(i)

gezogeneZahlen = []
random.seed()
#for i in range(1,7):
#    gezogeneZahlen.append(random.randint(1,45))

#for q in gezogeneZahlen:
#    for w in gezogeneZahlen:
#        if(w == q):
#            gezogeneZahlen.remove(w)
#            gezogeneZahlen.append(random.randint(1,45))

for i in range (1,7):
    i = random.randint(0,len(lottozahlen)-1)
    x = lottozahlen.pop(i)
    gezogeneZahlen.append(x)
    


#for z in gezogeneZahlen:
#    for zahlOfLotto in lottozahlen:
#        if(z == zahlOfLotto):
#            lottozahlen.remove(z)
        
gezogeneZahlen.sort()
print(gezogeneZahlen)
print(lottozahlen)