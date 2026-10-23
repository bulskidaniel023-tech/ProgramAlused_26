#Kirjuta enda esumene programm, mis väljastab käsureale teksti:
# "Tere, maailm!".
#Küsi, kasutaja nimi ja muuda tekst, et ta näeks välja nii:
# "Tere, maailm! Tervitan sind Mati", Kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#"Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana".
#Ülesanne1
print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=input("Sinu, vanus: ")
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana")
except ValueError:
    print("Palun siseta kehtiv number vanuse jaoks")
    # Ülesanne 2
#on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi= "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada?
# Kuidas võiks nende muutujate väärtusi koodis konmtrollida?
# Kirjuta kood tüüpide kontrollimiseks.
vanus=18 #int-täisarv
eesnimi="Jaak" #str-sõne
pikkus=16.5 #float-kümnendmurd/ujukomaarv
kas_käib_koolis=True #bool-tõeväärtus
print(f"Vanus:{vanus}, tüüp :{type(vanus)}")
print(f"Pikkus:{eesnimi}, tüüp: {type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp: {type(pikkus)}")
print(f"Käib koolis:{kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")

#Ülesanne 3
#Kirjuta enda koolis laual olevate kommide arv muutujasse
# (kommide arv on juhuslik)
# Seejärel kuva muutujas olev kommide arv ekraanile kasuta print()
# Küsu kasutajakt sisendit, mitu kommi ta soovibn laualt ära võtta.
# Eemakda soovitud kommide arv laual olevate kommide arvust 
# ja kuva ekraanile, 
# kui palku komme laual nüüd on.
from random import * #randint
kommide_arv=randint(1, 100) #int(input("Kommide arv: "))
kommide_arv=int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
kommid=int(input("Mitu kommi soovid ära võtta? "))
kommide_arv -= kommid
print(f"Laud on nüüd {kommide_arv} kommi.")



