# Belajar Intsall Package External

# PIP

# Melihat Python => python3 --version
# Melihat Package => pip3 list --format=columns

# import numpy as np
from PIL import Image
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([6, 7, 8, 9, 10])
im = Image.open('foto.jpg')
print('Format File : ' + im.format)
print('Ukuran File : ' + str(im.size))
print('Mode File : ' + im.mode)

im.show()

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9]

# print(a + b)
