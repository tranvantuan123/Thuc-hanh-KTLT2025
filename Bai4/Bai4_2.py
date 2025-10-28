S = input("Nhập chuỗi: ")
for ch in S:
    if ch not in [' ', '\t']:  # bỏ qua dấu cách và tab
        print(ch)
