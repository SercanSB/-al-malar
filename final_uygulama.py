from tkinter import *
pencere=Tk()
pencere.title("SİMON OYUNU")


birinciKullanıcı=[]
ikinciKullanıcı=[]

seviye=1




def listeYazG():

    birinciKullanıcı.append("green")
    if len(birinciKullanıcı) == seviye:
        disabled()
        enabled2()





def listeyeYazY():
    global seviye
    birinciKullanıcı.append("yellow")
    if len(birinciKullanıcı) == seviye:
        disabled()
        enabled2()




def listeYazB():
    global seviye
    birinciKullanıcı.append("blue")
    if len(birinciKullanıcı) == seviye:
        disabled()
        enabled2()




def listeYazR():
    global seviye
    birinciKullanıcı.append("red")
    if len(birinciKullanıcı) == seviye:
        disabled()
        enabled2()










def listeYazG2():
    global seviye
    ikinciKullanıcı.append("green")
    if birinciKullanıcı == ikinciKullanıcı:
        disabled2()
        enabled()
        birinciKullanıcı.clear()
        ikinciKullanıcı.clear()
        seviye+=1
    if len(birinciKullanıcı)==len(ikinciKullanıcı):
        if birinciKullanıcı!=(ikinciKullanıcı):
            pencere.destroy()
            pencere1 = Tk()
            pencere1.title("Skor Tablosu")
            pencere1.geometry("300x100")
            pencere1.after(3000, pencere1.destroy)
            Label(pencere1, text= "Yanlış yol izlediniz. \n Oyun bitti. \n \n Skor=" + str(seviye-1)).grid(padx=100, pady=25)


def listeYazY2():
    global seviye
    ikinciKullanıcı.append("yellow")
    if birinciKullanıcı == ikinciKullanıcı:
        disabled2()
        enabled()
        birinciKullanıcı.clear()
        ikinciKullanıcı.clear()
        seviye += 1

    if len(birinciKullanıcı)==len(ikinciKullanıcı):
        if birinciKullanıcı!=(ikinciKullanıcı):
            pencere.destroy()
            pencere1 = Tk()
            pencere1.title("Skor Tablosu")
            pencere1.geometry("300x100")
            pencere1.after(3000, pencere1.destroy)
            Label(pencere1, text= "Yanlış yol izlediniz. \n Oyun bitti. \n \n Skor=" + str(seviye-1)).grid(padx=100, pady=25)


def listeYazB2():
    global seviye

    ikinciKullanıcı.append("blue")
    if birinciKullanıcı == ikinciKullanıcı:
        disabled2()
        enabled()
        birinciKullanıcı.clear()
        ikinciKullanıcı.clear()
        seviye += 1

    if len(birinciKullanıcı)==len(ikinciKullanıcı):
        if birinciKullanıcı!=(ikinciKullanıcı):
            pencere.destroy()
            pencere1 = Tk()
            pencere1.title("Skor Tablosu")
            pencere1.geometry("300x100")
            pencere1.after(3000, pencere1.destroy)
            Label(pencere1, text= "Yanlış yol izlediniz. \n Oyun bitti. \n \n Skor=" + str(seviye-1)).grid(padx=100, pady=25)


def listeYazR2():
    global seviye
    ikinciKullanıcı.append("red")
    if birinciKullanıcı == ikinciKullanıcı:
        disabled2()
        enabled()
        birinciKullanıcı.clear()
        ikinciKullanıcı.clear()
        seviye += 1

    if len(birinciKullanıcı)==len(ikinciKullanıcı):
        if birinciKullanıcı!=(ikinciKullanıcı):
            pencere.destroy()
            pencere1 = Tk()
            pencere1.title("Skor Tablosu")
            pencere1.geometry("300x100")
            pencere1.after(3000, pencere1.destroy)
            Label(pencere1, text= "Yanlış yol izlediniz. \n Oyun bitti. \n \n Skor=" + str(seviye-1)).grid(padx=100, pady=25)





# def yazdır():
#     print(birinciKullanıcı)



butonG = Button(pencere, height=10, width=15, bg="green",command=listeYazG)
butonG.grid(row=1, column=0)
butonY=Button(pencere, height=10, width=15,bg="yellow",command=listeyeYazY)
butonY.grid(row=1,column=1)
butonB=Button(pencere,height=10,width=15,bg="blue",command=listeYazB)
butonB.grid(row=2,column=0)
butonR=Button(pencere ,height=10,width=15,bg="red",command=listeYazR)
butonR.grid(row=2,column=1)

butonG2 = Button(pencere, height=10, width=15, bg="green",command=listeYazG2)
butonG2.grid(row=1, column=3)
butonY2=Button(pencere, height=10, width=15,bg="yellow",command=listeYazY2)
butonY2.grid(row=1,column=4)
butonB2=Button(pencere,height=10,width=15,bg="blue",command=listeYazB2)
butonB2.grid(row=2,column=3)
butonR2=Button(pencere ,height=10,width=15,bg="red",command=listeYazR2)
butonR2.grid(row=2,column=4)
labelbos=Label(pencere ,text="VS")
labelbos.grid(row=1,column=2)


def disabled2():
    butonG2["state"] = DISABLED
    butonG2.config(bg="white")
    butonY2["state"] = DISABLED
    butonY2.config(bg="white")
    butonB2["state"] = DISABLED
    butonB2.config(bg="white")
    butonR2["state"] = DISABLED
    butonR2.config(bg="white")


def disabled():
    butonG["state"] = DISABLED
    butonG.config(bg="white")
    butonY["state"] = DISABLED
    butonY.config(bg="white")
    butonB["state"] = DISABLED
    butonB.config(bg="white")
    butonR["state"] = DISABLED
    butonR.config(bg="white")

def enabled():
    butonG["state"] = NORMAL
    butonG.config(bg="green")
    butonY["state"] = NORMAL
    butonY.config(bg="yellow")
    butonB["state"] = NORMAL
    butonB.config(bg="blue")
    butonR["state"] = NORMAL
    butonR.config(bg="red")

def enabled2():
    butonG2["state"] = NORMAL
    butonG2.config(bg="green")
    butonY2["state"] = NORMAL
    butonY2.config(bg="yellow")
    butonB2["state"] = NORMAL
    butonB2.config(bg="blue")
    butonR2["state"] = NORMAL
    butonR2.config(bg="red")

disabled2()


mainloop()
