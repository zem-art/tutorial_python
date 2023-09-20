# Latihan komperasi dan Logika

# membuat gabungan area rentang dari angka

# Menggunkana Keword OR

# ++++3-----10+++++
# Ini adalah Kasus Gabungan

inputUser = int(input(
    "masukan angka yang bernilai \n kurang dari 3  \n atau lebih besar dari 10 : "))

# +++3---
# Memeriksa Angka Kurang dari 3

isKurangDari = (inputUser < 3)

print("Kurang Dari 3: ", isKurangDari)

# +++10-----
# Memeriksa Lebih Besar Dari 10

isLebihDari = (inputUser > 10)

print("Lebih Dari 10: ", isLebihDari)

isCorrect = isKurangDari or isLebihDari

print("angka Yang Anda Masukan: ", isCorrect)

# cara membuat = yang banyak Dan Space
print("\n", 19*"=", "\n")

# Menggunakan Keword AND

# ----3++++10-----

# ini Adalah Kasus Irisan

inputUser = int(input(
    "masukan angka yang bernilai \n lebih dari 3  \n dan kurang dari 10 : "))


# ---3++++
# Memeriksa Angka Lebih dari 3

isLebihDari = (inputUser > 3)

print("Lebih Dari 3: ", isLebihDari)

# +++10-----
# Memeriksa Kurang Dari 10

isKurangDari = (inputUser < 10)

print("Kurang Dari 10: ", isKurangDari)

isCorrect = isLebihDari and isKurangDari

print("angka Yang Anda Masukan: ", isCorrect)
