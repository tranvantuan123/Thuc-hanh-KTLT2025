n = int(input("Nhập số nguyên n: "))
fibo = [0, 1]
while fibo[-1] + fibo[-2] < n:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)
