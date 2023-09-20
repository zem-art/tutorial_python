# Belajar For LOOP

print("==Belajar Foor Loop==\n")

# List Sebagai Iterable
print("\n==List Sebagai Iterable==\n")
gorengan = ["bakwan", "cireng", "tahu-isi", "tempe", "ubi goreng"]


# in : didalam
for g in gorengan:
    print(g)  # g mengambil component dari array
    print(len(g))  # hitung panjang dari setiap element nya

# String Sebagai Iterable
print("\n==String Sebagai Iterable==\n")

bakwan = "Bakwan"

for i in bakwan:
    print(i)  # Di Eja Sitiap huruf nya dan di Print

# For di dalam For

print("\n==For Dalam For==\n")

buah = ["semangka", "jeruk", "apel", "anggur"]
sayur = ["kangkung", "wortel", "tomat", "kentang"]

Daftar_belanja = [gorengan, buah, sayur]  # ini Layer 1

# print(Daftar_belanja)

for subDaftarBelanja in Daftar_belanja:  # subdaftarbelanja mengambil Dari daftar belanja
    # mengambil List Layer 1
    print('Ini Dari Daftar_belanja', subDaftarBelanja)
    for komponen in subDaftarBelanja:  # komponen Mengambil data dari subdaftarbelanja
        print('=>', komponen)
