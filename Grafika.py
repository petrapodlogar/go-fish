import tkinter as tk
import GoFish as model
from tkinter import *

class GoFish:
    
    def __init__(self, okno):
        self.igra = model.Igra()

        tk.Label(okno, text='Računalnik:').grid(row=0, column=0, sticky=W)

        self.rezultat_racunalnik = tk.Label(okno, text=self.igra.racunalnik.rezultat)
        self.rezultat_racunalnik.grid(row=0, column=1, sticky=W)

        self.racunalnikove_karte = tk.Label(okno, text='število računalnikovih kart')
        self.racunalnikove_karte.grid(row=1, column=1, sticky=W)

        tk.Label(okno, text='Človek:').grid(row=3, column=0, sticky=W)

        self.rezultat_clovek = tk.Label(okno, text=self.igra.clovek.rezultat)
        self.rezultat_clovek.grid(row=3, column=1, sticky=W)

        self.clovekove_karte = tk.Label(okno, text='človekove karte')
        self.clovekove_karte.grid(row=4, column=1, columnspan=50, sticky=W)

        tk.Label(okno, text='Ostale karte:').grid(row=5, column=0, sticky=W)

        self.preostale_karte = tk.Label(okno, text='')
        self.preostale_karte.grid(row=5, column=1, sticky=W)

        tk.Label(okno, text='').grid(row=6)

        tk.Label(okno, text='Na potezi:').grid(row=7, column=0, sticky=W)
        self.na_potezi_je = tk.Label(okno, text='ČLOVEK')
        self.na_potezi_je.grid(row=7, column=1, sticky=W)

        self.entry = tk.Entry(okno, width = 10)
        self.entry.grid(row=8, column=1)
        self.za_igro = tk.Button(okno, text='Igraj', command=self.en_korak, width=10)
        self.za_igro.grid(row=8, column=2)
        #self.nova = tk.Button(okno, text='Nova igra', command=self.nova_igra, width=10)
        #self.nova.grid(row=8, column=3)

        self.status = tk.Label(okno, text='')
        self.status.grid(row=9, column=1, sticky=W, columnspan=20)

        self.igra.razdeli_karte()

        
        menubar = tk.Menu(okno)

        igra_menu = Menu(menubar, tearoff=0)
        igra_menu.add_command(label="Nova igra", command=self.nova_igra)
        igra_menu.add_separator()
        igra_menu.add_command(label="Izhod", command=okno.destroy)
        menubar.add_cascade(label="Igra", menu=igra_menu)

        okno.config(menu=menubar)

        okno.minsize(width=550, height=220)

        
        self.obnovi()


    def stevilo_kart(self, n, sklon):
        if n == 1:
            if sklon:
                return '1 karto'
            else:
                return '1 karta'
        elif n == 2:
            return '2 karti'
        elif n in {3, 4}:
            return str(n) + ' karte'
        else:
            return str(n) + ' kart'


    def obnovi(self):
        self.igra.clovek.v_roki.sort()
        self.rezultat_racunalnik.config(text=self.igra.racunalnik.rezultat)
        self.racunalnikove_karte.config(text='Računalnik ima ' + self.stevilo_kart(len(self.igra.racunalnik.v_roki), True) + '.')
        self.rezultat_clovek.config(text=self.igra.clovek.rezultat)
        self.clovekove_karte.config(text=self.igra.prikazi_karte(self.igra.clovek.v_roki))
        self.preostale_karte.config(text=self.stevilo_kart(len(self.igra.karte), False))

        if self.igra.je_konec():
            self.racunalnikove_karte.config(text='')
            self.preostale_karte.config(text='')
            self.na_potezi_je.config(text='')


    def karta_v_stevilko(self, karta):
        ime = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        karta = karta.upper().strip()
        for i in range(len(ime)):
            if ime[i] == karta:
                return i + 2
        return -1

    def stevilka_v_karto(self, stevilka):
        ime = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return ime[stevilka - 2]
        
    def en_korak(self):
        nadaljuj_igro = True

        if self.igra.na_potezi == 0:
            # igra človek
            vnos = self.entry.get().upper()
            self.entry.delete(0, END)
            karta = self.karta_v_stevilko(vnos)
            if karta < 0:
                self.status.config(text='Neveljaven vnos. Vnesi število med 2 in 10, J, Q, K ali A.')
            else:
                if self.igra.izbira_clovek(karta):
                    nadaljuj_igro = self.igra.en_korak(karta)
                    self.status.config(text=self.obnovi_status(karta))
                else:
                    self.status.config(text='Napačen vnos. Izbiraj med števili, ki jih imaš v roki.')

        else:
            # igra računalnik
            karta = self.igra.izbira_racunalnik()
            nadaljuj_igro = self.igra.en_korak(karta)
            self.status.config(text=self.obnovi_status(karta))


        if self.igra.je_konec():
            self.status.config(text='Zmagal je {}.'.format(self.igra.zmagovalec()))
            self.za_igro.config(state='disabled')
            self.entry.delete(0, END)
            self.entry.config(state='disabled')

        else:
            if not nadaljuj_igro:
                self.igra.menjava_igralca()
                
            if self.igra.na_potezi == 1:
                self.entry.config(state='disabled')
                self.na_potezi_je.config(text='RAČUNALNIK')
            else:
                self.entry.config(state='normal')
                self.na_potezi_je.config(text='ČLOVEK')
            
        self.obnovi()


    def nova_igra(self):
        self.igra = model.Igra()
        self.igra.razdeli_karte()
        self.obnovi()
        self.za_igro.config(state='normal')
        self.status.config(text='')
        self.entry.config(state='normal')


    def obnovi_status(self, karta):
        if self.igra.na_potezi == 0:
            text = 'Človek je izbral [{}]'.format(self.stevilka_v_karto(karta))
        else:
            text = 'Računalnik je izbral [{}]'.format(self.stevilka_v_karto(karta))
        if self.igra.zadnje_prenesene == []:
            text += ' in prenesla se ni nobena karta.'
        else:
            prenesene = self.igra.zadnje_prenesene
            prikaz_prenesenih = self.igra.prikazi_karte(prenesene)
            dolzina = len(prenesene)
            if dolzina == 1:
                text += ' in prenesla se je {}'.format(prikaz_prenesenih)
            elif dolzina == 2:
                text += ' in prenesli sta se {}'.format(prikaz_prenesenih)
            else:
                text += ' in prenesle so se {}'.format(prikaz_prenesenih)
        return text
        


okno = tk.Tk()
okno.title("Go Fish")
igrica = GoFish(okno)
okno.mainloop()
            

