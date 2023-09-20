# Belajar Foor Loop Range Dan Break

# Range untuk membuat list

for i in range(10, 40, 5):  # membuat kelipat dari nilai 5
    print('nilai i :', i)

print('\n===For Excemple===')

for i in range(0, 5):
    print(i)
else:
    print("hallo")


print('\n====Menggunakan If ====')

number = 10

for i in range(0, 20):
    print('nilai : ', i)
    if i == number:  # mengecek apakah angkanya sudah sama dengan yg di var number
        print('Angka Di temukan : ', i)
# dan ini masih terjadi perulangan walupun var nya sama

print('\n====Menggunakan Break====')
# Break Untuk Menghentikan For loop Dan Dia Akan Keluar dari For Loop

number = 10

for i in range(0, 15):
    print('nilai : ', i)

    if i == number:  # mengecek apakah angkanya sudah sama dengan yg di var number
        print('Angka Di temukan : ', i)
        break  # akan Keluar dari Perulangan / for


print('\n====Menggunakan For Else ====')
# Else untuk Mengecek Apakah If nya sesuai dengan yg di minta maka tampil kan apabila tidak maka akan menampilkan else
number = 20

for i in range(0, 10):
    print('nilai : ', i)

    if i == number:  # mengecek apakah angkanya sudah sama dengan yg di var number
        print('Angka Di temukan : ', i)
        break  # akan Keluar dari Perulangan / for
else:
    print('Angka Tidak Di temukan')
