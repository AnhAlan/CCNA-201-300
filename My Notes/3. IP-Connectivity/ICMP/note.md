- ICMP (Internet Control Message Protocol)
- Dùng để kiểm tra khả năng kết nối giữa hai thiết bị
- Đo thời gian khứ hồi (Round-Trip Time - RTT):
    - PC1 → PC3 → PC1

---

## 1. Các loại ICMP Message dùng trong Ping

- ICMP Echo Request
    - Gói tin yêu cầu được gửi đến thiết bị đích

- ICMP Echo Reply
    - Gói tin phản hồi từ thiết bị đích

---

## 2. Hành vi mặc định

- Thiết bị Cisco mặc định gửi 5 ICMP Echo Request
- Kích thước gói mặc định là 100 bytes (Cisco)

---

## 3. Ký hiệu kết quả Ping trên Cisco

- ! → Nhận được phản hồi thành công
- . → Không nhận được phản hồi (timeout hoặc thất bại)

---

## 4. Ví dụ kết quả Ping trên Windows

- Reply from 192.168.1.1: bytes=32 time<1ms TTL=128

    - bytes=32
        - Kích thước dữ liệu ICMP nhận được

    - time<1ms
        - Thời gian RTT nhỏ hơn 1 ms

    - TTL=128
        - Giá trị Time To Live còn lại khi gói tin đến nơi

---

## 5. Ghi nhớ quan trọng

- Ping hoạt động ở Layer 3 (Network Layer)

- Lần ping đầu tiên có thể thất bại do quá trình ARP

    - Ban đầu thiết bị chỉ biết địa chỉ IP đích
    - Nó phải dùng ARP để tìm địa chỉ MAC tương ứng
    - Sau khi ARP hoàn tất, các lần ping tiếp theo thường sẽ thành công

- Trong mạng Ethernet, mọi thiết bị cần:
    - Địa chỉ IP (Layer 3)
    - Địa chỉ MAC (Layer 2)

- Ping thành công không có nghĩa tất cả dịch vụ đều hoạt động
    - Chỉ chứng minh thiết bị đích có thể phản hồi ICMP