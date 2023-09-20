# Operasi Komperasi Boollean

# > , < , >= , <= , == , != , is ,is not

# Lebih Besar Dari
print("====Lebih Dari==== ( > ) ")
a = 4
b = 2

hasil = a > 3

print(a, ">", b, "=", hasil)

hasil = b > 3

print(a, ">", b, "=", hasil)

hasil = b > 3

print(a, ">", 2, "=", hasil)

# Kurang Dari

print("====Kurang Dari==== ( < )")


hasil = a < 3

print(a, "<", b, "=", hasil)

hasil = b < 3

print(a, "<", b, "=", hasil)

hasil = b < 2

print(a, "<", 2, "=", hasil)

# Lebih Dari Sama Dengan

print("====Lebih Dari Sama Dengan==== ( >= )")


hasil = a >= 3

print(a, ">=", b, "=", hasil)

hasil = b >= 3

print(a, ">=", b, "=", hasil)

hasil = b >= 3

print(a, ">=", 2, "=", hasil)

# Kurang Dari Sama Dengan

print("====Kurang Dari Sama Dengan==== ( <= )")


hasil = a <= 3

print(a, "<=", b, "=", hasil)

hasil = b <= 2

print(a, "<=", 3, "=", hasil)

hasil = b <= 3

print(a, "<=", 2, "=", hasil)

# sama dengan (==)

print("====Sama Dengan Dari Sama ==== ( == )")

hasil = a == 4

print(a, "==", b, "=", hasil)

hasil = b == 4

print(a, "==", 3, "=", hasil)

# Tidak Sama Dengan (!=)

print("====Sama Dengan Dari Sama ==== ( != )")

hasil = a != 4

print(a, "!=", 4, "=", hasil)

hasil = b != 4

print(a, "!=", 4, "=", hasil)

# Semua yang diatas bekerja pada syntax literal (Yang tidak Ada variabel nya)

# 'is' sebagai komperasi object identity
# is (Membanding kan object / variabel)

print("===Object Identity=== (is) ")

x = 5  # ini adalah assigment membuat object
y = 5
# hex mengecek id nya
print("nilai x = ", x, "id", hex(id(x)))
print("nilai y = ", y, "id", hex(id(y)))

hasil = x is y

print("x is y = ", hasil)

print("===Object Identity=== (is not) ")

x = 5  # ini adalah assigment membuat object
y = 6
# hex mengecek id nya
print("nilai x = ", x, "id", hex(id(x)))
print("nilai y = ", y, "id", hex(id(y)))

hasil = x is not y

print("x is not y = ", hasil)
