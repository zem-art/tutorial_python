# Belajar Menggunkan Init

print("\n===Belajar Menggunkan Init==\n")


class mahasiswa():
    # nama = "nama" # Tidak Ada Karna Sudah Di gantikan Oleh init

    # Belajar Menggunkan Init

    def __init__(self, input_Nama, input_No):  # init Adalah Method Yg Pertama Kali Di jalankan
        self.nama = input_Nama
        self.no = input_No

    def belajar(self, kondisi):
        print(self.nama, "Sedang Belajar Mengaji", kondisi)

    def tidur(self):
        print(self.nama, "Tidur Di Kelas")


# ini main Programnya
ucup = mahasiswa("Ucup Saricup", 20)

# Jadi Tingall Di Panggil

print("Nama Saya :", ucup.nama)
print("No Absenya :", ucup.no)
