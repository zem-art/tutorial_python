# Scope Global Dan Lokal
print("\n==Scope Global Dan Lokal==\n")

# Contoh Scope Lokal
print("\n==Scope Lokal==")

namaKucing = "Ucil"

def rubahNama(namaBaru):
  namaKucing = namaBaru # namaKucing Ini Lokal Bkn GLobal
  print("Saya Ingin Merubah Nama Kucing Menjadi :" , namaKucing)

rubahNama("Jojo")
print("Nama Kucing Saya Adalah :" , namaKucing)

# Contoh Scope GLobal
print("\n==Scope GLobal==")

namaKucing = "Ucil"

def rubahNamaKucing(namaBaru):
  global namaKucing # Tinggal Tambah ini
  namaKucing = namaBaru # namaKucing Ini Lokal Bkn GLobal
  print("Saya Ingin Merubah Nama Kucing Menjadi :" , namaKucing)

rubahNamaKucing("Jojo")
print("Nama Kucing Saya Adalah :" , namaKucing)




# Contoh Scope GLobal Multi
print("\n==Scope Lokal==")

makananKucing = "Royal Canin"

def kasihMakan(makanan,nama):
  global namaKucing,makananKucing # Membuat Nama GLobal Yang Banyak
  namaKucing = nama
  makananKucing = makanan
  print("Saya Ingin Merubah Nama Kucing Menjadi :" , namaKucing)


kasihMakan("Universal","Leo")

print("Nama Kucing Saya Adalah :" , namaKucing,"Dan Makana Nya Adalah :" ,makananKucing)