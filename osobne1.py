"""
koment
"""
# input automaticky příjmá vždy string
"""
salku = float(input("Zadej, kolik vypiješ šálků kávy denně \n"))
dni = float(input("Zadej, kolik dní piješ kávu \n"))
vypito = salku * dni
typ = "Presso" + " s mlékem"
# f string si to sám převede na text
print(f"Vypil jsi {vypito} šálků kávy {typ}")
print("Vypil jsi již celkem {0} šálků kávy.".format(vypito))


s = "Toto je pozdrav velkými MALÝMI a hledej"
print(s.find("hledej"))
print(s.endswith("hledej"))
print(s.startswith("Toto"))
print(s.__contains__("pozdrav"))
print(s.index("pozdrav"))
print(s.lower())



# původní string
st = " C++ je [kolikrat] KRÁT lepší! "
print(st)

# chtěné úpravy stringu
st = st.strip().lower().replace("c++", "Python")
print("\nJe Python lepší než C++?")

# ujištění zda je PY lepší
if st.startswith("Python"):
    print(" - Ano ujistil jsem se že je.")
else:
    print(" - Ne bohužel není lepší než C++")

# Výpočet, kolikrát je lepší podle délky řetězce
kolikrat_lepsix3 = len(st) * 3
st = st.replace("[kolikrat]", str(kolikrat_lepsix3))

# výtisk výsledku
print("\n{}".format(st))



cislo1 = float(input("Vlož první číslo: \n"))
cislo2 = float(input("Vlož druhé číslo: \n"))
if cislo1 > cislo2:
    print("První číslo je větší než druhé")
elif cislo1 == cislo2:
    print("Čísla jsou si rovna")
else:
    print("Druhé číslo je větší než první")


retezec = input("Vlož řetězec: \n")
if retezec == retezec.upper():
    print("Zadaný řetězec je velkými písmeny")
else:
    print("Zadaný řetězec není velkými písmeny")



for i in range(10,100,10):
    print(i)

j = 0
while j < 1000:
    print(j)
    j += 10


# from turtle import *


for j in range (1, 11):
    for i in range (1, 11):
        print(f"{i * j}\t", end="")
    print("")


ozvena = "Ozvěna\n"
print(ozvena * 3)

for i in range(1,11):
    print (i)
for i in range(10, 0, -1):
    print (i)


pokracujeme = "ano"
while pokracujeme == "ano":
    print("-----Vítej ve sčítačce------\n")
    cislo1 = input("Zadej první číslo: \n")
    cislo2 = input("Zadej druhé číslo: \n")
    soucet = cislo1 + cislo2
    print(f"Výsledek součtu je: {soucet}")
    print("Chceš zadat další příklad? Napiš \"ano\" ")
    pokracujeme = input()
print("Ok, měj se")

for j in range(1, 9):

    for i in range(1, 9):
        if (j+i) % 2 == 0:
            print("  ", end="")
        else: print("##", end="")
    print("")

# pro trenovani weby:
# coderank.io
# code duel
# code wars


cisla = []
cisla.append(5)  # přidá 5 do pole
cisla.insert(1, 10)  # do indexu 1 vloží číslo 10
cisla.append(3)
print(cisla)

for i in range(len(cisla)):
    cisla[i] = 15  # všude vloží 15

print(cisla)

for cislo in cisla:
    print(cislo)

for i in range(len(cisla)):
    print(i, end=" ")
    print(cisla[i])

s = "Ahoj"
print(s[2])
print(s.split(","))
# ASCII
print(ord("c"))
print(chr(97))

# slovníky 
# ... 
"""

def den_v_tydnu(zadej_den):
    dny_v_tydnu = ["Pondělí", "Úterý",  "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
    # zadej_den = int(input("Zadej den v týdnu pomocí číslice 1-7. \n"))
    den = zadej_den - 1
    print("Zadal jsi: {0}".format(dny_v_tydnu[den]))
den_v_tydnu(5)
"""
    k_otoceni = input("Zadej string k otočení: \n")
    otoceny = k_otoceni[::-1]
    print("Tvůj string pozpátku je: {}".format(otoceny))


platy = input("Zadej platy (odděl je čárkou): ").split(",")
soucet = 0
print(platy)
for plat in platy:
    soucet += int(plat.strip())
prumer = soucet/len(platy)
print(f"Průměr platů je {prumer}")


text = input("Zadejte text: ")
soucet = 0
for i in range(len(text)):
    znak = ord(text[i])
    if (int(znak) >= 48) and (int(znak) <= 57):
        soucet += znak - 48
print("Součet cifer je: " + str(soucet))

"""

def pozdrav(jmeno, vek):
    return(f"Ahoj uživateli {jmeno}!\nJe ti {vek} let.")


# print(pozdrav("Karel", 30))
# print(pozdrav("Jana", 21))

