# list [Array]

data = [1, 4, 9, 16, 24, 26, 49, 64]

print('\n==Mengakses List==\n')
# mengakses List
Subdata1 = data[5]
Subdata2 = data[-3]
print('data default = ', data)
print('data ke 5 = ', Subdata1)
print('data ke 3 dari belakang = ', Subdata2)


print('\n==Memotong List data==\n')
# Memotong list
Subdata3 = data[2:4]

print('data default = ', data)
print('data yang ke potong = ', Subdata3)

print('\n==Memotong List data==\n')
# mengambil data yang ada di belakang
Subdata4 = data[-2:]
print('data yang diambil = ', Subdata4)

print('\n==Menggabungkan 2 array==\n')
data2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
# data nya kita tambah
data3 = data + data2
print('data yang sudah di gabungkan = ', data3)

print('\n==Merubah Data content dari list==\n')
# Merubah Data content dari list
# data[4] = 24

# mengcopy data list ke variabel baru
a = data[:]
# datanya akan berubah apabila kita tidak menambahkan :
a[4] = 87  # data nya diubah yang ke 4
# apabila panggil data maka data nya akan tetep sama seperti yg di default
print('data yang belum di ubah = ', data)
# apabila panggil a maka datanya akan berubah menjdai 87
print('data yang sudah di ubah = ', a)

print('\n===mengubah content list===\n')
# merubah content list dengan menggunkan metode slicing( merubah data list secara double )

data[3:5] = [11, 12]
print(data)

# list dalam list
print('\n===menggabungkan array dengan array===\n')
x = [data, data2]
print('data gabungan = ', x)

print('\n===mengakses Multidimensional===\n')
# mengakses list dalam multidimensional list \ memanggil data di dalam array multidemsion
y = x[1][4]
print('komponent X =', x)
print('\nkomponent Y =', y)

# method untuk list
print('\n==Method untuk list==\n')
data.append(30)

print('ini data tambahan = ', data)

# function yang bisa kita gunakan pada list
print('\n==Method Lenght==\n')
panjang_list = len(data)

print('data = ', data)
print('data lenght = ', panjang_list)
