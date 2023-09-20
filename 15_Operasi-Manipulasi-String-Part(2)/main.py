# Operator dalam Bentuk Methods

# Merubah case dari string

# merubah semua ke upper case

salam = "bro !"

print("normal = " + salam)

# merubah menjadi Huruh KAPITAL
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case

salam = "aKu KeCe AbieeZzZzzZ"
print("lower = " + salam)  # var Default nya

# di ubah Menjadi Normal Hurufnya
salam = salam.lower()

print("lower = " + salam)

# Pengecekan dengan isX method

# contoh Pengecekan lower case

salam = "sist"

apakah_lower = salam.islower()

print(salam + " is lower " + str(apakah_lower))  # ubah ke str

apakah_upper = salam.isupper()

print(salam + " is  upper " + str(apakah_upper))  # ubah ke str

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- untuk huruf dan angka (Biasanya Di Gunkan di Pass)
# isdecimal() <--- untuk angka saja
# isspace() <--- untuk space , tab , newline in
# istitle() <--- untuk kata yg dimulai dengan huruf besar

# istitle()
# harus gede semua di depan katanya
judul = "It's Is Okay Not To Be Orkay"

cek_judul = judul.istitle()  # hasil nya Bool

print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswith() endswith() <--- keren
# bisa Menggunkan Literal (.)
# cek Depan kata dari string
cek_start = "Sangjangim Oppa".startswith("Sangjangim")

print("start = " + str(cek_start))
# cek Belakang kata dari string
cek_end = "Sangjanim Oppak".endswith("Oppak")

print("Start = " + str(cek_end))

# penggabungkan komponen join() , split

# JOIN
pisah = ["aku", "sayang", "kamu"]
gabung = ",".join(pisah)
print(gabung)

gabungan = " ".join(pisah)
print(gabungan)

gabungan = " ehm ".join(pisah)
print(gabungan)

# SPLIT
gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))
# membalikan data ke semula dan memisahkanya

# Alokasi Karakter # rjust() , ljust() ,center

# contoh rjust()
kanan = "kanan".rjust(10)

print("'" + kanan + "'")
# cotoh ljust()
kiri = "kiri".ljust(10)

print("'" + kiri + "'")

# contoh center
tengah = "tengah".center(20, ":")

print("'" + tengah + "'")

# Kebalikan --> strip()
tengah = tengah.strip(":")  # mengilangkan tanda ini (#)

print("'" + tengah + "'")
