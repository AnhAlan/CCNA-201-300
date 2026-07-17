# Trạng thái Interface Switch

## Lệnh
```bash
Switch#show int fa0/1
```

---

## Trạng thái
- FastEthernet0/1 is down - interface đang bị down về vật lý hoặc bị shutdown
- Line protocol is down (disabled) - giao thức Layer 2 không hoạt động

---

## Thông tin phần cứng
- Hardware: Lance - loại phần cứng của interface
- MAC Address: 000a.4161.5101 - địa chỉ MAC của interface
- BIA: 000a.4161.5101 - MAC gốc từ nhà sản xuất

---

## Hiệu năng
- Bandwidth: 100000 Kbit (100 Mbps) - tốc độ cấu hình của interface
- Delay: 1000 usec - độ trễ xử lý nội bộ
- Reliability: 255/255 - độ ổn định của interface (255 là tốt nhất)
- TX Load: 1/255 - mức tải gửi ra (rất thấp)
- RX Load: 1/255 - mức tải nhận vào (rất thấp)

---

## Cấu hình interface
- Encapsulation: ARPA - kiểu đóng gói frame Ethernet
- Loopback: not set - không bật chế độ loopback
- Keepalive: 10 sec - thời gian kiểm tra kết nối định kỳ
- Duplex: Half-duplex - chỉ gửi hoặc nhận tại một thời điểm
- Speed: 100 Mb/s - tốc độ đường truyền hiện tại

---

## Điều khiển luồng
- Input flow-control: off - không điều khiển luồng dữ liệu vào
- Output flow-control: off - không điều khiển luồng dữ liệu ra

---

## Thông tin ARP
- ARP Type: ARPA - kiểu đóng gói ARP
- ARP Timeout: 04:00:00 - thời gian hết hạn của bản ghi ARP

---

## Hoạt động
- Last input: 00:00:08 - thời gian từ lần nhận gói gần nhất
- Last output: 00:00:05 - thời gian từ lần gửi gói gần nhất
- Output hang: never - không có tình trạng treo khi gửi

---

## Thống kê input
- Packets input: 956 - tổng số gói tin nhận được
- Bytes received: 193351 - tổng số byte đã nhận
- Broadcasts received: 956 - số gói broadcast nhận được
- Runts: 0 - gói tin quá nhỏ (không có lỗi)
- Giants: 0 - gói tin quá lớn (không có lỗi)
- CRC errors: 0 - lỗi kiểm tra dữ liệu (không có)
- Frame errors: 0 - lỗi khung dữ liệu
- Overrun: 0 - tràn bộ đệm phần cứng
- Ignored: 0 - gói bị bỏ qua do thiếu tài nguyên

---

## Thống kê output
- Packets output: 2357 - tổng số gói đã gửi
- Bytes output: 263570 - tổng số byte đã gửi
- Output errors: 0 - không có lỗi khi gửi
- Collisions: 0 - không có va chạm tín hiệu
- Interface resets: 10 - số lần interface bị reset

---

## Tổng kết lỗi
- No input errors - không có lỗi khi nhận
- No CRC errors - không có lỗi dữ liệu
- No frame errors - không có lỗi frame
- No output buffer failures - không lỗi bộ nhớ đệm
- No late collisions - không có va chạm trễ

---

## Hiểu nhanh
- down/down - lỗi cáp hoặc port vật lý
- half-duplex - chế độ truyền cũ
- zero errors - kết nối Layer 1 tốt
- broadcast cao - bình thường trong LAN