#  bai1 hw1_billsplit.py

# Nhập tổng hóa đơn (X), phần trăm tip (Y), số người chia (N)
print("--- TỔNG HÓA ĐƠN ---")
X = float(input("Nhập tổng hóa đơn (X, đồng): "))
Y = float(input("Nhập phần trăm tip (Y, %): "))
N = float(input("Nhập số người chia (N): "))

# Tính tổng tiền tip
tien_tip = X * Y / 100

# Tính tiền tổng hóa đơn sau khi cộng tip
tong_tien = X + tien_tip

# TÍnh số tiền mỗi người phải trả, làm tròn đến số nguyên
so_tien_moi_nguoi = round(tong_tien / N)

#In kết quả
print(f"\n Tổng hóa đơn: {X:,.0f} đồng")
print(f"Tiền tip ({Y}%): {tien_tip:,.0f} đồng")
print(f"Số người chia: {N}")
print(f"Mỗi người phải trả: {so_tien_moi_nguoi:,.0f} đồng")