# hw1_email_masking
email_unmask = input("Hãy nhập email của bạn: ")
part = email_unmask.split("@")
# Dùng split để tách ra 
username = part[0] 
tenmien = part[1]
# Dùng sclicing để cắt lấy 3 kí tự đầu tiên của email
email_masked = username[0:3] + "***@" + tenmien
# In ra và kiểm tra kết quả
print(f"Email của bạn là: {email_masked}")