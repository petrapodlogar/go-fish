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
    return vse_karte

def premesaj(karte):
    random.shuffle(karte)

def bo_igralec_prvi():
    igralceva_izbira = input("Grb ali cifra? ")
    met = random.choice(['cifra', 'grb'])
    return igralceva_izbira == met


class Igralec:

    def __init__(self, karte):
        self.igralceve_karte = karte

class Računalnik:

    def __init__(self, karte):
        self.racunalnikove_karte = karte


def razdeli(karte):
    racunalnikove = []
    igralceve = []
#    for _ in range(7):
#        if bo_igralec_prvi() == True:
# najprej deli igralcu
        
