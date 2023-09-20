import timeit

print("\n===Test Kecepatan Tuple===\n")

data_list = timeit.timeit(stmt = "[1,3,4,5,6,7,8,9]",number=1000000)
data_tuple = timeit.timeit(stmt = "(1,3,4,5,6,7,8,9)",number=1000000)

print("Waktu Untuk Memproses List :" ,data_list)
print("Waktu Untuk Memproses Tuple :" ,data_tuple)