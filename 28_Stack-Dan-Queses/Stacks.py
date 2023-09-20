# Belajar Stackcs And Queues
print("\n==Contoh Dari Stacks==\n")

# Stacks : Menumpuk Sama Hal nya Buku Pasti Yang Di Ambil Paling Atas

# Queues : Antrian Barang Yang Pertama Di Ambil nya 

# COntoh Data Append
print("\n===Uji Coba Menggunakan Data Append===")
tumpukan = [1,2,3,4,5,6]
print("Data Sekarang :" ,tumpukan)
# Memasukan Data Baru
tumpukan.append(7)
print("Data Yang Sudah Di Tambah :" , tumpukan)
tumpukan.append(8)
print("Data Yang Sudah Di Tambah :" , tumpukan)

# Menghapus Data
print("\n===Contoh Stacks===")
out = tumpukan.pop() # Ini Adalah Stacks # Menghilangkan Data Di Belakang
print("Data Keluar" , out) # melihat Data yg di keluarkan
print("Data Sekarang :" ,tumpukan)

