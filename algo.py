#septi wulandari
#222410102020




import random
list=[]
angka = random.randint(0,100)
kondisi = True
i = 0
while (kondisi) :
    if i < 10:
        peluang = int(input("masukkan angka:"))
        if int (peluang) < int(angka):
            print("angka kamu terlalu kecil,coba lagi...!")
            list.append(angka)
        elif int(angka) >int (angka):
            list.append((angka))
            print("angka kamu terlalu besar, coba lagi..")
        elif int(angka) == int(angka):
            print("selamat angka kamu benar setelah menebak ", len(list),"kali")
            break
    else:
        print("maaf kamu kurang beruntung")
        kondisi = False
    i+=1