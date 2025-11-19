class StringClass:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.string.upper())


# Chạy thử class
obj = StringClass()
obj.get_String()
obj.print_String()
