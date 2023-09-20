# Operator Bitwise , Operasi Binner

a = 9
b = 5

# Operator Bitwise OR ( | )

c = a | b

print("\n======OR======\n")

# pakai format untuk menghitung binary

# dan hitung menggunkan huruf b untuk binary

print("nilai : ", a, 'Binary ', format(a, "08b"))

print("nilai : ", b, 'Binary ', format(b, "08b"))

# untuk Bitwise or tandanya (|)

print("--------------(|)")

print("nilai : ", c, "Binary", format(c, "08b"))

# untuk tanda Bitwese and (&)

# dan untuk tanda or tidak harus true dua-duanya / bernilai

print("\n======AND======\n")

c = a & b

print("nilai : ", a, 'Binary ', format(a, "08b"))

print("nilai : ", b, 'Binary ', format(b, "08b"))

print("--------------(&)")

print("nilai : ", c, "Binary ", format(c, "08b"))

# ingat tanda and harus true dua duanya  / bernilai

# Untuk tanda Bitwise xor (^)

print("\n======XOR======\n")

c = a ^ b

print("nilai : ", a, 'Binary ', format(a, "08b"))

print("nilai : ", b, 'Binary ', format(b, "08b"))

print("--------------(^)")

print("nilai : ", c, "Binary", format(c, "08b"))

# ingat tanda xor akan merubah yang kondisinya dua-duanya true menjadi false / tidak bernilai

# Untuk tanda Bitwise NOT (~)
# Bernilai Positive dan Negative

print("\n======NOT======\n")
# not di miror yg tadi nya plus menjadi minus

c = ~a

print("nilai : ", a, 'Binary ', format(a, "08b"))

print("--------------(~)")

print("nilai : ", c, "Binary", format(c, "08b"))

print("--------------(^)")
d = 0b0000001001
e = 0b1111111111
print("nilai: ", e ^ d, "Binary", format(e ^ d, "08b"))

# untuk Shifting (Menggeser )

# shifting right ( >> )

c = a >> 2

print("\n======>>======\n")

print("nilai : ", a, 'Binary ', format(a, "08b"))

print("--------------(>>)")

print("nilai : ", c, "Binary ", format(c, "08b"))

# shifting left ( << )

c = a << 2

print("\n======<<======\n")

print("nilai : ", a, 'Binary ', format(a, "08b"))

print("--------------(<<)")

print("nilai : ", c, "Binary ", format(c, "08b"))
