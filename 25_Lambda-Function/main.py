# Belajar Lambda Function

print("\n==BELAJAR LAMBDA FUNCTION==\n")


def jumlah(a, b):
    c = a+b
    return c


hasil = jumlah(4, 5)

print('hasil nya : ', hasil)

# Contoh Menggunkan Lambda
# Anonymous Function

print("\n==Cara Menggunkan Lambda==")


test = lambda argumen: print(argumen)

test('Ini Contoh Lambda')


# membuat Perkalian Dengan Lambda 
kali = lambda x,y: x*y

hasil = kali(3,5)

print('Hasil :' ,hasil)