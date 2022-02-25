#1

"""
1.1 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
"""

"""

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4
    def terulet(self):
        return self.oldalhossz ** 2
negyzet = Negyzet(3)
print(f'A négyzet területe: {negyzet.terulet()}, kerülete: {negyzet.kerulet()}')
"""

#---------------------------------------------------------------------

#1.2

"""
1.2 Feladat
Módosítsd az előző programot úgy, hogy a metódus ne a kerület- illetve a területértékkel térjen vissza, hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
"""

"""
class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4
    def terulet(self):
        return self.oldalhossz ** 2
    def informacio(self):
        return f"A négyzet területe: {negyzet.terulet()}, kerülete: {negyzet.kerulet()}"
        
negyzet = Negyzet(3)
print(negyzet.informacio())
"""

#-------------------------------------------------------------------

#1.3
"""
1.3 Feladat
Az 1.1 feladatban meghatározottak szerint készíts egy programot, amely a felhasználótól egymás után bekér négyzetek oldalhosszát egészen addíg, amíg a felhasználó 0 értéket nem ad meg! Ezen adat alapján a program hozzon létre negyzet objektumokat, melyeket egy listában tárol! A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
"""
"""
lista = []
class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def terulet(self):
        return self.oldalhossz ** 2

    def kerulet(self):
        return self.oldalhossz * 4 

while True:
        beker = input('Négyzet oldal hossza: ')
        if beker == "" or beker == str(0):
            break
        lista.append(int(beker))
for i in lista:
    negyzet1 = Negyzet(i)

    print(f"A négyzet kerülete {negyzet1.kerulet()}, a területe {negyzet1.terulet()}")
"""

#---------------------------------------------------------------------------

#2

"""
2. Feladat
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait (név, életkor, nem)! A nevét a felhasználó adja meg, az életkorát és a nemét véletlenszerűen határozza meg a program! Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!
"""
from random import choice, randint

nemek = ['fiu', 'lany']

class Kutyak:
    def __init__(self, nev):
        self.nev = nev
        kor = randint(0,15)
        nem = choice(nemek)
        print(f'A kutya neve:  {self.nev} \nkora: {kor},\nneme: {nem}')

kutya1 = Kutyak('atesz')

#---------------------------------------------------------------------------


    

