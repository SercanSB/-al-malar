__author__="Sercan BAYTEMUR"
import random
kelimelik=("elma","armut","çilek","muz","ananas")
seçilenKelime=random.choice(kelimelik)
havuz=[]
arananHarf=0
kalanCan=3
for meyveler in seçilenKelime:
    havuz.append("_")
print(havuz)
while kalanCan > 0:
    girilenHarf=input("Harf Giriniz:")
    i= girilenHarf in seçilenKelime
    if i == False:
        kalanCan -=1
        print("Yanlış harf. Kalan canınız: " + str(kalanCan))
    if kalanCan == 0:
        print('Kaybettiniz. Doğru kelime "{}"'.format(seçilenKelime))

    if girilenHarf in seçilenKelime:
        for meyve in seçilenKelime:
            if seçilenKelime[arananHarf] == girilenHarf:
                havuz[arananHarf] = girilenHarf
            arananHarf += 1
        print(havuz)
        arananHarf=0
    if "_" not in havuz:
        print("Tebrikler kazandınız..")
        break
