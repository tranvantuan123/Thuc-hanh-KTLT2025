from tkinter import *

# Tạo cửa sổ
root = Tk()
root.title("Thông tin cá nhân")
root.geometry("350x250")

# ====== Nội dung form ======
Label(root, text="Họ và tên:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
Entry(root, width=25).grid(row=0, column=1)

Label(root, text="Ngày tháng năm sinh:", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
Entry(root, width=25).grid(row=1, column=1)

Label(root, text="MSSV:", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
Entry(root, width=25).grid(row=2, column=1)

Label(root, text="Ngành học:", font=("Arial", 12)).grid(row=3, column=0, sticky="w")
Entry(root, width=25).grid(row=3, column=1)

root.mainloop()
