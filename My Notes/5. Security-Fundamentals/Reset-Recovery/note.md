- Khi nào cần Reset / Recovery  
- Quên mật khẩu → không thể đăng nhập console hoặc VTY lines  

- Thiết bị bị cấu hình sai → không hoạt động đúng chức năng  
- Xóa toàn bộ cấu hình → đưa về trạng thái mặc định  

- Nâng cấp / hạ cấp IOS  

---

1. Reload  
- Router# reload  
- Thiết bị khởi động lại nhưng vẫn giữ cấu hình hiện tại  

---

2. Xóa cấu hình đã lưu (startup-config)  
- Router# write erase  # hoặc erase startup-config  
- Router# reload  
- Thiết bị khởi động lại không còn cấu hình  
- VTY, VLAN, IP → trở về mặc định  

---

3. Khôi phục mật khẩu / ROMMON  
- Tắt thiết bị rồi bật lại (rút điện và cắm lại)  
- Nhấn liên tục Ctrl + Break khi boot  
- (Laptop có thể dùng Ctrl + Fn + B)  
- Vào chế độ ROMMON  

---

- rommon 1 >  
- rommon 2 > dir flash:  
- Kiểm tra file startup-config còn hay không  

- File size / Checksum / File name  
- Kích thước file / mã kiểm tra / tên file  

- isr4300-universalk9.16.06.04.SPA.bin → file hệ điều hành IOS  
- sigdef-category.xml → file chữ ký hệ thống  
- sigdef-default.xml → file chữ ký mặc định  

---

- rommon 4 > confreg 0x2142  
- Bỏ qua startup-config khi khởi động  

- rommon 5 > reset  
- Khởi động lại thiết bị  

---

- Khi IOS khởi động → vào privileged EXEC mode không cần mật khẩu  
- Router> enable  
- Router# copy startup-config running-config  
- Nạp lại cấu hình cũ vào RAM  

---

- Đổi mật khẩu  
- Router(config)# enable secret 1234  
- Router(config)# username annk secret ccna  

---

- Khôi phục chế độ boot bình thường  
- Router(config)# config-register 0x2102  
- Trở lại chế độ boot mặc định (đọc startup-config)  

---

- Lưu cấu hình và khởi động lại  
- Router# write memory  
- Router# reload  
- Thiết bị chạy lại với cấu hình cũ + mật khẩu mới  

---

- Ghi chú quan trọng  
- 0x2142 → bỏ qua startup-config khi boot  
- 0x2102 → boot bình thường, đọc startup-config  
- Luôn backup cấu hình trước khi reset  

---

- Ý tưởng quy trình  
- confreg 0x2142 → bỏ qua cấu hình khi khởi động  
- reload → vào hệ thống không cần mật khẩu  
- copy startup-config → khôi phục cấu hình cũ  
- đổi mật khẩu → bảo mật lại hệ thống  
- config-register 0x2102 → quay lại chế độ boot bình thường  