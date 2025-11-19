class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        # Tách chuỗi thành danh sách các từ
        words = self.text.split()
        # Đảo ngược danh sách từ
        words.reverse()
        # Ghép lại thành chuỗi
        return " ".join(words)


# Chạy thử
input_str = 'hello .py'
obj = ReverseWords(input_str)

print("Kết quả:", obj.reverse())
