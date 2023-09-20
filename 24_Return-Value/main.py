# Belajar Return Value
print('\n===BELAJAR RETURN VALUE===')

# Membuat fungsi Mengembalikan Value

# Cara Ke 1

print("\n==Membuat Fungsi Dengan Return Value==")


def kuadrat(argument):
    total = argument**2
    print("Nilai Kuadrat Dari : ", argument,
          "Adalah", total)  # Tanda Kuadrat (**)
    return total  # untuk mengembalikan nilai value nya


a = kuadrat(3)  # Cara Ke 1
print("Nilai Kuadrat Nya", a)
# print(kuadrat(4))  # cara Ke 2

print('='*20)
# Fungsi Dengan Return Value Dan Multiple Argumen

print("\n===Fungsi Return Value Dan Multiple Argument===")

# Contoh PERTAMBAHAN
print("\n==Contoh Pertambahan==")


def tambah(argument1, argument2):
    total = argument1 + argument2
    print(argument1, "+", argument2, "=", total)
    return total


a = tambah(3, 4)
print('Total :', a)

# Contoh PERKALIAN
print("\n==Contoh Perkalian==")


def kali(argument1, argument2):
    total = argument1 * argument2
    print(argument1, "*", argument2, "=", total)
    return total


b = kali(3, tambah(3, 4))  # Nilai Tambah Dapet Dari Atas
print("Total : ", b)

# Membuat LIST
print("\n===Membuat List===")


def urutan(argument1, argument2):
    total = argument1 + argument2
    print(argument1, "+", argument2, "=", total)
    return [total, 2, 3, 4]


a = urutan(3, 4)
print('Total :', a)
