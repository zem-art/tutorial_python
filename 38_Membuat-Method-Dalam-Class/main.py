# Belajar Pengenalan Class Dan Method

print("\n===Pengenalan Class Dan Membuat Method===\n")

# Class nya
# Jgn Lupa python Interpreted language


class mahasiswa():
    nama = "nama"  # atribut : nilai yg Menempel Pda Class

    def belajar(self, kondisi):  # Ini Method
        print(self.nama, "Sedang Belajar Mengaji", kondisi)

# Kenapa Harus Menggunkan Self : Agar Dia Mengetahui data ini milik Class Trsbt

# self Itu mengambil Data dari Class nya

    def tidur(self):
        print(self.nama, "Tidur Di Kelas")


# ini main Programnya
ucup = mahasiswa()
asep = mahasiswa()

ucup.nama = "Ucup Saricup"
asep.nama = "Asep Kararasep"

print("Siapa Mahasiswa :", asep.nama)
print("Siapa Mahasiswa :", ucup.nama)


print("\n===Belajar Method===")

# Dia Adalah Menagambil Inputan Dari sini (kondisi)
asep.belajar(",Dia Belajar Dengan Giat")
ucup.tidur()
