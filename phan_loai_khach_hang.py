def phan_loai_khach_hang(diem_credit):
    if diem_credit >= 750:
        return "Rủi ro Thấp - Duyệt tự động"
    elif diem_credit >= 600:
        return "Rủi ro Trung bình - Cần thẩm định"
    else:
        return "Rủi ro Cao - Từ chối cấp tín dụng"


# Nhập điểm tín dụng
diem = int(input("Nhập điểm tín dụng (300-850): "))

# Kiểm tra và phân loại
if 300 <= diem <= 850:
    print(phan_loai_khach_hang(diem))
else:
    print("Điểm tín dụng không hợp lệ!")