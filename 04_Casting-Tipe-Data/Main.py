# Casting (Merubah Dari 1 Tipe Ke Tipe Lain)

# Tipe Data = int, float , str , bool

# INTEGER
print("=====INTEGER=====")
# Defaulty Var nya
# data_int = 0
data_int = 9
# data_int = -1

print("data", data_int, "type:", type(data_int))

# cara Merubah Data dari int Menjadi Tipe data yg lain

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data:", data_float, "type:", type(data_float))
print("data:", data_str, "type:", type(data_str))

# apabila Nilai nya berisikan 0 makan Nilai nya True dan apabila Nilai nya 0 Maka Nilai nya False
print("data:", data_bool, "type:", type(data_bool))


# FLOAT
print("=====FLOAT=====")
data_float = 9.5

print("data", data_float, "type:", type(data_float))

# cara Merubah Data dari int Menjadi Tipe data yg lain

data_inti = int(data_float)  # akan dibulatkan ke bawah walaupun int ada koma
data_stri = str(data_float)
data_bool = bool(data_float)
# apabila Nilai nya berisikan 0 makan Nilai nya True dan apabila Nilai nya 0 Maka Nilai nya False

print("data:", data_inti, "type:", type(data_int))
print("data:", data_stri, "type:", type(data_str))
print("data:", data_bool, "type:", type(data_bool))


# BOOLEAN
print("=====BOOLEAN=====")
data_bool = False

print("data", data_bool, "type:", type(data_bool))

# cara Merubah Data dari int Menjadi Tipe data yg lain

data_inti = int(data_bool)  # akan dibulatkan ke bawah walaupun int ada koma
data_str = str(data_bool)
data_float = float(data_bool)
# apabila Nilai nya berisikan 0 makan Nilai nya True dan apabila Nilai nya 0 Maka Nilai nya False

print("data:", data_inti, "type:", type(data_int))
print("data:", data_str, "type:", type(data_str))
print("data:", data_float, "type:", type(data_float))

# STRING
print("=====STRING=====")
data_str = ""

print("data", data_str, "type:", type(data_str))

# cara Merubah Data dari int Menjadi Tipe data yg lain

# data_int = int(data_str)  # str Harus Angka
data_bool = bool(data_str)  # str Harus Angka
# data_float = float(data_str)  # false Harus string kosong

# print("data:", data_int, "type:", type(data_int))

print("data:", data_bool, "type:", type(data_bool))
# print("data:", data_float, "type:", type(data_float))
