# Belajar Function

print('\n===BELAJAR FUNCTION===\n')

# Contoh Menggunkan Function Terus Menerus

# function di python Menggunkan def

# mendefinisikan fungsi
print('\n==Exemple Membuat Function==')


def fungsi():
    print('Ini Adalah Function')


# memanggil function tersebut
fungsi()

# membuat fungsi sederhana
print('\n==Membuat Function Sederhana==')


def suaraayam():
    print('Kukuruyukkk !!!')


def hargaayam():
    suaraayam()
    print('Harga Ayam 1 kg nya 20.000')


hargaayam()

# membuat Function Dengan Menginputkan Argumen
print('\n==Exemple Function Dengan Inputan==')


def panggilan():
    print('Di Jual Di Jual')


def hargatotalayam(kg):
    panggilan()
    harga = 20000
    hargaTotal = kg*harga
    print('Harga ', kg, "Kg , Ayam Adalah", hargaTotal)


hargatotalayam(1)
hargatotalayam(2)
hargatotalayam(6)
hargatotalayam(0.5)
hargatotalayam(10)
# inputan nya di dalam (Sini)
