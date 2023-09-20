# Membuat Module / Belajar Module

# Belajar Cara - Cara Memanggil Modul / Stntax Di Fila Lain

import matematika

import matematika as macth

import matematika as m

from matematika import tambah, kurang

from matematika import *  # untuk memanggil semua syntak di file trsbt

# tinggal di tambah kan setelah as t / terserah kita
from matematika import tambah as t
from matematika import kurang as k

print("\n===Membuat Module===\n")

print("\n===Cara-Cara Memanggil Modul Di File Lain===")

print("\n==Cara Pertama==")
# Cara Pertama

matematika.tambah(4, 3)
matematika.kurang(4, 3)

# Cara Ke Dua
print("\n===Cara Ke Dua===")
# Di Tambahkan as macth / m
m.tambah(4, 3)
m.kurang(4, 3)

print("\n==Cara Ke Tiga==")
# Cara Ke Tiga

# menggunakan from import nama fungsi/var/ dll

tambah(4, 5)
kurang(4, 5)  # kalo mau manggil lagi tinggal kasih (,) nama fungsi/ dll

print("\n==Cara Ke Empat==")
# menggunkan * untuk memangil semua nya
# apabila kita mau meanggil semua syntak di file trsbt
tambah(6, 5)
kurang(6, 3)

print("\n==Cara Ke Lima==")
# menggunakan as tapi mirip cara ke 3

t(7, 8)
k(8, 6)
