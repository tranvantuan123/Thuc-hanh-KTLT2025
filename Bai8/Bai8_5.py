import tkinter as tk

root = tk.Tk()
root.title("Radio Button Demo")
root.geometry("300x250")

v = tk.IntVar()
v.set(1)     # giá trị mặc định

languages = [
    ("Lựa chọn 1", 1),
    ("Lựa chọn 2", 2),
    ("Lựa chọn 3", 3),
    ("Lựa chọn 4", 4),
    ("Lựa chọn 5", 5)
]

def ShowChoice():
    print("Bạn chọn:", v.get())

# Label tiêu đề
tk.Label(
    root,
    text="Choose your favourite programming language:",
    justify=tk.LEFT,
    padx=20
).pack()

# Tạo radio button dạng tròn
for txt, val in languages:
    tk.Radiobutton(
        root,
        text=txt,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val
    ).pack(anchor=tk.W)

root.mainloop()
