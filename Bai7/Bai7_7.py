# Mở file
with open('D:/a.txt', 'r', encoding='utf-8') as file:
    num_lines = sum(1 for line in file)  # Đếm từng dòng

print("Số dòng trong file:", num_lines)
