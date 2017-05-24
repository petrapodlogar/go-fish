import random

class Karta:

    def __init__(self, stevilka, barva):
        self.stevilka = stevilka
        self.barva = barva

    def __str__(self):
        return "({}, {})".format(self.stevilka, self.barva)

    def __repr__(self):
        return "Karta({}, {})".format(self.stevilka, self.barva)


def nov_kup():
    vse_karte = []
    for stevilka in range(2, 11):
        for barva in ['srce', 'kara', 'križ', 'pik']:
            vse_karte.append(Karta(stevilka, barva))
    for barva in ['srce', 'kara', 'križ', 'pik']:
        for i in ['J', 'Q', 'K', 'A']:
            vse_karte.append(Karta(i, barva))
    random.shuffle(vse_karte)
    return vse_karte

def bo_igralec_prvi():
    igralceva_izbira = input("Grb ali cifra? ")
    met = random.choice(['cifra', 'grb'])
    return igralceva_izbira == met

def razdeli(karte):
    racunalnikove = []
    igralceve = []
    for _ in range(7):
        prva_karta = karte.pop()
        druga_karta = karte.pop()
        igralceve.append(prva_karta)
        racunalnikove.append(druga_karta)
    razdeljene = igralceve, racunalnikove
    return razdeljene


KARTE = nov_kup()
RAZDELJENE = razdeli(KARTE)


class Igralec:

    def __init__(self, v_roki=RAZDELJENE[0]):
        self.vse_karte = KARTE
        self.v_roki = v_roki
        self.rezultat = 0

    def __repr__(self):
        return "{}".format(self.v_roki)

    def Preveri_ce_vse_stiri(self):
        ponovitve_stevilk = {}
        for karta in self.v_roki:
            i = karta.stevilka
            if i in ponovitve_stevilk:
                ponovitve_stevilk[i] += 1
            else:
                ponovitve_stevilk[i] = 1
        for stevilka in ponovitve_stevilk:
            if ponovitve_stevilk[stevilka] == 4:
                self.rezultat += 1
                j = 0
                for karta in self.v_roki:
                    i = karta.stevilka
                    if i == stevilka:
                        del self.v_roki[j] # TODO zbriše 2 namesto 4 karte
                    j += 1
        return self.v_roki
                

    #def Kupi_karto(self):
        

        

class Racunalnik:

    def __init__(self, v_roki=RAZDELJENE[1]):
        self.v_roki = v_roki

    def __repr__(self):
        return "{}".format(self.v_roki)

          
        
