- IPv4 có 32 bit

- Class A: 1 - 127
    - 1.0.0.0 → 126.0.0.0
    - Mỗi network có (2^24 - 2) host / subnet mask
    - 127.0.0.0 → dùng cho loopback (xem file loopback.txt)

- Class B: 128 - 191
    - 128.0.0.0 → 191.255.0.0
    - 2 bit đầu là 10xxxxxx → thuộc Class B
    - Có 2^14 = 16384 network

- Class C: 192 - 223
    - Bit bắt đầu: 110xxxxx
    - 192.0.0.0 → 223.255.255.0
    - Có 2^21 = 2,097,152 network

- Class D: 224 - 239
    - Dùng cho multicast address → gửi đến nhóm thiết bị được chỉ định
    - Ví dụ:
        + 224.0.0.5 → OSPF
        + 224.0.0.6 → tất cả router DR và BDR của OSPF
    - Không chia host/network như các class khác
    - Tiết kiệm băng thông (gửi theo nhóm)
    - 224.0.0.0 → 239.255.255.255
    - Một số subnet dùng cho mục đích đặc biệt

- Class E: 240 - 255
    - 240.0.0.0 → 255.255.255.255
    - Dùng cho nghiên cứu và thử nghiệm

- 3 dải IP private
    - 10.0.0.0/8 → 10.0.0.0 → 10.255.255.255
    - 172.16.0.0/12 → 172.16.0.0 → 172.31.255.255
    - 192.168.0.0/16 → 192.168.0.0 → 192.168.255.255