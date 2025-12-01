import turtle

# Tạo màn hình
screen = turtle.Screen()
screen.title("Ve bong hoa bang turtle")

# Tạo bút
pen = turtle.Turtle()
pen.speed(0)        # tốc độ nhanh nhất
pen.color("red")    # màu cánh hoa

# Vẽ 36 cánh hoa
for i in range(36):
    pen.circle(100)     # vẽ một vòng tròn bán kính 100
    pen.right(10)       # xoay bút 10 độ để tạo cánh tiếp theo

# Vẽ nhụy hoa
pen.color("yellow")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# Giữ màn hình
turtle.done()
