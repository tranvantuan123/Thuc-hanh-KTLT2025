def benefit(t, n, k):
    # t: lãi suất %/tháng
    # n: số vốn ban đầu
    # k: số tháng gửi

    if t < 0 or n <= 0 or k <= 0:
        print("Dữ liệu không hợp lệ!")
        return

    final_money = n * (1 + t/100)**k
    return final_money


# Nhập dữ liệu từ bàn phím
t = float(input("Nhập lãi suất t (%/tháng): "))
n = float(input("Nhập vốn ban đầu n: "))
k = int(input("Nhập số tháng gửi k: "))

result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", result)
