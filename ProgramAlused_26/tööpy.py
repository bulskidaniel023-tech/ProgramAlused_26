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




