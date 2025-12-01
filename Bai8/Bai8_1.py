import turtle

# Tạo màn hình và đặt tiêu đề
man_hinh = turtle.Screen()
man_hinh.title("Ve hinh xoay bang Turtle")

# Tạo bút vẽ
but = turtle.Turtle()
but.speed(0)   # tốc độ nhanh nhất

# Vẽ hình xoắn từ các hình vuông
canh = 5
for i in range(50):
    but.forward(canh)   # vẽ cạnh
    but.right(90)       # quay phải 90 độ
    canh += 5           # tăng độ dài cạnh mỗi vòng để tạo xoắn

# Giữ màn hình đến khi đóng
turtle.done()
