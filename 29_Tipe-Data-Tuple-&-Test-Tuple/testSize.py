# Kegunaan Dari Tuple
import sys

print("\n==Menguji Kegunaan Dari Tuple==\n")

data_list = [1,2,3,4,5,6,7,8,9,10,"pisang goreng","via valen",False,3.14]

data_tuple = (1,2,3,4,5,6,7,8,9,10,"pisang goreng","via valen",False,3.14)

# print("Data List : " ,data_list)
# print("Data Tuple : ",data_tuple)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple =sys.getsizeof(data_tuple)

print("Besar Data Dari List :" , besar_datalist)
print("Besar Data Dari Tuple :" , besar_datatuple)