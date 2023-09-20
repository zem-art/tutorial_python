# Belajar Input Dan Output

# Membuat File Eksternal

"""
Macam Macam Mode

w = write mode / mode menulis dan menghapus file lama , jika file tidak ada maka akan di buat file baru

r = read mode only / hanya bisa membaca

a = appending mode / menambah data di akhir baris

r+ = write and read mode
"""

# nama file , mode

# Membuat file Text
print("\n===Membuat File txt===")
file = open('data.txt', 'w')

file.write('Ini Adalah Data Text yang Dibuat Pake Python')
file.write('\nIni Baris Ke Dua')
file.write('\nIni Baris Ke Ketiga')
file.write('\nIni Baris Ke Ke Empat')

file.close()
print("\n==Sucsse Membuat===")

# Membaca File Text

file2 = open('data.txt', 'r')

# print(file2.read(10))  # membaca 10 character
print(file2.readline())  # membaca 1 baris


# appending mode / Menabahkan data

file3 = open("data.txt", 'a')

file3.write('\nBaris Ini Adalah Baru')

file3.close()
