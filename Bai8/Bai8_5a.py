import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")

v = tk.IntVar()
v.set(1)       # Giá trị mặc định (Python = 1)

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
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
