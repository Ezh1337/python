import random
#import random biblioteket
dice1 = 1
dice2 = 6
#Lag 1 variabel terning kan ha
#lag siste variabel terning kan ha
def dice_throw():
    #Lage en funksjon som velger en random tall mellom variabel 1 og 2
    return random.randint(dice1, dice2)
    #Lag en varibel resultat, og gi den tall 0, for start
result = 0
#Hvis result er ikke 6, så kaster terning vi igjen
while result != 6:
    result = dice_throw()
    #Skrive ut midlertidig resultat
    print(f"Resultat: {result}")
#Gratulere en gambler
print("Her er en sekser")

    