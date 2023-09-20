# Belajar Class Variabel

print("\n==Belajar Variabel==\n")


class mahasiswa():

    jurusan = "Ekonomi"

    jumlah_mahasiswa = 0

    def __init__(self, input_Nama, input_No):
        self.nama = input_Nama  # Public
        self.no = input_No  # Public

        # membuat jumlah Mahasiswa tanpa harus membuat class lagi
        mahasiswa.jumlah_mahasiswa += 1


# Main Programnya
ucup = mahasiswa("Ucup ", 123939780)  # Instanse
mujahid = mahasiswa("Mujahid", 103282449)  # instanse

hanif = mahasiswa("Hanif", 103282449)  # instanse

# ucup.jurusan = "Ekonomi Mikrotic"  # membuat instanse baru , sesuai nama instanse

# print(mahasiswa.jurusan)
# print(ucup.jurusan)
# print(mujahid.jurusan)

# print(ucup.__dict__)  # mengambil Semua component / var data

print('Jumlah Mahasiswa Sekarang', mahasiswa.jumlah_mahasiswa)
