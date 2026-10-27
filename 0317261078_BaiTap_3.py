# Thông số ban đầu
V_goc = 20.0  # Đơn vị: Tỷ VNĐ

# Danh sach kịch bản
delta_Ex = [-0.03, 0.0, 0.03]                   # Tỷ giá USD/VND (-3%, 0%, +3%)
delta_Ir = [-0.02, -0.01, 0.01, 0.02]           # Lãi suất (-2%, -1%, +1%, +2%)

print("=== MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ DANH MỤC (TỶ VNĐ) ===")
print(f"Vốn danh mục ban đầu: {V_goc:.2f} Tỷ VNĐ\n")

# In tiêu đề cột (các kịch bản Tỷ giá)
header = f"{'Thay đổi Lãi suất (Dòng) \\ Tỷ giá (Cột)':<40} | " + " | ".join([f"{ex*100:>5.1f}%" for ex in delta_Ex])
print(header)
print("-" * len(header))

# Vòng lặp lồng nhau
for ir in delta_Ir:
    # In tiêu đề dòng (kịch bản Lãi suất)
    row_str = f"Lãi suất: {ir*100:+5.1f}%{'':<22} | "
    values = []
    
    for ex in delta_Ex:
        # Công thức tính giá trị danh mục mới
        v_moi = V_goc * (1 + 1.5 * ex - 2.0 * ir)
        values.append(f"{v_moi:>6.2f} Tỷ")
    
    row_str += " | ".join(values)
    print(row_str)