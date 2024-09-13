#lage en array med spørsmål og svar
sporsmal = [
    {"sporsmal": "Hva heter stedet der vi lærer?", "svar": "Skole"},
    {"sporsmal": "Hva kalles en person som underviser?", "svar": "Lærer"},
    {"sporsmal": "Hva heter måltidet midt på skoledagen?", "svar": "Lunsj"},
    {"sporsmal": "Hvilket fag handler om tall?", "svar": "Matte"},
    {"sporsmal": "Hva kalles et sted hvor man låner bøker?", "svar": "Bibliotek"},
    {"sporsmal": "Hvilken dag starter skoleuken?", "svar": "Mandag"},
    {"sporsmal": "Hva bruker vi til å skrive på?", "svar": "Blyant"},
    {"sporsmal": "Hvilken måned starter ofte skoleåret?", "svar": "August"},
    {"sporsmal": "Hva er det motsatte av teori?", "svar": "Praksis"},
    {"sporsmal": "Hva heter pausen midt på dagen?", "svar": "Friminutt"}
]
#lage 2 variabler som teller riktige og feil svarene
rik_svar = 0
feil_svar = 0
#Lage en for løkke for å framvise hver og enkelt sprsm
for i in sporsmal:
    #Lage en varibel som tar imot svarene fra bruker og gjør de om til småtekst
    svar = input(i["sporsmal"] + " ").lower()
    #sjekke om svar som ble inntastet stemmer
    if svar == i["svar"].lower(): 
        #printe ut : du har rett
        print("du hadde rett")
        #forstørre antall riktige svar med 1
        rik_svar += 1
    #ellers (om svaren ikke stemmer)    
    else:
        #printe ut : du bomma
        print("Du bomma")
        #forstørre antall feil svar med 1
        feil_svar += 1
#skriv ut antall riktige og feil svar
print("Du hadde :", rik_svar, "riktige svar")
print("Du hadde :", feil_svar, "feil svar")
