class RomanToInteger:
    def __init__(self):
        # Bảng giá trị số La Mã
        self.roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman):
        total = 0
        prev_value = 0

        # Duyệt từng ký tự trong chuỗi La Mã từ phải sang trái
        for char in reversed(roman):
            value = self.roman_values[char]

            # Quy tắc:
            # Nếu số hiện tại < số trước đó → trừ
            # Nếu số hiện tại >= số trước đó → cộng
            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total


# Chạy thử
converter = RomanToInteger()

roman_num = input("Nhập số La Mã: ")
integer = converter.convert(roman_num)

print("Giá trị nguyên:", integer)

