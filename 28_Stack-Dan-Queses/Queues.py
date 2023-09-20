from collections import deque # Apabila Tidak punya Build in Di Python
print("\n===Contoh Dari Queues===\n")

antrian = deque([1,2,3,4,5,6]) # Pakai deque Untuk Mengurutkan Data

print("Data Sekarang : " , antrian)

# Menambah Kan Data
print("\n===Menambah Kan Data===") 

antrian.append(7)

print("Data Masuk : ",7)
print("Data Masuk Adalah :" , antrian)

antrian.append(8)

print("Data Masuk : ",8)
print("Data Masuk Adalah :" , antrian)

# Menguragi Antrian Dari Depan 
print("\n===Mengurangi Data Dari Awal===")

out = antrian.popleft() # tambahkan popleft untuk Mengeluarkan Data Dari Depan

print("Data Keluar :" ,out)
print("Data Sekarang :" , antrian)


out = antrian.popleft() # tambahkan popleft untuk Mengeluarkan Data Dari Depan

print("Data Keluar :" ,out)
print("Data Sekarang :" , antrian)


out = antrian.popleft() # tambahkan popleft untuk Mengeluarkan Data Dari Depan

print("Data Keluar :" ,out)
print("Data Sekarang :" , antrian)