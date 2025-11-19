class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Nạp thành công: {amount} VND")
        else:
            print("Số tiền nạp không hợp lệ!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền rút không hợp lệ!")
        elif amount > self.balance:
            print("Số dư không đủ!")
        else:
            self.balance -= amount
            print(f"Rút thành công: {amount} VND")

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("Đổi PIN thành công!")
        else:
            print("PIN cũ không đúng!")


# -------------------------
# Chạy chương trình ATM
# -------------------------
atm = ATM(pin="1234", balance=10000000000)  # Tạo tài khoản với PIN 1234 và số dư 5000

print("Chào mừng bạn đến với ATM!")
input_pin = input("Nhập PIN: ")

if atm.check_pin(input_pin):
    while True:
        print("\nChọn chức năng:")
        print("1. Kiểm tra số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Đổi PIN")
        print("5. Thoát")

        choice = input("Lựa chọn của bạn: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Nhập số tiền muốn nạp: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Nhập số tiền muốn rút: "))
            atm.withdraw(amount)
        elif choice == '4':
            old_pin = input("Nhập PIN cũ: ")
            new_pin = input("Nhập PIN mới: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == '5':
            print("Cảm ơn bạn! Hẹn gặp lại.")
            break
        else:
            print("Lựa chọn không hợp lệ!")
else:
    print("PIN không đúng! Vui lòng thử lại.")
