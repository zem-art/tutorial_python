# Mengambil Data Dari User

# data Yang di Masukan Pasti str

data = input("Masukan Nama: ")

print("data", data, type(data))

# jika Mau Mengambil Data int Maka :

number = int(input("Masukan Umur: "))

print("data", number, "type", type(number))

# Data Float

number_koma = float(input("Masukan Tinggi: "))

print("data", number_koma, "type", type(number_koma))

# Bagaimana Dengan Bool
# casting data bool dulu menjadi int baru bisa

binner = bool(int(input("Masukan nilai boollean: ")))

# print("data", binner, "type", type(binner))
