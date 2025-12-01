from tkinter import *

# a) Xây dựng cửa sổ đồ họa
window = Tk()
window.title("Ví dụ Tkinter")
window.geometry("350x200")

# Nhãn hiển thị
lbl = Label(window, text="Nhấn nút để đổi nội dung")
lbl.grid(column=0, row=0)

# c) Xây dựng phương thức xử lý sự kiện khi bấm phím
def clicked():
    lbl.configure(text="Bạn đã bấm nút!")

# b) Thêm Button vào window form
# d) Thay đổi màu nền (bg) và màu chữ (fg)
btn = Button(window, 
             text="Click Me",
             bg="lightgreen",   # màu nền
             fg="blue",         # màu chữ
             command=clicked)   # gán sự kiện
btn.grid(column=1, row=0)

# Vòng lặp chạy chương trình
window.mainloop()
