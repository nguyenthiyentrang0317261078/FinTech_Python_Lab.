# bai2 hw2_roi.py

print("--- TÍNH LÃI SUẤT SINH LỜI ---")
# Nhập tổng vốn ban đầu và tổng giá trị bán ra
von_ban_dau = float(input("Nhập tổng số vốn ban đầu (Intitial Investment): "))
gia_tri_ban_ra = float(input(" Nhập tổng số giá trị bán ra ( Final Value): "))

#tính lợi nhuận ròng (Net Profit)
loi_nhuan_rong = gia_tri_ban_ra - von_ban_dau

#tính tỷ lệ ROI (%)
roi = (loi_nhuan_rong / von_ban_dau) * 100

#In kết quả
print(f"\n Tổng vốn ban đầu: {von_ban_dau:,.0f} đồng")
print(f" Tổng giá trị bán ra: {gia_tri_ban_ra:,.0f} đồng")
print(f" Lợi nhuận ròng: {loi_nhuan_rong:,.0f} đồng")
print(f" Tỷ lệ ROI: {roi:.2f}%")