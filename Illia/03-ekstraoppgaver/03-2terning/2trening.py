import random

# Start- og sluttverdi for terningene
tall = 1
tall1 = 6

# Funksjon som simulerer å kaste to terninger
def roll():
    return random.randint(tall, tall1), random.randint(tall, tall1)

# Funksjon som teller antall kast til vi får to like terninger
def to_both():
    dice1, dice2 = roll() 
    count = 1
    
    # Hvis terningene ikke er like, fortsett å kaste
    while dice1 != dice2:
        print(f"Kast {count}: Terning 1 = {dice1}, Terning 2 = {dice2}")
        dice1, dice2 = roll()
        count += 1

    # Skriver ut det siste kastet som resulterer i to like terninger
    print(f"Kast {count}: Terning 1 = {dice1}, Terning 2 = {dice2}")
    print("Gratulerer, du fikk to like terninger!")
    return count

# Kjør funksjonen hvis scriptet blir kjørt direkte
if __name__ == "__main__":
    to_both()
