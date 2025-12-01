
# GAME LEARN COLORS (TKINTER)

import tkinter
import random

# Danh sách màu
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0        # điểm ban đầu
timeleft = 120      # Bước 2: đổi thời gian từ 30 → 120 giây

# HÀM BẮT ĐẦU GAME

def startGame(event):
    global timeleft

    # Nếu thời gian còn nguyên (chưa chạy)
    if timeleft == 120:
        countdown()     # bắt đầu đếm giờ
        nextColour()    # hiển thị màu tiếp theo

# HÀM SINH MÀU TIẾP THEO

def nextColour():
    global score
    global timeleft

    # nếu còn thời gian chơi
    if timeleft > 0:

        e.focus_set()   # đặt focus vào ô nhập

        # Lấy chữ người dùng gõ
        typed = e.get().lower()
        real = colours[1].lower()  # màu đúng là colours[1] (màu hiển thị)

        # Nếu gõ đúng màu → +2 điểm
        if typed == real:
            score += 2                   # BƯỚC 3: +2 điểm
        else:
            if typed != "":              # tránh trừ điểm khi chưa gõ gì
                score -= 1               # BƯỚC 3: đoán sai → -1 điểm

        # Xóa ô nhập
        e.delete(0, tkinter.END)

        # Xáo trộn màu
        random.shuffle(colours)

        # Hiển thị màu ngẫu nhiên
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # Cập nhật điểm
        scoreLabel.config(text="Score: " + str(score))

# HÀM ĐẾM NGƯỢC THỜI GIAN

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1   # giảm 1 giây

        # cập nhật hiển thị thời gian
        timeLabel.config(text="Time left: " + str(timeleft))

        # gọi lại countdown sau 1000ms
        timeLabel.after(1000, countdown)

# GIAO DIỆN TKINTER

root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("450x250")

# Hướng dẫn
instructions = tkinter.Label(
    root,
    text="Type in the COLOUR of the word,\nnot the text written!",
    font=('Helvetica', 12)
)
instructions.pack()

# hiển thị điểm
scoreLabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# hiển thị thời gian
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# label hiển thị màu chữ
label = tkinter.Label(root, font=('Helvetica', 50))
label.pack()

# Ô nhập
e = tkinter.Entry(root)
e.pack()

# Bấm Enter để bắt đầu
root.bind('<Return>', startGame)

e.focus_set()  # đặt con trỏ vào ô nhập

root.mainloop()
