- Đây là gói tin được gửi đến tất cả các host trong cùng một mạng (subnet).
    - Mục đích: thông báo, tìm thiết bị, ARP, v.v.
    - Mọi host trong subnet đều nhận và xử lý gói broadcast.

- 1. Limited Broadcast
    - 255.255.255.255

- 2. Subnet Broadcast
    - Gửi đến tất cả host trong một subnet cụ thể
    - Có thể route được nếu router cho phép
    - Cách xác định: broadcast = địa chỉ mạng OR (NOT subnet mask)

    - Ví dụ: 192.168.1.0/26 → mask 255.255.255.192
        + Network: 192.168.1.0
        + Host đầu tiên: 192.168.1.1
        + Host cuối: 192.168.1.62
        + Broadcast: 192.168.1.63
        + Subnet tiếp theo: 192.168.1.64/26 → broadcast = 192.168.1.127

- 3. Ghi chú
    - Nhiều broadcast không cần thiết sẽ làm chậm mạng
    - Cách giảm: giảm lưu lượng, chia mạng nhỏ hơn, dùng VLAN, VLSM