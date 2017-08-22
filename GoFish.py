import random

KARA, SRCE, KRIŽ, PIK = 'kara', 'srce', 'križ', 'pik'



class Karta:

    def __init__(self, stevilka, barva):
        self.stevilka = stevilka
        self.barva = barva

    def __str__(self):
        return "({}, {})".format(self.stevilka, self.barva)

    def __repr__(self):
        return "Karta({}, {})".format(self.stevilka, self.barva)

    def __lt__(self, other):
        return self.stevilka < other.stevilka

    def barva_karte(self):
        if self.barva == SRCE:
            return '♥'
        elif self.barva == KARA:
            return '♦'
        elif self.barva == PIK:
            return '♠'
        elif self.barva == KRIŽ:
            return '♣'

    def stevilka_karte(self):
        if self.stevilka < 11:
            return str(self.stevilka)
        else:
            ime = ['J', 'Q', 'K', 'A']
            return ime[self.stevilka - 11]



def nov_kup():
    vse_karte = []
    for stevilka in range(2, 15):
        for barva in [SRCE, KARA, KRIŽ, PIK]:
            vse_karte.append(Karta(stevilka, barva))
    random.shuffle(vse_karte)
    return vse_karte



class Igra:

    def __init__(self):
        self.karte = nov_kup()
        self.clovek = Igralec(True)
        self.racunalnik = Igralec()
        self.igralci = [self.clovek, self.racunalnik]
        self.na_potezi = 0 # 0 = človek, 1 = računalnik
        self.zadnje_prenesene = []


    def razdeli_karte(self):
        for _ in range(7):
            self.clovek.daj_karto(self.karte.pop())
            self.racunalnik.daj_karto(self.karte.pop())


    def prikazi_karte(self, karte):
        zadnja_karta = None
        text = ''
        for karta in karte:
            if zadnja_karta == None or zadnja_karta.stevilka != karta.stevilka:
                if text != '':
                    text += '] '
                text += '[' + karta.stevilka_karte() + ' '
                text += karta.barva_karte()
            else:
                text += karta.barva_karte()     
            zadnja_karta = karta
        if text != '':
            text += ']'
        return text
                    

    def en_korak(self, klicana_karta):
        vsaj_kaksna_karta_je_bila_prenesena = self.izvedi_prenos_kart(klicana_karta)
        self.igralci[self.na_potezi].preveri_in_odstrani()

        # če nima praznih rok in nasprotnik nima iskane karte, kupi 1, na vrsto pride drugi
        if self.igralci[self.na_potezi].v_roki != []:
            if not vsaj_kaksna_karta_je_bila_prenesena:
                if self.karte != []:
                    self.igralci[self.na_potezi].daj_karto(self.karte.pop())
                    self.igralci[self.na_potezi].preveri_in_odstrani()

        # če nima več kart, jih kupi 7 oz. kolikor jih je še ostalo, na vrsto pride drugi
        if self.igralci[self.na_potezi].v_roki == []:
            vsaj_kaksna_karta_je_bila_prenesena = False
            self.kupi_karte(self.na_potezi)
            self.igralci[self.na_potezi].preveri_in_odstrani()

        if self.igralci[1-self.na_potezi].v_roki == []:
            self.kupi_karte(1 - self.na_potezi)
            self.igralci[1 - self.na_potezi].preveri_in_odstrani()
        
        return vsaj_kaksna_karta_je_bila_prenesena


    def menjava_igralca(self):
        self.igralci[self.na_potezi].preveri_in_odstrani()
        self.na_potezi = 1 - self.na_potezi


    def kupi_karte(self, kateri):
        if self.karte != []:
            # kupi karte, če so še na kupu
            if self.igralci[kateri].v_roki == []:
                # če nima kart, jih vzame 7
                nakup = min(7, len(self.karte))
                for _ in range(nakup):
                    self.igralci[kateri].daj_karto(self.karte.pop())
            else:
                # če ima karte, vzame eno
                self.igralci[kateri].daj_karto(self.karte.pop())
    

    def je_konec(self):
        if self.karte == [] and self.clovek.v_roki == [] and self.racunalnik.v_roki == []:
            return True
        else:
            return False


    def zmagovalec(self):
        if self.racunalnik.rezultat > self.clovek.rezultat:
            return 'računalnik'
        else:
            return 'človek'
        

    def izbira_clovek(self, n):
        ''' Ko je na vrsti človek, si med številkami, ki jih ima v roki, izbere eno. '''
        moznosti = []
        for karta in self.clovek.v_roki:
            stevilka = karta.stevilka
            if stevilka not in moznosti:
                moznosti.append(stevilka)
        return n in moznosti


    def izbira_racunalnik(self):
        ''' Računalnik naključno izbere med številkami, ki jih ima. '''
        moznosti = []
        for karta in self.racunalnik.v_roki:
            stevilka = karta.stevilka
            if stevilka not in moznosti:
                moznosti.append(stevilka)
        return random.choice(moznosti)


    def izvedi_prenos_kart(self, n):
        self.zadnje_prenesene = seznam_kart = self.igralci[1-self.na_potezi].vzemi_karte(n)
        for karta in seznam_kart:
            self.igralci[self.na_potezi].daj_karto(karta)
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
        ''' Odstrani 4 karte, če ima igralec v roki 4 karte z isto številko. '''
        ponovitve_stevilk = {}
        for karta in self.v_roki:
            i = karta.stevilka
            ponovitve_stevilk[i] = 1 + ponovitve_stevilk.get(i, 0)
        for stevilka in ponovitve_stevilk:
            if ponovitve_stevilk[stevilka] == 4:
                self.rezultat += 1
                # odstani te karte
                nov_seznam = []
                for karta in self.v_roki:
                    if karta.stevilka != stevilka:
                        nov_seznam.append(karta)
                self.v_roki = nov_seznam
