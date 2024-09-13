#Lag variabel rik_svar, som teller riktige svar fra brukeren
rik_svar = 0
feil_svar = 0
#skrive ut 1 sprsm
print("Hva heter stedet der vi lærer?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "skole":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1


print("Hva kalles en person som underviser?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "lærer":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hva heter måltidet midt på skoledagen?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "lunsj":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hvilket fag handler om tall?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "matte":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hva kalles et sted hvor man låner bøker?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "bibliotek":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hvilken dag starter skoleuken?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "mandag":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hva kan fjernes med viskelær?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "blyant":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1


print("Hvilken måned starter ofte skoleåret?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "august":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hva heter forsøk etter teori?")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "praksis":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

print("Hva er annet navn for pausen")
#lage en input med mulighet for svar 
svar_fra_bruker = str(input())
#hvis input = riktig svar
if svar_fra_bruker.lower() == "friminutt":
#skrive ut "du hadde rett"
    print("du hadde rett")
    #riksvar forstørre med 1
    rik_svar+=1
 #ellers
else:
#skrive ut "du bomma"
    print("Du bomma")
    feil_svar+=1

#skriv ut antall riktige og feil svar
print("Du hadde : ",rik_svar," riktige svar")
print("Du hadde : ",feil_svar," feil svar")