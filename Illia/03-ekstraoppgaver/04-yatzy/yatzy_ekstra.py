#Jobba med Madelen
import random
 
terning1 = 1
terning2 = 2
terning3 = 3
terning4 = 4
terning5 = 5
kast = 0
antallKast = []
antallRunder = int(input("Hvor mange yatzier ønsker du å regne gjennomsnitt av? "))
for i in range(antallRunder):
    kast = 0
    while not (terning1 == terning2 == terning3 == terning4 == terning5): 
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        terning3 = random.randint(1,6)
        terning4 = random.randint(1,6)
        terning5 = random.randint(1,6)
        kast += 1
        print("Kast nummer: ",kast," Terning 1: ",terning1," Terning 2: ",terning2," Terning 3: ",terning3," Terning 4: ",terning4," Terning 5: ",terning5)
    terning1 = 0
    print("Det tok ",kast," for å få yatzy")
    antallKast.append(int(kast))
 
svar = sum(antallKast)/len(antallKast)
svar = round(svar,2)
print("Gjennomsnittlig tok det ",svar," antall kast å få yatzy.")