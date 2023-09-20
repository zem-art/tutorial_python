# Tipe Data Tuple 

# Contoh List
Ganjil = [1,3,5,7,9] # Bisa Di Ubah Data nya 

# Contoh Tuple 
Genap = (2,4,6,8,6,10) # Tidak Bisa Di Rubah Data nya

print("Ini Data Tipe : ",type(Ganjil))
print("Ini Data Tipe : ",type(Genap))

Ganjil[2] = 99

print("Data Di Tambahkan : ",Ganjil)

# dir Untuk Mengetahui Tipe Data Apa Aja yg Bisa Kita Akses

# print("Tipe Data Yang Bisa Di Pakai Di List :" ,dir(Ganjil))

# print("Tipe Data Yang Bisa Di Pakai Di Tuple :" ,dir(Genap)) # Cuman ada Count Dan Index Di Tuple

print("\n===Mengetahui Tipe Data Tuple===")
print("Array Genap :",Genap)
print("Ada Berapa Angka No 6 Di Array Genap : " , Genap.
count(6))

print("Array Genap :",Genap)
print("No Berapa Angka 8 Di Array Genap : " , Genap.count(8))