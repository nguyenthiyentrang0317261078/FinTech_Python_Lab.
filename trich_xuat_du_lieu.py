# Bước 1: Khai báo chuỗi thông tin giao dịch
ma_giao_dich = "GD001-5000000-VND"

# Bước 2: Cắt chuỗi để lấy số tiền giao dịch
so_tien = ma_giao_dich[6:13]

# Bước 3: Chuyển số tiền từ chuỗi sang số nguyên
so_tien = int(so_tien)

# Bước 4: Kiểm tra số tiền bằng cấu trúc if/else
if so_tien >= 5000000:
    print("Giao dịch cần xác thực OTP")
else:
    print("Giao dịch thành công")