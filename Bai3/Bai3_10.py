import math

def Tinh(R):
    # Kiểm tra bán kính hợp lệ
    if R <= 0:
        print("Bán kính phải lớn hơn 0!")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R

    print("Chu vi =", chu_vi)
    print("Diện tích =", dien_tich)

# Nhập bán kính từ bàn phím
R = float(input("Nhập bán kính R: "))
Tinh(R)
