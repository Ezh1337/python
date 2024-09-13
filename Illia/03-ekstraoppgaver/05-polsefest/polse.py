#importere math_library
import math

#lage en funksjon, som regner alt sammen med 2 parametre fra brukeren, pølser og mennesker:
def regning(polser, mennesker):
    #finne ut hvor mye pølser skal være til sammen
    total_polser = mennesker * polser
    #finne ut hvor mye pakker med pølser trenger vi
    pakk_med_pols = math.ceil(total_polser/10)
    #finne ut hvor mye pakker med brød trenger vi
    pakk_med_brod = math.ceil(total_polser/8)
    #finne ut hvor mye pølser skal være til overs
    polser_til_overs = pakk_med_pols * 10 - total_polser
    #finne ut hvor mye brød skal være til overs
    brod_til_overs = pakk_med_brod * 8 - total_polser
    #skrive ut antall pakker med pølser, som trenges
    print("Minste antall pakker pølser som kreves:", pakk_med_pols)
    #skrive ut antall pakker med brød, som trenges
    print("Minste antall pakker pølserbrød som kreves:", pakk_med_brod)
    #skrive ut pølser, som er til overs
    print("Antall pølser som blir til overs:", polser_til_overs)
    #skrive ut brød, som er til overs
    print("Antall pølsebrød som blir til overs:", brod_til_overs)
#få antall mennesker fra brukeren og tilordne det til en verdi, som blir en parameter i funksjonen
mennesker= int(input("Hvor mange mennesker skal være på fest: "))
#få antall pølser per person fra brukeren og tilordne det til en verdi, som blir en parameter i funksjonen
polser = int(input("Hvor mange pølser skal være til 1 pers på fest: "))
#kjøre en funksjon
regning(polser,mennesker)
