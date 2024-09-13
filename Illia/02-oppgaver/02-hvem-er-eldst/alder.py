#Lage en variabel Kari og tilordne den verdi alder, som bruker velger
alder_kari = int(input("Skriv alder til Kari: "))

#Lage en variabel Henrik og tilordne den verdi alder, som bruker velger
alder_henrik = int(input("Skriv alder til Henrik: "))

#Hvis Kari er eldre enn Henrik,så  skrive ut at Kari er eldre
if alder_kari>alder_henrik:
    print("Kari er eldre.")
# Ellers hvis Henrik er eldre enn Kari,så  skrive ut at Kari er eldre
elif alder_henrik > alder_kari:
     print("Henrik er eldre.")
# Ellers skrive ut at de er like gamle
else:
    print("De er like gamle.")

# Lærer: Bra python-kode, Illia!    