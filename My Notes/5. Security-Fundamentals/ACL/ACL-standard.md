## Standard ACLs:
- tiêu chuẩn là chỉ khớp dựa trên Source và destination IP
- có 2 loại:
    * Standard number ACL
    * Standard name ACL

### Standard number ACL
- ACL standard chỉ khớp dựa trên Src / Dst IP
- các ACL được xác định bằng số (ACL 1, ACL 2, ...)
- Các loại ACL khác nhau có phạm vi số khác nhau mà có thể sử dụng được:
    * Standard ACL có thể dụng (1 - 99) hoặc (1300 - 1999)
    * các phạm vi khác thuộc kiểu ACL khác
    * vì vậy cấu hình Standard ACL phải nằm trong phạm vi đó
- basic command:
    * R1(config)# access-list "number" {deny | permit} ip 'wild-card'
    * ví dụ: R1(config) access-list 1 deny 1.1.1.1 0.0.0.0
    * tức từ chối 1.1.1.1/32 tức 1 host duy nhất
    * note: nếu cấu hình không thêm wild-card thì router sẽ tự động thêm /32
    * hoặc: access-list 1 deny host 1.1.1.1 - lệnh tương tự
    * sau đó ngoài 1.1.1.1/32 tất cả mạng khác đều được chấp nhận:
        * R1(config)# access-list 1 permit any 
        * hoặc R1(config)# access-list 1 permit 0.0.0.0 255.255.255.255
    * note (ghi chú) cho ACL:
        * access-list 1 remark ## marketing ##
- áp dụng vào ACL và interface:
    * R1(config-if)# ip access-group 1 {in / out}
    * khi này interface đó sẽ lấy ACL đó áp dụng vào
- lưu ý:
    * nên áp dụng ACL vào giao diện gần đích nhất - tức gần mạng đích nhất
- có thể bỏ mục ACL number:
    * R1(config)# no access-list 1 deny 192.168.3.0 0.0.0.255 // bỏ mục này ra khỏi ACL number

### Standard name ACL
- ACL name vẫn chỉ khớp với Src / đích IP
- nhưng ACL được xác định bằng tên (BLOCK_BOB, ICPC_NOTE, ...) - có thể đặt tên là số nhưng khuyên không nên đặt
- ACL name được cấu hình bằng cách vào chế độ "Standard named ACL config mode" sau đó mới cấu hình từng mục ACL
    * R1(config)# ip access-list standard *acl name*
    * R1(config-std-nacl)# [entry-number] {deny | permit} *ip wild-card*
    * ví dụ:
        * R1(config)# ip acess-list standard icpc
        * R1(config-sdt-nacl)# 5 deny 1.1.1.1
        * R1(config-sdt-nacl)# 10 permit any
        * R1(config-sdt-nacl)# remark ## note ##
        * R1(config)# int g0/0
        * R1(config-if)# ip access-group icpc
        * R1# show access-list
- có thể xóa mục ACL với *number* của mục đó
    * R1(config-sdt-nacl)# no 10 // bỏ lệnh 10 permit any
    * có thể thêm mục khác với số 10 vừa bỏ
    * R1(config-sdt-nacl)# 10 deny 192.168.2.0 0.0.0.255
- mục địch đặt 2 mục liên tiếp khoảng cách là 10 (hoặc lớn hơn) là vì để sau này thêm mục khác ở giữa ta chỉ việc chèn số giữa 2 mục đó
    * có mục 10 và 20 ta muốn thêm mục mà ưu tiên nó dưới 10 trên 20 thì tạo mục 15 và thêm vào
    * vì vậy việc đặt các mục là các số liên tiếp là ý tồi tệ
- Lưu ý:
    * Nếu cấu hình Named Standard ACL mà không chỉ định sequence number, IOS sẽ tự động gán các số 10, 20, 30, ... (bội số của 10).
    * Khi dùng `show ip access-lists`, các mục có thể không hiển thị theo thứ tự sequence number.
    * IOS có thể tự tối ưu cách lưu trữ và hiển thị các ACE, đặc biệt đối với các mục `/32` (host).
    * Việc hiển thị khác thứ tự **không làm thay đổi thứ tự xử lý ACL**. Router vẫn đánh giá các ACE theo sequence number (thứ tự logic).
    * Packet Tracer thường không mô phỏng hành vi tối ưu này nên các ACE sẽ hiển thị đúng theo sequence number.
```text
R2#show ip access-lists

Standard IP access list TO_10.0.1.0/24
    30 permit 192.168.1.1
    10 deny   192.168.2.1
    20 permit 192.168.2.0, wildcard bits 0.0.0.255
    40 deny   192.168.1.0, wildcard bits 0.0.0.255
    50 permit any
```
#### Tại sao IOS hiển thị không theo sequence number?

- IOS có thể tối ưu việc lưu trữ và hiển thị các ACE (*Access Control Entry*) để cải thiện hiệu quả xử lý, đặc biệt với các mục **host (`/32`)**.
- Đây chỉ là thay đổi về **cách hiển thị**, **không phải** thay đổi thứ tự đánh giá ACL.
- Router vẫn áp dụng ACL theo **sequence number** (`10 → 20 → 30 → ...`), vì vậy kết quả lọc gói tin không thay đổi.
- Hành vi này có thể gặp trên cả **Standard Named ACL** và **Standard Numbered ACL**, tùy phiên bản Cisco IOS.
- **Cisco Packet Tracer** thường không mô phỏng cơ chế tối ưu này nên các ACE sẽ hiển thị đúng theo sequence number.
- chủ yếu để tối ưu lookup tăng tốc độ xử lý packet
> **Lưu ý:** Không nên dựa vào thứ tự hiển thị của `show ip access-lists` để suy ra thứ tự xử lý ACL. Nếu cần kiểm tra, hãy dựa vào **sequence number** của từng ACE.
        