def tambah(a, b):
    print("Fungsi Pertambahan")
    print(a, "+", b, "=", a + b)
    return a + b


def kurang(a, b):
    print("Fungsi Pengurangan")
    print(a, "-", b, "=", a - b)
    return a - b


def main():
    print("Ini Adalah Fungsi Utama Dari Matematika")


if __name__ == "__main__":  # supaya __main Tidak Di jalankan
    main()


# print(__name__)  # untuk memberikan nama modul

# apabila di run di file mtk maka akan menjadi str __main__
# apabila di run di main.py maka menjadi matematika
