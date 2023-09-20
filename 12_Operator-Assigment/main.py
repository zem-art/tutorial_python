# Operator Assigment Operator Yang Dilakukan dengan Penyingkatan

# Operasi Di Tambah Assignment

a = 5  # adlah Assignment

print('nilai a =', a)

a = a + 1  # artinya adalah a = a + 1

print('nilai a += 1, nilai a menjadi', a)

a -= 2  # artinya adalah a = a - 2
print('nilai a -= 2, nilai a menjadi', a)

# nilai awal 5 + 1 = 6
# lalu 6 - 2 = jadi

a *= 5  # artinya adalah a = a * 5
print('nilai a *= 5, nilai a menjadi', a)

a /= 2  # artinya adalah a = a / 2
print('nilai a /= 2, nilai a menjadi', a)

# Coba di Modulus kan (Di bagi Sampai Habis)
# dan kita Floor Division

print('\n===Modulus===')

b = 10
print('\nnilai b =', b)

b %= 3
print('nilai a %= 2, nilai b menjadi', b)

b = 10
print('\nnilai b =', b)

# Kita Ubah Menjadi LeftDivicion
b //= 3
print('nilai a //= 3, nilai b menjadi', b)

# pangkat / Eksponen

a = 5
print('nilai a = ', a)
# pangkat kan
a **= 3
print('nilai a **= 3, nilai a menjadi', a)

print('\n===Operasi Bitwase===')

print('\n===OR===')
# operasi OR
c = True
print('\nNilai c =', c)
# kita OR kan
c |= False
print('nilai c |= False, nilai c menjadi', c)
# kita False
c = False
print('\nNilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi', c)

print('\n===AND===')
# AND

c = True
print('\nNilai c =', c)
# kita OR kan
c &= False
print('nilai c &= False, nilai c menjadi', c)
# Kondisi False
c = True
print('\nNilai c =', c)
c &= True
print('nilai c &= True, nilai c menjadi', c)

print('\n===XOR===')
# XOR

c = True
print('\nNilai c =', c)
# kita OR kan
c ^= False
print('nilai c ^= False, nilai c menjadi', c)
# Kondisi False
c = True
print('\nNilai c =', c)
c ^= True
print('nilai c ^= True, nilai c menjadi', c)

# Operator Geser - Geser
print('\n==Operator Geser-Geser==')

d = 0b0100

print('\nNilai d =', format(d, '04b'))

# Sift right (geser Ke Kanan)

d >>= 2
print('nilai d >>= 2, nilai d menjadi', format(d, '04b'))

# Sift left (geser Ke Kiri)
d <<= 1
print('nilai d <<= 1, nilai d menjadi', format(d, '04b'))
