# hw2_promo_code
# Nhập tên và năm sinh của bạn
ho_ten = input("Nhập tên của bạn: ")
year = input("Nhập năm sinh của bạn: ")
# Lấy 3 chữ cái đầu tiên trong tên của bạn
ten = ho_ten.split()[-1]
ten = ten[0:3].upper() 
# Tạo mã ưu đãi với tên + năm sinh + VIP
ma_uu_dai = ten + "-" + year + "-" + "VIP"\
# In ra kết quả mã ưu đãi
print(f"Mã ưu đãi của bạn là: {ma_uu_dai}")