import tkinter as tk
import GoFish as model
from tkinter import *

class GoFish:
    
    def __init__(self, okno):
        self.igra = model.Igra()

        self.obvestilo_rac = tk.Label(okno, text='Računalnik:')
        self.obvestilo_rac.grid(row=0, column=0, sticky=W)

        self.rezultat_racunalnik = tk.Label(okno, text=self.igra.racunalnik.rezultat)
        self.rezultat_racunalnik.grid(row=0, column=1, sticky=W)

        self.racunalnikove_karte = tk.Label(okno, text='stevilo racunalnikovih kart')
        self.racunalnikove_karte.grid(row=1, column=1, sticky=W)

        self.obvestilo_clo = tk.Label(okno, text='Človek:')
        self.obvestilo_clo.grid(row=3, column=0, sticky=W)

        self.rezultat_clovek = tk.Label(okno, text=self.igra.clovek.rezultat)
        self.rezultat_clovek.grid(row=3, column=1, sticky=W)

        self.clovekove_karte = tk.Label(okno, text='clovekove karte')
        self.clovekove_karte.grid(row=4, column=1, columnspan=10, sticky=W)

        tk.Entry(okno, width = 10).grid(row=5, column=1)
        tk.Button(okno, text='Igraj', width=10).grid(row=5, column=2)

        tk.Label(okno, text='kaj naredil clovek').grid(row=6, column=1, sticky=W)
        tk.Label(okno, text='kaj naredil racunalnik').grid(row=7, column=1, sticky=W)

        tk.Button(okno, text='Nova igra', width=10).grid(row=5, column=3)
        


okno = tk.Tk()
okno.title("Go Fish")
igrica = GoFish(okno)
okno.mainloop()
            

