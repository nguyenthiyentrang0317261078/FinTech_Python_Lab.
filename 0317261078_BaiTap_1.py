# Khởi tạo các thông số đầu vào
tuoi = 25
so_du = 0.0
tien_gui = 60000000.0
lai_suat = 0.10
tang_tien_gui = 0.08
muc_tieu = 10000000000.0
nam = 1

print("=== BÁO CÁO MÔ PHỎNG KẾ HOẠCH HƯU TRÍ TỰ ĐỘNG ===")
print(f"Mục tiêu tài sản: {muc_tieu:,.0f} VNĐ\n")
print(f"{'Năm':<5} | {'Tuổi':<5} | {'Tiền gửi mới':<18} | {'Tiền lãi phát sinh':<20} | {'Dư nợ/Tài sản cuối năm'}")
print("-" * 85)

# Vòng lập tính toán cho đến khi đạt mục tiêu
while so_du < muc_tieu:
    tien_lai = so_du * lai_suat
    so_du = so_du + tien_lai + tien_gui
    
    # In thông tin của năm hiện tại
    print(f"{nam:<5} | {tuoi:<5} | {tien_gui:>14,.0f} VNĐ | {tien_lai:>16,.0f} VNĐ | {so_du:>20,.0f} VNĐ")
    
    # Cập nhật cho năm tiếp theo
    tien_gui *= (1 + tang_tien_gui)
    tuoi += 1
    nam += 1

print("-" * 85)
print(f"KẾT LUẬN: Khách hàng sẽ đạt mục tiêu nghỉ hưu sau {nam - 1} năm (lúc {tuoi - 1} tuổi).")