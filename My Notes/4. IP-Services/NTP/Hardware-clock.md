# Hardware clock (Calendar)

- **Hardware clock** (còn gọi là **calendar**): đồng hồ vật lý (RTC) gắn trên bo mạch thiết bị, vẫn hoạt động ngay cả khi thiết bị mất nguồn hoặc reload

## Cấu hình hardware clock

```
R2# calendar set 14:35:00 27 DEC 2020
```
- `14:35:00`: giờ : phút : giây
- `27 DEC 2020`: ngày tháng năm
- Lệnh này cấu hình trực tiếp cho **hardware clock**, khác với `clock set` (dùng để cấu hình **software clock**)

## Kiểm tra hardware clock

```
R2# show calendar
```
- Hiển thị thời gian hiện tại đang được lưu trên hardware clock

## Đồng bộ giữa clock (software) và calendar (hardware)
- Nên đồng bộ **software clock** và **hardware clock** với nhau để tránh lệch giờ

| Lệnh | Chức năng |
|---|---|
| `clock update-calendar` | Đồng bộ **calendar (hardware)** theo **clock (software)** — copy giờ từ software clock ghi vào hardware clock |
| `clock read-calendar` | Đồng bộ **clock (software)** theo **calendar (hardware)** — copy giờ từ hardware clock nạp vào software clock |
