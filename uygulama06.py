__author__="Sercan BAYTEMÜR"
from tkinter import Tk, Label, Button, LEFT, RIGHT,font, BOTTOM
import random

class kitapSecimi:
    def __init__(self,sayfa):
        self.sayfa=sayfa
        sayfa.title("Kitap Seçimi")


        self.label= Label(sayfa, text="Haftanın Kazananı")
        self.label.pack()

        self.button= Button(sayfa, text="Seç Bakalım!",command=self.button)
        self.button.pack()

        self.cıkıs=Button(sayfa, text="Kapat",command= sayfa.quit)
        self.cıkıs.pack()

    def button(self):
        sınıfListesi=["Ali", "Kemal","Kadir","Leyla","Buse", "Selin","Ahmet"]
        kisiSec=random.choice(sınıfListesi)


        self.button=Label(self.sayfa, text=kisiSec)
        self.button.pack()

root=Tk()
button=kitapSecimi(root)
root.mainloop()