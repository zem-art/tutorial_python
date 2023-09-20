# Belajar Try And Exception Eror Handling

# Ada 2 Tipe Eror

# Eror Syntax
# print('Nama Saya Asep)

# Eror Runtime
# def pembagian(a, b):
#     return(a/b)


# penyembut = int(input("Masukan Angka Sembarang : \n"))
# pembilang = int(input("Masukan Angka Sembarang : \n"))

# print(pembagian(penyembut, pembilang))

# Eror Handling

# try:
#     a = 1/0
# except:
#     print("Eror Pembagian Nol")

# print("Akhir Dari Pembagian")
print('\n====Program Pembagian====\n')

while True:
    try:
        penyebut = int(input("Masukan Angka Penyebut: "))
        pembilang = int(input("Masukan Angka Pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:  # Kita Ambil Value Dari Eror Tersbut
        print("Yang Anda Masukan Bukan Angka\n")

    except ZeroDivisionError:
        print('Angka Yang Anda Masukan Adalah Nol , Pilih Yang Lain Yaa Bro\n')

    except Exception as err:  # Mengambil Eror Dari Bawaan Interperted nya Langsung
        print(err, '\n')  # Membuat Eror Yang Lebih Umum


"""
  Type Of Exception Erorrs
  1 . IOError => Untuk Input Output Apabila kita masukan file txt / json
  2 . ImportError => Untuk Apabila Tidak Ada Package Di Projeck Kita
  3 . ValueError => 
  4 . KeyboardIntereptured =>
  5 . EoFError => 
"""

print("Berhasil , Hasil Dari Pembagian Adalah :", hasil)
