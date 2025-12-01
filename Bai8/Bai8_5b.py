import tkinter as tk

root = tk.Tk()
root.title("Radio Button Indicator")

v = tk.IntVar()
v.set(1)

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Bạn đã chọn:", v.get())

tk.Label(root,
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20).pack()

for lang, val in languages:
    tk.Radiobutton(root,
                   text=lang,
                   variable=v,
                   value=val,
                   indicatoron=0,   # biến radio thành nút nhấn
                   width=20,
                   command=ShowChoice).pack(anchor=tk.W, pady=2)

root.mainloop()
