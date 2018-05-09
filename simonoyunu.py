from tkinter import *
import random
import time

pencere=Tk()
etiket=pencere.title("Simon Oyunu")

liste=[]
liste1=[]

def doldur1():
    liste1.append("green")

def doldur2():
    liste1.append("yellow")

def doldur3():
    liste1.append("blue")

def doldur4():
    liste1.append("red")



def yazdırListe():
    aa=print(liste)

def yazdırListe1():
    aa=print(liste1)




buton1 = Button(pencere, text="1", height=10, width=15, bg="green", activebackground="green", command=doldur1)
buton1.grid(row=1, column=0)

buton2=Button(pencere,text="2", height=10, width=15,bg="yellow", activebackground="yellow",command=doldur2)
buton2.grid(row=1,column=1)

buton3=Button(pencere,text="3",height=10,width=15,bg="blue",command=doldur3)
buton3.grid(row=2,column=0)

buton4=Button(pencere,text="4",height=10,width=15,bg="red",command=doldur4)
buton4.grid(row=2,column=1)
i=0
def green():

    buton1.configure(bg="white")
    buton1.after(100, lambda: buton1.configure(bg="green"))
    pencere.update()
    time.sleep(1)
    buton1.configure(bg="green")
    pencere.update()
    time.sleep(1)
    i = 0

def yellow():

    buton2.configure(bg="white")
    buton2.after(100, lambda: buton2.configure(bg="yellow"))
    pencere.update()
    time.sleep(1)
    buton2.configure(bg="yellow")
    pencere.update()
    time.sleep(1)

    i = 0

def blue():

    buton3.configure(bg="white")
    buton3.after(100, lambda: buton3.configure(bg="blue"))
    pencere.update()
    time.sleep(1)
    buton3.configure(bg="blue")
    pencere.update()
    time.sleep(1)
    i = 0

def red():

    buton4.configure(bg="white")
    buton4.after(100, lambda: buton4.configure(bg="red"))
    pencere.update()
    time.sleep(1)
    buton4.configure(bg="red")
    pencere.update()
    time.sleep(1)
    i = 0






def göster():

    for i in liste:
        if "red" in liste:
            red()
            break
        if "blue" in liste:
            blue()
            break
        if "yellow" in liste:
            yellow()
            break
        if "green" in liste:
            green()
            break

    





        else:
            print("hata")




liste2=["red","blue","yellow","green"]

def secimYap():
    x=random.choice(liste2)
    liste.append(x)
    return

sayı=1
def başla():
    global sayı

    liste.clear()
    liste1.clear()
    if sayı==1:
        secimYap()
        göster()
        sayı+=1




    elif sayı ==2:
        secimYap()
        göster()
        secimYap()
        göster()
        sayı += 1

    elif sayı==3:
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()

        sayı += 1

    elif sayı==4:
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        sayı += 1

    elif sayı==5:
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        sayı +=1

    elif sayı==5:
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        secimYap()
        göster()
        sayı +=1

    else:
        print("hata")

    print(liste)





def kontrol():
    if liste1==liste:
        print("tebrikler")

    else:
        print("yanlış secim")

buton5=Button(pencere,text="Oyuna Başla",command=başla)
buton5.grid(row=3,column=0)
buton7=Button(pencere,text="Kontrol Et",command=kontrol)
buton7.grid(row=3,column=1)


mainloop()