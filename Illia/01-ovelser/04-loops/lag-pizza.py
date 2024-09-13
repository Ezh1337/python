# Denne koden skal behandle en pizza-bestilling
print("Her kan vi ta imot pizza bestillinger\n")

# Spørre kunden hvor mange pizzaer h*n skal ha?
# Lagre antall_bestilte pizzaer
antall_bestilte = int(input("Hvor mange pizzaer skal du ha?"))
# Sett antall_lagde pizzer lik 0 
antall_lagd = 0
# Utfør loop om det er flere pizzaer i bestillingen
while antall_lagd < antall_bestilte:
    # Vi lager pizza nummer: ?
    print("dette er pizza nummer", antall_lagd + 1)
    # Lag pizzabunn
    print("vi lager pizzabunn\n")
    # Ha på tomatsaus
    # Ha på sopp
    # Ha på skinke
    # Ha på ost
    # stek i 10 min
    # Sette pizzaen i varmeskap

    # Øk antall_lagde pizzaer med 1
    antall_lagd+=1
# Server alle pizzaene til kunden
print(antall_lagd, "pizzaer blir levert ut")