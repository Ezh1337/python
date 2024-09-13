#imporeter biblioteket random
import random
#Lage 5 terning-variabler
tern1 = 0
tern2 = 0
tern3 = 0
tern4 = 0
tern5 = 0
kaster = 1
#lage en funksjon som simulerer 1 kast
tern1 = random.randint(1,6)
tern2 = random.randint(1,6)
tern3 = random.randint(1,6)
tern4 = random.randint(1,6)
tern5 = random.randint(1,6)
#lage while løkke- sånn at hvis tallene stemmer ikke, det blir en kast til
while tern1 != tern2 or tern1 != tern3 or tern1 !=tern4 or tern1!=tern5:
    tern1 = random.randint(1,6)
    tern2 = random.randint(1,6)
    tern3 = random.randint(1,6)
    tern4 = random.randint(1,6)
    tern5 = random.randint(1,6)
#gjenta kaster
    kaster += 1
    
print("Yatzy: ",tern1,tern2,tern3,tern4, tern5)
print("Kast antall = ", kaster)
#skrive ut yatzy hvis alle 5 ternninger har samme verdi