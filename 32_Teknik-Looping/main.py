# Belajar Teknik Looping
print("\n===Teknik Looping===\n")

nama_band = ["Payung Teduh",
             "Fourtny",
             "Dialog Dini Hari",
             "Mr Sonjana",
             "Parahyana",
             "Maron 5"
             ]

kumpulan_lagu = ["Daun",
                 "Kemarau",
                 "Akad",
                 "Zona Nyaman",
                 "Rumahku",
                 "Sugar"
                 ]
# Cara Yang kurang Efektif Untuk Melooping
print("\n===Teknik Looping Yang Kurang Efektif===")

iterasi = 0
for band in nama_band:
    print('No :', iterasi, "Nama Band :", band)
    iterasi += 1

# Pakai Enumered Untuk Melooping Di Python

# pakai enumerate otomatis akan menghitung index dan nilai ny

# nama Otong & Saepul Terserah Tidak Harus Sama
print("\n===Contoh Menggunkan Enumered===")

for index, band in enumerate(nama_band):
    print(index, "Nama Band :", band)

# Zip : Menggabungkan List
print("\n===Contoh Menggunkan Zip===")

for band, lagu in zip(nama_band, kumpulan_lagu):
    print(band, "Menyayikan Lagu Yang Berjudul :", lagu)

# Apabila Tuple sama List Bisa di Iterebels (Di Pasangkan Data nya )

print("\n==Tipe Data Set Di Iterebels==")

nama_kucing = {"Ucil",
               "Lulu",
               "Loli",
               "Jaki",
               "Oren",
               "Black",
               "Putih"
               }

# Untuk Set
print("\n==Bagian Set==")
for jenis in sorted(nama_kucing):
    print("Nama Kucing :", jenis)

print("\n===Bagian Dictonory===")

namakucing2 = {"Ucil": "Galak",
               "Lulu": "Galak",
               "Loli": "Baik",
               "Jaki": "Jahat",
               "Oren": "Pemalas",
               "Black": "Cuby",
               "Putih": "Manis",
               }

# items : mengambil semua data :
# values : Mengambil value data : (yang di belakan keys)
# keys : Mengambil Keys data : (yang di depan values)
for i, v in namakucing2.items():
    print(i, "Sifat Nya :", v)  # mirip mirip Zip menggabungkan 2 data

# for i in reversed(range(1, 10, 1)):
#     print(i)
