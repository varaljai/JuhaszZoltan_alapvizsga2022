#1 feladat:
print("1. feladat:")

l = []
karakterlanc = input("adj megy egy tetszöleges szót nagybetüvel! ")
szam = int(input("adj meg egy számot! "))
szamsor = szam**2
while True:
    if szamsor >= 0:
        szamsor = szamsor -1
        l.append(karakterlanc)
    else:
        break
a = [x.lower() for x in l]
print("    ",*a)


#2 feladat:
print("2. feladat:")

import math


a = szam = float(input("add meg a háromszög a odlalát törtszámban!"))
b = szam = float(input("add meg b háromszög a odlalát törtszámban!"))
c = szam = float(input("add meg c háromszög a odlalát törtszámban!"))

kerulet = a + b + c
p = a**2 / c
q = b**2 / c
m = math.sqrt(q * p)
terulet = a * m / 2

if a + b > c:
    print(f"     Nem létezik a háromszög")
    print(f"     kerület : {kerület} ")
    
elif a == b or a == c or c == b  :
    print(f"     Egyenlő szárú háromszög")
    print(f"     kerület: {kerulet},terület: {terulet} ")
    
elif a**2 + b**2 < c**2:
    print(f"     derékszögü háromszög.")
    print(f"     kerület: {kerulet},terület: {terulet} ")

#3. feladat:
print("3. feladat: ")
class Bolygok:
    def __init__(self, sor):
        neve, holdak, terfogat = sor.strip().split(';')
        self.neve = neve
        self.holdak  = holdak
        self.terfogat = terfogat
       
with open("solsys.txt", encoding="UTF-8") as f:
    l = [ Bolygok(sor) for sor in f ]
    
#(3.1) feladat:
print(f"     3.1: {len(l)} bolygó van a naprendszerben")

#(3.2) feladat:
holdai = [int(sor.holdak) for sor in l ]
atlag = sum(holdai) / len(l)
print(f"     3.2: a napredszerben egy bolygónak átlagosan {atlag} holdja van")

#(3.3) feladat:
terfogatai = [float(sor.terfogat) for sor in l]
maxterfogat = max(terfogatai)
vizsgalat = [sor.neve for sor in l if float(sor.terfogat) == maxterfogat]
print(f"     3.3: A legnagyobb térfogatú bolygó a {vizsgalat}.")

#(3.4) feladat:
nev = input("     3.4: Írd le a kereset bolygó nevét: ")
kereses = [sor.neve for sor in l if nev == sor.neve]
valasz = "          van ilyen nevű bolygó" if kereses else "          sajnos nincs ilyen bolygó a naprendszerben"
print(valasz)

#(3.5) feladat:
szam = int(input("    3.5: írj be egy egész számot: "))
bolygok = [sor.neve for sor in l if szam < int(sor.holdak)]
print(f"          a következő bolygonak van {szam}-nál/nél több holdja:")
print("        ",bolygok)




