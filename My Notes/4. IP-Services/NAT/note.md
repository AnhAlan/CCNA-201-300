- Host LAN muốn ra Internet thường cần NAT (trừ khi dùng public IP trực tiếp)
- NAT giúp:
    + Cho phép IP private truy cập Internet
    + Giảm số lượng IP public cần dùng
    + Cho phép mạng trùng IP private vẫn giao tiếp được
- NAT là quá trình:
    + Router thay đổi source IP (SNAT) hoặc destination IP (DNAT)
    + Để IP trở nên hợp lệ trên mạng khác
- Router lưu thông tin vào:
    + NAT translation table
    + Để ánh xạ ngược khi gói tin quay về