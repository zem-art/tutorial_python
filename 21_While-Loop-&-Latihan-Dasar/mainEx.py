# Dengan Menggunkan ELSE , BREAK , CONTINUE , PASS
print('\n==Contoh While Menggunakan ELSE , BREAK , CONTINUE , PASS,===\n')

# Menggunkan Else
print('\n==Menggunkan ELSE==')

angka = 0

while angka < 5:
    print('Nilai angka adalah', angka)
    angka += 1  # Di Update
else:  # dengan Menggunkan Else Nilai Akhir Dari While Bisa Kita Ambil
    print("Nilai Akhir Nya Adalah", angka)


# Menggunkan IF

print('\n==Menggunkan IF==')

angka = 0

while angka < 10:
    if angka == 5:
        print('CheckPoint 1')
        break

    print('Nilai angka adalah', angka)
    angka += 1  # Di Update
else:
    print("Nilai Akhir Nya Adalah", angka)

print("Diluar While")

# Menggunkan BREAK

print('\n==Menggunkan Break==')

angka = 0

while angka < 10:
    if angka == 5:
        print('CheckPoint 1')
        break
        print('CheckPoint 2')
    print('Nilai angka adalah', angka)
    angka += 1  # Di Update
else:
    print("Nilai Akhir Nya Adalah", angka)

print("Diluar While")

print('\n==Menggunkan CONTINUE==')

angka = 0

while angka < 10:
    if angka == 5:
        # print('CheckPoint 1')
        angka += 1  # supaya dia tidak menerus di jalankan nya si loop nya
        continue  # dia Akan mengeksekusi yg di atas bukan di bawah nya
        # print('CheckPoint 2')
    print('Nilai angka adalah', angka)
    angka += 1  # Di Update
else:
    print("Nilai Akhir Nya Adalah", angka)

print("Diluar While")

print('\n==Menggunkan PASS==')

angka = 0

while angka < 10:
    if angka == 5:
        print('CheckPoint 1')
        pass  # Akan DI lewatkan Seperti biasanya
        print('CheckPoint 2')
    print('Nilai angka adalah', angka)
    angka += 1  # Di Update
else:
    print("Nilai Akhir Nya Adalah", angka)

print("Diluar While")
