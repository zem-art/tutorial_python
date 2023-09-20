# Belajar Tipe Data Dictionary
print("\n===Tipe Data Dictionary===\n")

print("\n===Contoh Tipe Data===")

# Contoh - Contoh Tipe Data Ada :
list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
set = {1, 2, 3, 4, 5, }

print("Ini Adalah Tipe Data List : ", list, type(list))
print("ini Adalah Tipe Data Tuple : ", tuple, type(tuple))
print("Ini Adalah Tipe Data Set : ", set, type(set))

print("\n===Tipe Data Dictionary===")
# Dictionary : Sebuah Struk tur data / maping


# contoh membuat Tipe Data Dictionary
# var = { key: value,
#         key: value,
#         key: value
#       }
pengurus1 = {"id": 1,
             "nama": "ucil",
             "pekerjaan": "Penganguran",
             "status": "Lajang",
             "alamat": "Indo"
             }

pengurus2 = {"id": 2,
             "nama": "Kiko",
             "pekerjaan": "Dokter",
             "status": "Fuck Boy",
             "alamat ": "Jawa"
             }

semuaPengurus = {1: pengurus1, 2: pengurus2}

print("Data :", semuaPengurus)

# Cek Tipe Data
print("\n===Cek Tipe Data==")
print("Ini Data :", pengurus1["pekerjaan"])  # contoh Memanggil 1 per 1 key nya
print("Ini Keys :", pengurus1.keys())  # melihat semua Keys
print("Ini Value :", pengurus1.values())  # melihat Value
print("Ini Items :", pengurus1.items())  # Melihat Item
