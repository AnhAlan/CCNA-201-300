# IP Header (IPv4 Header)
- IP header là phần thông tin nằm trong mỗi gói tin IPv4.
- Chứa các thông tin giúp router và thiết bị xử lý, định tuyến và kiểm tra gói tin.

## Các trường chính trong IP Header

- Version
    + Xác định phiên bản IP (IPv4 = 4)

- IHL (Internet Header Length)
    + Độ dài của header IP

- Total Length
    + Tổng kích thước của packet (header + data)

- Identification
    + Dùng để ghép lại các fragment

- Flags
    + Điều khiển fragmentation
        * DF (Don't Fragment)
        * MF (More Fragments)

- Fragment Offset
    + Vị trí của fragment trong gói tin gốc

- TTL (Time To Live)
    + Giảm dần qua mỗi router
    + = 0 → gói tin bị hủy

- Protocol
    + Xác định giao thức tầng trên:
        * TCP (6)
        * UDP (17)
        * ICMP (1)

- Header Checksum
    + Kiểm tra lỗi của header

- Source IP Address
    + IP nguồn

- Destination IP Address
    + IP đích

- Options (optional)
    + Dùng cho mục đích đặc biệt (hiếm dùng)

## Ghi nhớ nhanh
- TTL → chống loop
- Fragmentation → chia nhỏ gói tin
- Protocol → xác định TCP/UDP/ICMP
- Source/Destination → định tuyến