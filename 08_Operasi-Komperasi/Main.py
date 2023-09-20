# Operasi logika Perhitungan Boollean

# not , or , and , xor

# NOT

print("===NOT===")  # memiliki 1 buah nilai

a = False
# bisa di buat menggunakan not
c = not a
print("data Bool = ", a)
print("----------NOT")
print("data C =", c)

# OR

print("===OR===")  # jika salah 1 true maka hasilnya true
# memilki 2 buah nilai
a = False
b = False
# bisa di buat menggunakan or
c = a or b
print(a, "OR", b, "=", c)

a = False
b = True
# bisa di buat menggunakan or
c = a or b
print(a, "OR", b, " =", c)

a = True
b = False
# bisa di buat menggunakan or
c = a or b
print(a, " OR", b, "=", c)

a = True
b = True
# bisa di buat menggunakan or
c = a or b
print(a, " OR", b, " =", c)

# AND

print("===AND===")  # jika 2 buah nilai true maka hasil nya true
# memilki 2 buah nilai
a = False
b = False
# bisa di buat menggunakan and
c = a and b
print(a, "AND", b, "=", c)

a = False
b = True
# bisa di buat menggunakan and
c = a and b
print(a, "AND", b, " =", c)

a = True
b = False
# bisa di buat menggunakan and
c = a and b
print(a, " AND", b, "=", c)

a = True
b = True
# bisa di buat menggunakan and
c = a and b
print(a, " AND", b, " =", c)

# XOR

print("===XOR===")  # akan true jika salah satu true , sisanya false
# memilki 2 buah nilai & tanda nya ( ^ )
a = False
b = False
# bisa di buat menggunakan xor
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = True
# bisa di buat menggunakan xor
c = a ^ b
print(a, "XOR", b, " =", c)

a = True
b = False
# bisa di buat menggunakan xor
c = a ^ b
print(a, " XOR", b, "=", c)

a = True
b = True
# bisa di buat menggunakan xor
c = a ^ b
print(a, " XOR", b, " =", c)
