# Software clock configuration

- **Software clock**: là đồng hồ do IOS quản lý, dùng cho các lệnh `show clock`, ghi log, ...
  - Được cấu hình thủ công bằng lệnh `clock set` (xem phần "Manual time configuration")
  - Nhược điểm: khi thiết bị khởi động lại (reload), software clock sẽ **mất giá trị đã cấu hình** và cần được thiết lập lại (trừ khi được đồng bộ tự động qua NTP)

- **Hardware clock** (calendar): là đồng hồ vật lý (RTC) trên bo mạch, vẫn chạy được kể cả khi thiết bị mất nguồn hoặc reload

## Đồng bộ giữa software clock và hardware clock

```
R2# clock update-calendar
```
- Copy thời gian hiện tại của **software clock** → ghi vào **hardware clock**
- Dùng sau khi vừa cấu hình `clock set` để lưu thời gian đó vào phần cứng, tránh mất khi reload

```
R2# clock read-calendar
```
- Copy thời gian hiện tại của **hardware clock** → nạp vào **software clock**
- Thường dùng ngay sau khi thiết bị khởi động lại, để software clock lấy lại giờ từ hardware clock

## Kiểm tra
```
R2# show clock detail
```
- Cho biết time source hiện tại là gì: `user configured`, `NTP`, hay đang lấy từ hardware clock
