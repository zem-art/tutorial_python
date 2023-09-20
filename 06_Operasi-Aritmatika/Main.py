# Pelajaran Operasi AritMatika

a = 10
b = 5

# Operasi Tambah

hasil = (a + b)

print(a, "+", b, "=", hasil)

# Operasi Pengurangan

hasil = (a - b)

print(a, "-", b, "=", hasil)

# Operasi Perkalian

hasil = (a * b)

print(a, "*", b, "=", hasil)

# Operasi Pembagian

hasil = (a / b)

print(a, "/", b, "=", hasil)

# Operator Exponents (Pangkat)

hasil = (a ** b)

print(a, "**", b, "=", hasil)

# Operasi Modulus (Sisa Pembagian)

hasil = (a % b)

print(a, "%", b, "=", hasil)

# Operasis Floor Division(Kebalikan Dari Modulus)

hasil = (a // b)

print(a, "//", b, "=", hasil)

# Priotas Dalam Operasi (UGD)

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y-y % z // x

print(x, "**", y, " *", z, "+", x, "/", y, "-",
      y, "%", z, "//", x, "Hasil= ", hasil)

# Operasi Yg Akan Di selesai kan dahulu Di dalam MTK
# 1. (')
# 2. Exponent
# 3. Perkalian (Modulus & Pembagian , floor division )
# 4. Pertambahan, Pengurangan

hasil = x + y * z

print(x, "+", y, "*", z, "=", hasil)

# Kurung Akan Mengambil Langkah Pertama

hasil = (x + y) * z

print("(", x, "+", y, ") *", z, '=', hasil)
