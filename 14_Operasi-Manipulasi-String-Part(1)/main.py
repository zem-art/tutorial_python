# Operasi Dan Manipulasi String (part _1)

# 1 . menyambung String (Concatenate)

nama_pertama = "Asep"
nama_tengah = "S"
nama_akhir = "Sep"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir

print(nama_lengkap)

# 2. Menghitung Panjang String

panjang = len(nama_lengkap)

print("panjang Dari" + nama_lengkap + " = " + str(panjang))

# 3 . Operator Untuk String

# Mengecek Apakah Ad komponen CHAR atau String di String

d = "T"
status = d in nama_lengkap
print("String " + d + " ada di " + nama_lengkap + str(status))

d = "Asep"
status = d in nama_lengkap
# kompenen CHAR adalah Komponen Yg ad di huruf nya di dalam kata \ kalimat tersebut
print("String " + d + " ada di " + nama_lengkap + str(status))

# memakai komponen NOT In

D = "D"
status = D not in nama_lengkap
print("String " + D + " ada di " + nama_lengkap + str(status))

# Mengulang String

print("wk" * 10)

print(15 * "wk")

# indexing (Memotong Data Dari String \ Mengambilnya)

print("index Ke -0 " + nama_lengkap[0])

print("index Ke -2 " + nama_lengkap[2])

print("index Ke -7 " + nama_lengkap[7])

# kalo Min (ngambil dari Belakang kata)
print("index Ke (-1) " + nama_lengkap[-1])

print("index Ke (-2) " + nama_lengkap[-2])

# mengambil Range
# menggunakan Titik 2 : (Artinya Sampai)
print("index Ke-[0:3] " + nama_lengkap[0:4])

print("index Ke-[3:8] " + nama_lengkap[3:8])

print("index Ke-[0,2,4,6,8,10] " + nama_lengkap[0:10:2])  # dengan ingkermen 2

# item Paling Kecil

print("Paling Kecil :" + min(nama_lengkap))

# item Paling Besar

print("Paling Besar :" + max(nama_lengkap))

# Memanggil Nama ascii Code nya
ascii_code = ord("'")  # ord mangambil 1 chr String

print("ASCII_code untuk space adalah " + str(ascii_code))

data = 117
print("ASCII_code untuk Asccii 117 adalah " + chr(data))  # Chr Untuk Karakter

# operator dalam bentuk Method

data = "otong Surotonng pararotong"

jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))
