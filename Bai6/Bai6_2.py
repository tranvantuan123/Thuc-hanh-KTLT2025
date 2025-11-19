class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong


# Ví dụ sử dụng
hcn = Hinhchunhat(8, 10)
print("Diện tích:", hcn.dien_tich())  # 80
