- Duplex = cách hai thiết bị giao tiếp trên cùng một cổng mạng
- Tầng liên quan: Layer 1 / 2 (Physical + Data Link)
- Ảnh hưởng: tốc độ truyền + khả năng xảy ra collision

---

## 1. Half Duplex

- Truyền dữ liệu một chiều tại một thời điểm
- Ví dụ: bộ đàm → phải nói và nghe luân phiên
- Trước đây dùng với hub, dễ xảy ra collision, cần CSMA/CD
- Tốc độ: 10/100 Mbps

---

## 2. Full Duplex

- Truyền hai chiều đồng thời
- Ví dụ: điện thoại → nói và nghe cùng lúc
- Không xảy ra collision
- Cần switch + cáp chuẩn (Cat5e/Cat6 trở lên)
- Tốc độ: 10/100/1000 Mbps

---

## 3. Auto Duplex

- Thiết bị tự động thương lượng duplex và speed
- Lệnh kiểm tra:
    - show interfaces → xem duplex/speed
- Cấu hình interface:
    - duplex full/auto
    - speed 100/auto

- Lưu ý:
    - Tránh mismatch duplex (Full ↔ Half)
    - Gây giảm hiệu suất + tăng lỗi collision

---

## 4. Cấu hình

- Switch(config)#int fa0/1
- Switch(config-if)#duplex full (khuyến nghị)
- Switch(config-if)#speed 100 (FastEthernet chỉ 100 Mbps)

- Nguyên tắc:
    - Hai thiết bị phải cùng duplex để ổn định
    - Dùng auto khi thiết bị mới hỗ trợ tốt
    - Nếu hệ thống cũ → cấu hình tay cho đồng nhất

- Ethernet:
    - Ethernet / FastEthernet: half / full / auto
    - GigabitEthernet: thường full / auto

- Serial:
    - Luôn full duplex
    - Không liên quan duplex, chỉ cấu hình DTE/DCE

---

## 5. Ghi nhớ

- Hai thiết bị phải cùng chế độ duplex:
    - auto - auto (an toàn nhất)
    - manual - manual (ổn định nếu cấu hình chuẩn)

- Sai lệch duplex → giảm tốc độ + lỗi mạng + collision cao