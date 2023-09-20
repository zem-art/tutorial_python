# Belajar Class Inheritence

class Ojeg():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_mamang(self):
        print('Nama : ', self.nama, '\nMotor : ',
              self.transmisi, '\nWilayah:', self.daerah)


class Gojeg(Ojeg):  # Turunan Dari Class Ojeg
    def cek_id_mamang(self):
        print("silahkan Cek Aplikasi")


ojeg1 = Ojeg('Asep', 'Revo', 'Bandung')
ojeg2 = Gojeg('Budi', 'Jupiter', 'Bandung')

ojeg1.cek_id_mamang()
ojeg2.cek_id_mamang()
