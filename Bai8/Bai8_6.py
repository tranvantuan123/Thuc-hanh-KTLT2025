from tkinter import *

# ===== BƯỚC 3: CÁC HÀM XỬ LÝ MENU =====
def NewFile():
    print("Bạn đã chọn: New File")        # Hiển thị thông báo khi chọn New

def OpenFile():
    print("Bạn đã chọn: Open File")       # Hiển thị thông báo khi chọn Open

def Exit():
    print("Bạn đã chọn: Exit chương trình")  # Hiển thị thông báo khi chọn Exit

def InsText():
    print("Bạn đã chọn: Insert Text")     # Hiển thị thông báo khi chọn Insert Text

def InsPic():
    print("Bạn đã chọn: Insert Picture")  # Hiển thị thông báo khi chọn Insert Picture

def About():
    print("This is Menu Example using Tkinter")  # Hiển thị khi chọn About

# ===== BƯỚC 1 + 2: TẠO CỬA SỔ VÀ MENU =====
root = Tk()                     # Tạo cửa sổ chính
root.title("Demo Menu")         # Đặt tiêu đề cửa sổ
root.geometry("400x300")        # Đặt kích thước cửa sổ

menu = Menu(root)               # Tạo thanh menu
root.config(menu=menu)          # Gắn menu vào cửa sổ

# ----- MENU FILE -----
filemenu = Menu(menu, tearoff=0)   # Tạo menu con cho File (tearoff=0 để bỏ dấu gạch)
menu.add_cascade(label="File", menu=filemenu)  # Tạo mục File trên thanh menu

filemenu.add_command(label="New", command=NewFile)   # Tạo lựa chọn New
filemenu.add_command(label="Open", command=OpenFile) # Tạo lựa chọn Open
filemenu.add_separator()                             # Tạo đường gạch ngang
filemenu.add_command(label="Exit", command=Exit)     # Tạo lựa chọn Exit

# ----- MENU INSERT -----
insertmenu = Menu(menu, tearoff=0)                   # Menu Insert
menu.add_cascade(label="Insert", menu=insertmenu)    # Thêm mục Insert

insertmenu.add_command(label="Insert Text", command=InsText)  # Lệnh Insert Text
insertmenu.add_command(label="Insert Picture", command=InsPic) # Lệnh Insert Picture

# ----- MENU HELP -----
helpmenu = Menu(menu, tearoff=0)                     # Menu Help
menu.add_cascade(label="Help", menu=helpmenu)        # Thêm mục Help

helpmenu.add_command(label="About...", command=About) # Lệnh About

root.mainloop()      # Chạy chương trình giao diện
