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
        for i in [11, 12, 13, 14]:
            vse_karte.append(Karta(i, barva))
    random.shuffle(vse_karte)
    return vse_karte

def bo_igralec_prvi():
    igralceva_izbira = input("Grb ali cifra? ")
    met = random.choice(['cifra', 'grb'])
    return igralceva_izbira == met


class Igra:

    def __init__(self):
        self.karte = nov_kup()
        self.clovek = Igralec(True)
        self.racunalnik = Igralec()
        self.igralci = [self.clovek, self.racunalnik]
        self.na_potezi = 0 # 0 = človek, 1 = računalnik
    
    def razdeli_karte(self):
        print("Delim karte...")
        for _ in range(7):
            self.clovek.daj_karto(self.karte.pop())
            self.racunalnik.daj_karto(self.karte.pop())

    def igraj(self):
        self.razdeli_karte()

        while not self.je_konec():
            print("Na potezi: {}".format(self.na_potezi))
            vsaj_kaksna_karta_je_bila_prenesena = True
            while vsaj_kaksna_karta_je_bila_prenesena:
                print("Tvoje karte: {}".format(self.igralci[self.na_potezi]))
                n = self.povprasaj_po_stevilki()
                vsaj_kaksna_karta_je_bila_prenesena = self.izvedi_prenos_kart(n)
                self.igralci[self.na_potezi].preveri_in_odstrani()
                
            self.na_potezi = 1 - self.na_potezi
                

    def je_konec(self):
        if self.karte == [] and self.clovek.v_roki == [] and self.racunalnik.v_roki == []:
            return True
        else:
            return False

    def povprasaj_po_stevilki(self): # TODO lahko vprasa le po tistih ki jih ima v roki
        # če je na potezi človek, vprašamo, sicer si zmislimo/izberemo
        if self.na_potezi == 0: # človek
            return int(input("Katero število?"))
        else: # računalnik
            return random.randint(1, 14)

    def izvedi_prenos_kart(self, n):
        seznam_kart = self.igralci[1-self.na_potezi].vzemi_karte(n)
        self.igralci[self.na_potezi].daj_karte(seznam_kart)
        print("Prenesle so se karte: {}".format(seznam_kart))
        return seznam_kart != []

class Igralec:

    def __init__(self, je_clovek=False):
        self.v_roki = []
        self.rezultat = 0
        self.je_clovek = je_clovek

    def __repr__(self):
        return "{}".format(self.v_roki)

    def daj_karto(self, karta):
        self.v_roki.append(karta)

    def daj_karte(self, karte):
        for karta in karte:
            self.v_roki.append(karta)

    def vzemi_karte(self, n):
        vzete = []
        st_kart = len(self.v_roki)
        for j in range(st_kart-1, -1, -1):
            karta = self.v_roki[j]
            if karta.stevilka == n:
                vzete.append(karta)
                del self.v_roki[j]
        return vzete

    def preveri_in_odstrani(self):
        # odstrani 4 karte ce ima igralec v roki 4 karte z isto stevilko
        ponovitve_stevilk = {}
        for karta in self.v_roki:
            i = karta.stevilka
            ponovitve_stevilk[i] = 1 + ponovitve_stevilk.get(i, 0)
        for stevilka in ponovitve_stevilk:
            if ponovitve_stevilk[stevilka] == 4:
                print("Odstranili bomo karte s številko: {}".format(stevlika))
                # povečaj rezultat
                self.rezultat += 1
                # odstani te karte
                nov_seznam = []
                for karta in self.v_roki:
                    if karta.stevilka != stevilka:
                        nov_seznam.append(karta)
                self.v_roki = nov_seznam
