- Xử lý gói tin trong router
    * Gói tin đến đúng mạng đích → chuyển tiếp đến đích
    * Gói tin đến chính router → xử lý tại router (local processing)
    * Gói tin đi ra ngoài LAN → gửi tới next-hop

- Các bước chọn route protocol để gửi dữ liệu

1. **Longest Prefix Match (quan trọng nhất)**
- Chọn route có subnet mask dài nhất (/ giá trị lớn nhất)
- Nghĩa là match cụ thể nhất, không phải “gần nhất”
- Ví dụ:
    * IP đích: 10.1.1.19
    * Các route:
        * RIP: 10.1.1.16/28
        * OSPF: 10.1.1.0/24
        * EIGRP: 10.1.0.0/26 (KHÔNG match)
    *   Các route hợp lệ:
        * 10.1.1.16/28
        * 10.1.1.0/24
    * Chọn: 10.1.1.16/28
    * (vì /28 dài hơn /24 → cụ thể hơn)

2. **Administrative Distance (AD)**

- Chỉ dùng khi prefix length bằng nhau
- Chọn route có AD thấp nhất (đáng tin cậy hơn)

3. **Metric**
- Chỉ dùng khi AD cũng bằng nhau
- Chọn route có metric thấp nhất (đường tốt hơn)