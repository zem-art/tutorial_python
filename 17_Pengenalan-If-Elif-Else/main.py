# Belajar If Else

print("==Belajar If Else==\n")
nilai1 = 75
nilai2 = 80
nilai3 = 50
# kalo Di Python

if nilai1 == 75:  # equal eksplist
    print("nilai Anda : ", nilai1)
    print("Step 1")

if nilai2 is 80:  # equal
    print("nilai Anda :", nilai2)
    print("Step 2")


if nilai3 is not 60:  # Not Equal
    print("nilai Anda :", nilai3)


print("\n==If-Else==\n")

nilai = 50
print("nilai Defaultnya", nilai, "\n")

if 80 <= nilai <= 100:
    print("Nilai Anda Adalah A")
elif 70 <= nilai < 80:
    print("nilai Anda adalah B")
elif 60 <= nilai < 70:
    print("nilai Anda adalah C")  # elif Adalah syntax Else if
elif 50 <= nilai < 60:
    print("Nilai Anda Adalah T , Lakukan Perbaikan")
else:
    print("Maaf Anda Tidak Lulus Mata Kuliah")


print("\n==Operator List Dan String===\n")

gorengan = ["bakwan", "Cireng", "Bala-Bala", "Gehu",
            "Combro", "Pisang-Goreng", "Pukis", "Risoles"]

beli = "Sepatu"

if beli in gorengan:
    print('Mamang Bilang ", ya saya jual', beli, "'")
if not beli in gorengan:
    print("Maaf Mamang Engg Jual ", beli, "'")  # sama Saja Kaya Else


# Cek Karakter Di Dalam String / Variabel trsbt
print("\n==Cek Karakter==")
karakter = "k"
if karakter in beli:
    print("ada Huruf", karakter, "di", beli)
else:
    print("maaf engga ada Huruf", karakter, "di", beli)
