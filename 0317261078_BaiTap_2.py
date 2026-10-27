# Thông số đầu vào
F = 1000000      # Mệnh giá
c = 0.09         # Lãi suất coupon (9%/năm)
N = 10           # Thời hạn (năm)
y = 0.085        # Lãi suất kỳ vọng (8.5%/năm)

# 1. Số tiền lãi coupon hàng năm
C = F * c

# 2. Tổng giá trị hiện tại (PV) của các khoản lãi coupon
tong_pv_coupon = 0.0
for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c

# 3. Giá trị hiện tại (PV) của mệnh giá goc
pv_f = F / ((1 + y) ** N)

# 4. Giá trị lý thuyết của trái phiếu (P0)
gia_trai_phieu = tong_pv_coupon + pv_f

# Đánh giá loại giá trái phiếu
if gia_trai_phieu > F:
    danh_gia = "Cao hơn mệnh giá (Premium)"
elif gia_trai_phieu == F:
    danh_gia = "Đúng mệnh giá (Par)"
else:
    danh_gia = "Thấp hơn mệnh giá (Discount)"

# In kết quả
print("=== ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP ===")
print(f"Số tiền lãi coupon hàng năm (C): {C:,.0f} VNĐ")
print(f"Tổng PV lãi coupon: {tong_pv_coupon:,.2f} VNĐ")
print(f"PV mệnh giá gốc: {pv_f:,.2f} VNĐ")
print(f"Giá lý thuyết trái phiếu (P0): {gia_trai_phieu:,.2f} VNĐ")
print(f"Đánh giá giá trị trái phiếu: {danh_gia}")