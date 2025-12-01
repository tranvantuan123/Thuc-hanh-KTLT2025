from tkinter import *

# Tạo cửa sổ
window = Tk()
window.title("Demo Tkinter")
window.geometry('350x200')

# Label nằm ở giữa
lbl = Label(window, text="Nhấn nút bên dưới")
lbl.pack(pady=20)   # tạo khoảng cách trên/dưới cho đẹp

# Hàm xử lý sự kiện
def clicked():
    lbl.configure(text="Bạn đã bấm nút!")

# Button nằm giữa + đổi màu
btn = Button(window, text="Bấm vào đây",
             command=clicked,
             bg="lightblue",
             fg="red")
btn.pack()

window.mainloop()
