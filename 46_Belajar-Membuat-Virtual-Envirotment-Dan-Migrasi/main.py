# Belajar Virtual Environment Dan Migrasi

# Virtual Environment adalah untuk membagi file agar tidak terjadi kesalhan syntax ketika di update dari dependensi pc utama

# Cara masuk Ke Virtual Enverenment nya Adalah "Nama Directori Inverenmant/source bin/activate"
# CAra install Inverenment => sudo apt-get install python3-venv
# Membuat Lokal Virtual Enverenment python3 -m venv "Nama Project nya"
# Contoh  membuat Migrasi "pip3 freeze --local > Namafile.txt"

# CARA MEMBUAT MIGRASI

# 1 copy file txt nya
# taruh di virtualenveretment yg lain
# lalu ketik di terminal "pip3 install -r namafile.txtnya"
# nanti tinggal menunggu semua package selesai di install

import numpy as op

a = op.array([1, 2, 3, 4, 5])
b = op.array([6, 7, 8, 9, 10])

print(a+b)
