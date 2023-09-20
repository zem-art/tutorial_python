# balajar Menggunkan Packed Python
# tkinter = packed dari python untuk GUI

import tkinter

main_window = tkinter.Tk()


def event():  # fungsi untuk menjalan kan tombol nya
    label1 = tkinter.Label(main_window, text="Aku Di Tekan ^_^")
    label1.pack()


label = tkinter.Label(main_window, text="Hallo Dunia")
# comment untuk menjalankan fungsi
tombol = tkinter.Button(main_window, text="Tekan Aku", command=event)

label.pack()
tombol.pack()
# keluar kan main_windows
main_window.mainloop()  # kenapa Harus Mainloop agar menjalankan Terus
