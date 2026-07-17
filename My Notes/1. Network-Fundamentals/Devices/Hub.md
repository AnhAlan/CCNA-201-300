# Hub (Network Hub)
## Khái niệm
- Hub là thiết bị mạng hoạt động ở **Layer 1 (Physical Layer)**.
- Dùng để kết nối nhiều thiết bị trong cùng một mạng LAN.

## Cách hoạt động
- Nhận tín hiệu từ một cổng (port).
- Sao chép tín hiệu đó và phát ra **tất cả các cổng còn lại**.
- Không phân biệt thiết bị đích.

## 📡 Đặc điểm quan trọng
- Không có khả năng học MAC address.
- Không có bảng MAC (MAC table).
- Không có routing hay switching logic.
- Hoạt động kiểu “broadcast tất cả”.

## Nhược điểm
- Dễ gây **collision (xung đột tín hiệu)**.
- Băng thông bị chia sẻ cho toàn bộ thiết bị.
- Không bảo mật (ai cũng nhận được dữ liệu).
- Hiệu suất thấp khi nhiều thiết bị.

## Collision Domain
- Toàn bộ hub = **1 collision domain duy nhất**.
- Càng nhiều thiết bị → càng dễ va chạm dữ liệu.

## Half-duplex
- Chỉ có thể gửi hoặc nhận tại một thời điểm.
- Không thể truyền song song 2 chiều.

## So sánh nhanh
- Hub → Layer 1 → Broadcast toàn bộ → không thông minh
- Switch → Layer 2 → dùng MAC → thông minh hơn

## Tình trạng hiện nay
- Gần như **đã lỗi thời (obsolete)**.
- Được thay thế hoàn toàn bởi switch.
- Chỉ còn trong mô phỏng hoặc bài học cơ bản.

## Ghi nhớ nhanh
- Hub = “copy tất cả ra mọi cổng”
- Không MAC, không logic
- 1 collision domain
- Half-duplex