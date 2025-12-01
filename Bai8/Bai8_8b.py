from tkinter import *

root = Tk()
root.title("Radio Button Demo")
root.geometry("300x200")

# Biến chứa lựa chọn radio (1, 2, 3)
v = IntVar()
v.set(1)   # mặc định chọn 1

# Hàm xử lý nút bấm
def showSelected():
    lbl.config(text=f"Bạn chọn: {v.get()}")   # cập nhật label kết quả

# ====== Tạo radio button ======
Label(root, text="Chọn một tùy chọn:", font=("Arial", 12)).pack()

Radiobutton(root, text="Option 1", variable=v, value=1).pack(anchor="w")
Radiobutton(root, text="Option 2", variable=v, value=2).pack(anchor="w")
Radiobutton(root, text="Option 3", variable=v, value=3).pack(anchor="w")

# Nút Click Me
Button(root, text="Click Me", command=showSelected).pack(pady=10)

# Label hiện kết quả
lbl = Label(root, text="Bạn chọn: ", font=("Arial", 12))
lbl.pack()

root.mainloop()
