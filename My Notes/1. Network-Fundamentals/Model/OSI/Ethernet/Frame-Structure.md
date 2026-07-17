![alt text](images/Ethernet.Frame.png)

- Preamble (7 bytes)
    - Dùng để đồng bộ tín hiệu giữa bên gửi và bên nhận.

- Start Frame Delimiter (SFD, 1 byte)
    - Xác định điểm bắt đầu của frame dữ liệu.

- Destination MAC (6 bytes)
    - Địa chỉ MAC của thiết bị nhận.

- Source MAC (6 bytes)
    - Địa chỉ MAC của thiết bị gửi.

- Type/Length (2 bytes)
    - Với Ethernet II:
        + Là Type → xác định giao thức tầng trên (ví dụ 0x0800 = IPv4)
    - Với IEEE 802.3:
        + Là Length → xác định độ dài phần payload

- Payload/Data (46–1500 bytes)
    - Dữ liệu thực tế trong mạng (IP, ARP, v.v.)

- Frame Check Sequence (FCS, 4 bytes)
    - Dùng CRC để kiểm tra lỗi dữ liệu.

    - CRC (Cyclic Redundancy Check)
        + Phát hiện lỗi bằng phép chia nhị phân đa thức
        + Dùng một đa thức sinh cố định G(x) để tạo mã kiểm tra

    - Cách hiểu đơn giản:
        + Chia dữ liệu gốc cho đa thức sinh → lấy phần dư
        + Gắn phần dư vào dữ liệu để tạo frame gửi đi

    - Bên nhận:
        + Chia lại frame cho cùng đa thức
        + Nếu dư = 0 → dữ liệu đúng
        + Nếu dư ≠ 0 → dữ liệu bị lỗi

- Ethernet II vs IEEE 802.3

- IEEE 802.3
    - Có trường Length
    - Dùng để chỉ độ dài payload (chuẩn cũ)

- Ethernet II
    - Có trường Type
    - Dùng để xác định giao thức tầng trên (Layer 3)


- Lưu ý quan trọng
    - Payload tối thiểu: 46 bytes
    - Nếu nhỏ hơn → sẽ được padding thêm dữ liệu