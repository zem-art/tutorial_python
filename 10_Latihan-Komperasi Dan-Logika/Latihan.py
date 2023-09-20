# Latihan Nya

# 1 ---0+++5----8++++11-----

inputUser = int(input(
    "masukan angka yang bernilai \n lebih dari 0  \n dan kurang dari 5 \n dan lebih dari 8 \n dan kurang dari 11: "))

# ---0+++

isLebihDari = (inputUser > 0)

print("Lebih Dari 0: ", isLebihDari)

# +++5---

isKurangDari = (inputUser < 5)

print("Kurang Dari 5: ", isKurangDari)

# ---8+++

isLebihDari = (inputUser > 8)

print("Lebih Dari 8: ", isLebihDari)

# +++11---

isKurangDari = (inputUser < 11)

print("Kurang Dari 11: ", isKurangDari)

# hasil

isCorrect = isLebihDari ^ isKurangDari

print("angka Yang Anda Masukan: ", isCorrect)


print("\n", 19*"=", "\n")
# SOAL NO 2

# 2 +++0---5++++8----11+++++

inputUser = int(input(
    "masukan angka yang bernilai \n kurang dari 0  \n dan lebih dari 5 \n dan kurang dari 8 \n dan lebih dari 11: "))

# +++0---

isKurangDari = (inputUser < 0)

print("Kurang Dari 0: ", isKurangDari)

# ---5+++

isLebihDari = (inputUser > 5)

print("Lebih Dari 5: ", isLebihDari)

# +++8---

isKurangDari = (inputUser < 8)

print("Kurang Dari 8: ", isKurangDari)

# ---11+++

isLebihDari = (inputUser > 11)

print("Lebih Dari 11: ", isLebihDari)

# hasil

isCorrect = isKurangDari ^ isLebihDari

print("Angka Yang Anda Masukan: ", isCorrect)
