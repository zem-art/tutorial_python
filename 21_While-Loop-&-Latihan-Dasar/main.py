# BELAJAR WHILE LOOP
print('===BELAJAR WHILE LOOP\n')

# while argument
# Statement

print('\n==Menggunkan Syarat==')

angka = 0

while angka < 5:
    print('Nilai angka adalah', angka)
    angka = angka + 1  # Di Update

print('Diluar while')
print('\nMenggunkan BOLLEAN')

start = True
angka = 0

while start:
    print('Sedang Mencari Angka ', angka)
    if angka == 100:
        start = False
        print("Angka Ditemukan yang Ke", angka)
    angka += 1  # Belum Di Update
