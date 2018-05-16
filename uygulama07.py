from tkinter import *

anaPencere = Tk()
anaPencere.geometry("791x496")
anaPencere.title("Resim Galerime Hoşgeldiniz.")



def resim1():
    photo = PhotoImage(file="ağaç.png")
    w = Label(anaPencere, image=photo)
    w.photo = photo
    w.place(relx=0.0, rely=0.1)

def resim2():
    photo = PhotoImage(file="güneş.png")
    w = Label(anaPencere, image=photo)
    w.photo = photo
    w.place(relx=0.0,rely=0.1)

def resim3():
    photo = PhotoImage(file="göl.png")
    w = Label(anaPencere, image=photo)
    w.photo = photo
    w.place(relx=0.0,rely=0.1)

def resim4():
    photo = PhotoImage(file="köprü.png")
    w = Label(anaPencere, image=photo)
    w.photo = photo
    w.place(relx=0.0,rely=0.1)

def resim5():
    photo = PhotoImage(file="bayrak.png")
    w = Label(anaPencere, image=photo)
    w.photo = photo
    w.place(relx=0.0,rely=0.1)


buton=Button(anaPencere,text="Ağaç",font="Times 13",command=resim1)
buton.place(relx=0.0,rely=0.0,relheight=0.1,relwidth=0.2)
buton1=Button(anaPencere,text="Güneş",font="Times 13",command=resim2)
buton1.place(relx=0.2,rely=0.0,relheight=0.1,relwidth=0.2)
buton2=Button(anaPencere,text="Göl",font="Times 13",command=resim3)
buton2.place(relx=0.4,rely=0.0,relheight=0.1,relwidth=0.2)
buton3=Button(anaPencere,text="Köprü",font="Times 13",command=resim4)
buton3.place(relx=0.6,rely=0.0,relheight=0.1,relwidth=0.2)
buton4=Button(anaPencere,text="Bayrak",font="Times 13",command=resim5)
buton4.place(relx=0.8,rely=0.0,relheight=0.1,relwidth=0.2)


mainloop()
