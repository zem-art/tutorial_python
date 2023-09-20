# Belajar Function Argument
print('\n===BELAJAR FUNCTION & ARGUMENT===\n')

# funsi dengan Menggunkan argument sederhana

print('\n==Fungsi Sederhana==')


def siswa(nama):  # fungsi nya
    print("Siswa Ini Bernama : ", nama)


siswa('Asep')  # ini Argument Nya

# fungsi dengan menggunkan KEYWORD ARGUMENT
print("\n===Fungsi Dari Keyword Argument===")


def guru(nama, pelajaran):
    print('Guru Ini Bernama : ', nama)
    print('Mengajar : ', pelajaran)


# contoh kalo list nya panjang maka di panggil nya begini
guru(nama='Joni', pelajaran='PKN')

guru(pelajaran="Olah Raga", nama="Endang")  # Tidak Berurutan nya

guru('Raihan', 'IPS')  # Ini Contoh yang Salah


# fungsi Menggunkan DEFAULTY nya
print('\n==Menggunkan Fungsi Dari Defaulty nya==')


def penjagaSekolah(nama, shift='siang', sifat='galak'):
    print('Satpam Ini Bernama : ', nama)
    print('Mengajar : ', shift)
    print('Sifat : ', sifat)


penjagaSekolah(nama="Udin")
penjagaSekolah('maman', shift='Malam')
penjagaSekolah("Asep", sifat="Baik")

# Contoh Penulisan Yg Salah Karna Nama Tidak Di Isi / Argumenya

# penjagaSekolah(shift="Malam", sifat="Galak Banget")
