def tinh_lai_suat_tiet_kiem():
    """Tính tổng số tiền nhận được theo công thức lãi đơn."""

    # Bước 1: Nhập số tiền gốc
    so_tien_goc = float(input("Nhập số tiền gốc: "))

    # Bước 2: Nhập lãi suất năm
    lai_suat_nam = float(input("Nhập lãi suất năm (ví dụ 0.06): "))

    # Bước 3: Nhập thời gian gửi tính bằng năm
    thoi_gian = float(input("Nhập thời gian gửi (năm): "))

    # Bước 4: Tính tổng số tiền theo công thức lãi đơn
    tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)

    # Bước 5: In kết quả
    print("Tổng số tiền nhận được:", tong_tien)

   
 # Gọi hàm để chạy chương trình
tinh_lai_suat_tiet_kiem()