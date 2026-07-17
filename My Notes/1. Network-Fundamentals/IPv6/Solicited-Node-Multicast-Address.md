# Solicited-Node Multicast Address

- Là một loại địa chỉ Multicast đặc biệt trong IPv6, bắt buộc phải có trên mỗi giao diện (interface) mạng.
- **Cách tạo tự động:** Hệ thống tự động tạo địa chỉ này bằng cách kết hợp Tiền tố (Prefix) cố định với 24 bits cuối của địa chỉ IPv6 Unicast/Anycast.
- **Mục đích ra đời:** IPv6 **không còn dùng Broadcast**. Địa chỉ này được tạo ra để thay thế cơ chế Broadcast tốn băng thông của IPv4 bằng một cơ chế Multicast thông minh hơn.

---

# 1. Cấu trúc và Công thức tạo

Một địa chỉ Solicited-Node Multicast luôn có độ dài 128 bits, chia làm 2 phần:

- **Phần cố định (104 bits đầu):** Luôn là `FF02::1:FF00:0/104` (dạng viết đầy đủ là `FF02:0000:0000:0000:0000:0001:FF00:0000/104`).
- **Phần biến đổi (24 bits cuối):** Được bê nguyên từ **24 bits cuối** (tương đương **6 ký tự Hexa cuối**) của địa chỉ IPv6 Unicast/Anycast tương ứng.

> **Công thức tổng quát:**
> `FF02::1:FF` + `[6 ký tự Hex cuối của IPv6 Unicast]`

---

# 2. Ví dụ chi tiết từng bước

### Ví dụ 1: Tạo từ địa chỉ IPv6 Unicast
* Giả sử PC A có địa chỉ IPv6 Unicast: `2001:db8:1:1::2aa:ff28:9c5a`
* Ta viết dạng đầy đủ phần đuôi: `...:02aa:ff28:9c5a`
* Lấy **24 bits cuối** (6 ký tự Hex cuối): `28:9c5a`
* Ghép vào phần cố định:
  $$\text{Solicited-Node Multicast} = \text{FF02::1:FF} + \text{28:9c5a} = \text{FF02::1:FF28:9C5A}$$

### Ví dụ 2: Ánh xạ sang địa chỉ MAC Multicast ở Lớp 2 (Data Link Layer)
Để gửi được gói tin trong mạng LAN, địa chỉ IPv6 Multicast này bắt buộc phải được chuyển đổi sang địa chỉ MAC Multicast ở Lớp 2:
* **Quy tắc:** Địa chỉ MAC Multicast IPv6 luôn bắt đầu bằng `33:33:FF:` + `[24 bits cuối]`.
* Mạng sẽ chuyển `FF02::1:FF28:9C5A` $\rightarrow$ Địa chỉ MAC Multicast tương ứng: `33:33:FF:28:9C:5A`.

---

# 3. Giải thích rõ: Vì sao IPv6 lại cần nó? (So sánh với IPv4)

### Bối cảnh IPv4 (Dùng Broadcast - Kém hiệu quả)
Khi Máy A muốn tìm địa chỉ MAC của Máy B (biết IP của B là `192.168.1.5`):
1. Máy A gửi gói tin **ARP Request** đến địa chỉ Broadcast `255.255.255.255` (Lớp 3) và `FF:FF:FF:FF:FF:FF` (Lớp 2).
2. **TẤT CẢ** các máy tính trong cùng mạng LAN (máy B, C, D, E...) đều bị ngắt (interrupt) CPU để mở gói tin ra xem.
3. Máy C, D, E phát hiện không phải IP của mình nên ngậm ngùi bỏ qua $\rightarrow$ **Gây lãng phí tài nguyên xử lý của toàn mạng.**

### Giải pháp IPv6 (Dùng Solicited-Node Multicast - Tối ưu)
IPv6 bỏ hoàn toàn ARP và Broadcast, thay bằng giao thức **Neighbor Discovery Protocol (NDP)** kết hợp với Solicited-Node Multicast:
1. Máy B tự động đăng ký gia nhập nhóm Multicast dựa trên đuôi IP của nó (ví dụ đuôi `28:9C5A`).
2. Khi Máy A muốn tìm MAC của B, A không gửi Broadcast cho cả làng, mà chỉ gửi một gói **ICMPv6 Neighbor Solicitation (NS)** đến địa chỉ Solicited-Node Multicast `FF02::1:FF28:9C5A`.
3. Nhờ địa chỉ MAC tương ứng `33:33:FF:28:9C:5A`, card mạng (NIC) của các máy C, D, E thấy không khớp nhóm thì **lọc bỏ ngay từ phần cứng** mà không cần làm phiền CPU.
4. Chỉ duy nhất Máy B (có cùng đuôi `28:9C5A`) mở gói tin và trả lời $\rightarrow$ **Không ảnh hưởng đến các máy khác.**

---

# 4. Hai Ứng dụng quan trọng nhất

### A. Tìm địa chỉ MAC (Neighbor MAC Resolution)
- Thay thế hoàn toàn cho ARP trong IPv4.
- Dùng cặp thông điệp ICMPv6: **Neighbor Solicitation (NS)** (Hỏi) và **Neighbor Advertisement (NA)** (Trả lời).

### B. Phát hiện trùng địa chỉ IP (Duplicate Address Detection - DAD)
- Trước khi một máy tính chính thức sử dụng một địa chỉ IPv6 mới, nó sẽ gửi một gói tin NS đến địa chỉ Solicited-Node Multicast của **chính địa chỉ đó**.
- Nếu có thiết bị khác phản hồi lại $\rightarrow$ Địa chỉ bị trùng, máy sẽ không dùng địa chỉ đó nữa.
- Nếu không ai phản hồi $\rightarrow$ Địa chỉ an toàn để sử dụng.