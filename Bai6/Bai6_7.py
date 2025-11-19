
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo bán kính

    def area(self):
        # Diện tích = π * r^2
        return math.pi * self.radius ** 2

    def circumference(self):
        # Chu vi = 2 * π * r
        return 2 * math.pi * self.radius


# Chạy thử
r = float(input("Nhập bán kính hình tròn: "))
circle = Circle(r)

print("Diện tích:", circle.area())
print("Chu vi:", circle.circumference())
