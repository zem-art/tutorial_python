# Belajar Tipe Data Set
print("\n===Belajar Tipe Data SET===\n")

# Set === Himpunan , Tidak Punya Urutan

# Salah Satu Contoh Membuat Himpunan / Set

# 1 . Contoh Membuat Set
print("\n==1 . Contoh Membuat Set==")

hantuIndo = {"Tuyul",
             "kuntilanak",
             "Pocong",
             "Sundel Bolong",
             "Nenek Gayung",
             "Jenglot"
             }

hantuIndo.add("Sadako")  # Contoh Set
hantuIndo.add("Nenek Gayung")

print("Data Isi Nya :", hantuIndo)

# 2 . Contoh Membuat Set
print("\n==2 . Contoh Membuat Set==")

makanan = set()

makanan.add("Biskuit")
makanan.add("Roma")
makanan.add("Sosis")
makanan.add(2000)

# method untuk mengurutkan data sorted
# apa bila ingin menambahkan data int jangan di sort/urutkan
# apabila himpunan ingin di ambil maka dia tidak bisa
print("Data Yang sudah Di Tambahkan :", makanan)

# MENGGABUNGKAN SET

print("\n==Menggabungkan Set==")

ganjil = {1, 3, 5, 7, 9, 11}
genap = {2, 4, 6, 8, 10, 12}
prima = {2, 3, 5, 7}

print(ganjil.union(genap))  # menggabungkan menggunakan union
print(ganjil.intersection(prima))  # kebalikan dari Irisan / intersecsion
