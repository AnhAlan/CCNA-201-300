- Serial là cáp WAN, thường sử dụng kết nối Point-To-Point -> hiện nay hầu như không còn được sử dụng.
- Nhà cung cấp dịch vụ Internet (ISP) đóng vai trò là DCE.
- Thiết bị của bạn (router) đóng vai trò là DTE.

- 1. Serial DCE (Data Circuit-terminating Equipment)
- Thiết bị cung cấp tín hiệu clock cho kết nối.
- Ví dụ: Router kết nối tới CSU/DSU.
- Cáp được kết nối vào cổng DCE, router nhận clock từ DCE.
- Lệnh trên Cisco để kiểm tra:
    + Router#show controllers serial0/1/0
- Kết quả sẽ hiển thị DCE hoặc DTE.
- Nếu là DCE, bạn có thể thiết lập clock rate:
    + Router(config)#int serial 0/1/0
    + Router(config-if)#clock rate 64000

- Lệnh này chỉ áp dụng cho các interface DCE.
- 64000 = 64.000 bit/giây (64 Kbps)
    + 64.000 bit được truyền trong mỗi giây.
    + Đây cũng là tốc độ clock mà DCE truyền đi.

2. Serial DTE (Data Terminal Equipment)
- Thiết bị nhận tín hiệu clock từ DCE.
- Thông thường đây là router ở đầu còn lại của kết nối.
- Không cần cấu hình clock rate vì DTE không cung cấp tín hiệu clock.
- Serial cần DCE/DTE vì...
- Dữ liệu được truyền từng bit một bằng tín hiệu clock riêng.
- Không có clock được tích hợp sẵn trong tín hiệu.
- Cần một thiết bị tạo clock (DCE).
- Mục đích của DCE và DTE trong kết nối WAN Serial là đồng bộ hóa việc truyền dữ liệu.
- Ghi nhớ:
    + DCE cung cấp tín hiệu clock → bắt buộc cấu hình trên DCE.
    + DTE nhận tín hiệu → không cần cấu hình clock.
    + Cách phân biệt cáp: DCE thường có nhãn trên đầu kết nối.
- Các loại cáp khác tự động đồng bộ hóa (mỗi loại sẽ có cơ chế đồng bộ khác nhau) mà không cần cấu hình thủ công.