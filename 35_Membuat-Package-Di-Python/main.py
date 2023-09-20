# Belajar Membuat Package

import math
from sains import fisika, matematika
# apabila modul berada di dalam file maka mengimport modul tersebut seperti di atas

# apabila modul nya banyak maka tinggal di tambahkan (,) setelah modul yg pertama

# from (namaFile) import namaModul,namaModul,namaModul

import sains  # klo kita panggil sprt itu maka dia akan mengeksekusi file __init__.py

from sains import waktu_tempuh  # ini Membaca Dari File __init__.py


print("\n===Belajar Membuat Package===\n")

print("\n===Cara Pertama==")

# Cara Yang Sederhana

kecepatan = fisika.kecepatan(50, 10)
print("Kecepatan Mobil Itu :", kecepatan)

pertambahan = matematika.tambah(20, 40)
print("Hasil Dari :", 20, "+", 40, "=", pertambahan)

print("\n===Cara Kedua===")

# mengimport dari file __init__.py karna dia mengangap file sains sebagai modul

print("Hasil nya : ", sains.kurang(80, 9))
print("Hasil :", sains.tambah(3, 10))
print("Hasil :", sains.waktu_tempuh(40, 7))
print("Hasil :", sains.kecepatan(5, 10))

print("\n===Cara Ketiga===")

# Cara Ketiga Dengan Membuat From namaFile import modul

# print("Hasil Dari 4 + 7 : ", tambah(4, 7))

print("Jarak Dari Kota A Ke Kota B Adalah", waktu_tempuh(20, 13), "Km")

# Membuat Cos Di Python
print("\n===Membuat Cos Di Python===")

print(math.cos(3.14))
