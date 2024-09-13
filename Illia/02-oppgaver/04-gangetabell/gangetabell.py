# Velge en tall fra 1 til 10
tall = int(input("Oppgi et tall mellom 1 og 10: "))

# Sjekk om tallet er gyldig (1-10):
if 1 <= tall <= 10:
    #Hvis ja informerer om tall som ganges:
    print(f"Her ser du {tall}-gangen:")
    
     #lager en midlertidig variabel i, som kan være i interval 1- 10 og da kjører vi for løkke :
    for i in range(1, 11):
        #lager en variabel result og ganger det med rangen av i-variablen
        resultat = tall * i
        #skriver ut resultater hver for seg
        print(resultat, end=" \n")
#hvis ikke da ber vi om å velge gyldig tall
else:
    print("Tallet må være mellom 1 og 10!")
