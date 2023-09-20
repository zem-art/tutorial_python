# BELAJAR CONTINUE DAN PASS

# contoh dari BREAK
print('===Contoh Dari Break===')
for i in range(1, 10):
    if i == 6:
        print('Nilai i Adalah ', i)
        break
    print("nilai saat ini Adalah", i)
else:
    print('Akhir Dari Loop')

print("Diluar Loop ")

# contoh dari CONTINUE
print('\n===Contoh Dari Continue===')
for i in range(1, 10):
    if i == 6:
        print('Nilai i Adalah ', i)
        continue  # akan melanjutkan kestate berikut nya
        print('Cek Aja')  # ini dilewat

    print("nilai saat ini Adalah", i)
else:
    print('Akhir Dari Loop')

print("Diluar Loop ")

# contoh dari PASS
print('\n===Contoh Dari Pass===')
for i in range(1, 10):
    if i == 6:
        print('Nilai i Adalah ', i)
        pass  # kata kunci kosong untuk dilewat
        print('Cek Aja')  # ini dilewat
    print("nilai saat ini Adalah", i)
else:
    print('Akhir Dari Loop')

print("Diluar Loop ")
