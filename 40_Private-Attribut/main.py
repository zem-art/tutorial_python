# Belajar Private Attribut

print("\n===Belajar Private ==\n")


class mahasiswa():

    jurusan = "Teknik Tata Boga"

    __nilai = 0  # Private Atribut menggunkana (__)

    def __init__(self, input_Nama, input_No):
        self.nama = input_Nama  # Public
        self.no = input_No  # Public
        # self.__nilai = 0

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, "Anda Tidak Lulus")
        else:
            print(self.nama, "Anda Lulus")


# ini main Programnya
ucup = mahasiswa("Ucup Saricup", 123939780)
mujahid = mahasiswa("Mujahid khun", 103282449)
ucup.uts(20)
ucup.uas(40)
mujahid.uts(10)
mujahid.uas(30)
ucup.check_status()
mujahid.check_status()
