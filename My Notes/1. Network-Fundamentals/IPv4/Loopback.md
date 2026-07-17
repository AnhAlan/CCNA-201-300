- 1. Loopback interface
    - Là một interface ảo trên router/switch.
    - Không kết nối với phần cứng vật lý → luôn ở trạng thái up nếu được cấu hình.
    - Dùng cho:
        + Quản lý thiết bị từ xa (SSH/Telnet)
        + Cung cấp IP ổn định cho các giao thức định tuyến (OSPF, BGP, v.v.)

    - Ví dụ:
        + Router(config)# interface loopback0
        + Router(config-if)# ip address 10.1.1.1 255.255.255.0

- 2. Loopback address
    - Là một địa chỉ IP đặc biệt dùng để tự tham chiếu chính thiết bị.
    - Dải chuẩn: 127.0.0.0/8, phổ biến nhất là 127.0.0.1.
    - Dùng cho:
        + Kiểm tra TCP/IP stack (ping 127.0.0.1)
        + Kiểm tra dịch vụ nội bộ không đi ra mạng ngoài
        + Không nhất thiết phải gán cho loopback interface, nhưng thường gán 127.0.0.1 hoặc dải 127.x.x.x cho interface này