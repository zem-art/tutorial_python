# Pengenalan String

data = 'Ini adalah String'
print(data)
print(type(data))

# 1 . cara membuat String

'''

 1 . dengan Membuat Single quote '...' .
 2 . dengan Membuat Double quote "..."

'''

data = 'menggunakan single quote'

print(data)

data = "Ini adalah daouble quote"

print(data)

print("'Halo Apa Kabar ?'")
print('"Halo Apa Kabar ?"')

print("ini Adalah hari  jum'at")

# 2 .ini Adalah Tanda backslash |

# membuat tanda ' menjadi string

print('mari shalat jum\'at')
# print('g\day ist\'t it ?')
print("C:\\user\\Ujang")

# tanda Tab
print("ujang\t\t\tusup , jauhan")

# tanda BackSpace
print("ucup \botong , jadi deketan")

# tanda newline

print("baris Pertama.\nbaris kedua.")  # ini LF (line feed) (unix, mac & linux)

# CR -> carriage return -> commodore ,acorn ,lisp
print("baris Pertama.\rbaris kedua.")

# CRLF  => line feed carriage return -> dipakai untuk windows
print("baris Pertama.\r\nbaris kedua.")


# 3 . string literal atau raw

# Hati-hati

print('C:\new folder')  # akan salah pacth nya

# menggunakan raw string
# apa pun yang ada di dalam raw string akan di anggap string
print(r'C:\new folder')

# multiline literal string

print(""" 
nama: arif 
tingkat : Kuliah 
""")

# multiline literal raw string

print(""" 
Nama: arif 
Tingkat : Kuliah S3\new Normal
website : www.larashop.com/newID 
""")
