import turtle
import random

# Tạo màn hình
screen = turtle.Screen()
screen.title("Ve hinh do hoa nhieu vong tron xoay")

# Tạo bút
pen = turtle.Turtle()
pen.speed(0)       # tốc độ nhanh nhất
pen.width(2)       # nét vẽ đậm hơn

colors = ["red", "blue", "green", "purple", "orange", "brown"]

# Vẽ 12 vòng tròn xoay quanh tâm
for i in range(12):
    pen.color(colors[i % len(colors)])  # đổi màu liên tục
    pen.circle(100)                      # vẽ vòng tròn bán kính 100
    pen.right(30)                        # xoay 30 độ (12 lần = 360°)

turtle.done()
