#Belajar More On List
print("\n==MORE ON LIST==\n")

Barang = ["Kunci", "Ember","Ban", "Mobil","Jaket"]

print(Barang)

# Beberapa Method Untuk Digunakan Untuk Manipulasi List

print("\n==Method Yang Di Gunkanan Untuk List==\n")

# Menambah Barang
print("\n==Nambah Barang==")
Barang.append("Sepeda") # Menambah Barang Di Belakang nya

print("Nambah Barang",Barang)

# Contoh Iterebels

data = "Text" # Bentuk Iterebels

# for i in data:
#   print(i)
print(data[1])

print("\n==Bentuk Iterebels==")

Barang.extend("Dompet") # Dalam Bentuk Iterebels
print("Menambah Data Dalam Bentuk Iterebels",Barang)

print("\n==Menambah Kan Data Dari Berbagai Arah")
Barang.insert(3,"Sepeda") # input Dulu No Yang Di Inginkan Lalu Data nya
print("Tambah kan Data Di No 3 :" , Barang)

# Method Untuk Menghitung Anggontanya 
print("\n==Method Untuk Menghitung Kata==")

jumlah = Barang.count("Sepeda")

print("Jumlah Kata Yang Sama Ada : " , jumlah)

#Method Untuk Meremove Data
print("\n==Method Delete Data==")

Barang.remove("Sepeda")

print("Data Yang Sudah Di Hapus Adalah :" , Barang)

#Membalikan Nama Data Tsbt

Barang.reverse()
print('Kata Yang Terbalik Adalah : ', Barang)

print("="*70)

# Cara Membuat Variabel Baru Dan Tidak Merubah Data Asli nya

Stuff = Barang.copy() # Agar Tidak Merubah Data Yang Asli Nya
Stuff.append("Gelas") # Kita Menambah Kan Data Tpi Tidak Merubah Data Yg Asli nya
print('Data Dari Stuff  : ',Stuff)
print("Data DAri Barang : ",Barang)

