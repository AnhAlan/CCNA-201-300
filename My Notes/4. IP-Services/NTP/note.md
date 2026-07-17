# NTP - Network Time Protocol

## Đồng hồ nội bộ thiết bị
- Các thiết bị mạng đều có đồng hồ nội bộ riêng: router, switch, PC, ...
- Trong IOS (Internetwork Operating System):
  - `show clock` → xem thời gian hiện tại trên thiết bị

## Múi giờ UTC
- Giờ mặc định trên thiết bị là **UTC** (Coordinated Universal Time)
  - Là múi giờ chuẩn được dùng làm mốc chung trên thế giới
  - Việt Nam sử dụng **UTC+7** → giờ Việt Nam luôn nhanh hơn UTC 7 giờ

## show clock detail
Lệnh `show clock detail` cho phép xem chi tiết thời gian của thiết bị, ví dụ:

```
*00:19:44.41 UTC Sat Dec 26 2020
```

- Dấu `*` phía trước: cho biết thời gian này **chưa được xác nhận là chính xác** (chưa đồng bộ với nguồn tin cậy)
- Dù thời gian có thể không chính xác tuyệt đối, người ta vẫn dùng nó để xác định **tính tương đồng thời gian giữa các thiết bị** → phục vụ cho việc khắc phục sự cố (troubleshooting) thông qua syslog

## show logging
Lệnh `show logging` hiển thị:
- Thông báo lỗi
- Cảnh báo bảo mật
- Sự kiện hệ thống
- Log debug

Ví dụ một dòng log:

```
%LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to down
```

- **LINK**: loại sự kiện (facility)
- **3**: mức độ nghiêm trọng (severity level) = Errors
- **UPDOWN**: tên loại thông báo, thể hiện trạng thái vừa thay đổi (up/down)

> Lưu ý: Nếu không đồng bộ thời gian, các thiết bị trong mạng sẽ có thời gian khác nhau → gây khó khăn khi đối chiếu log giữa các thiết bị.

## Cấu hình thời gian thủ công (Manual time configuration)
- Có thể cấu hình thời gian thủ công trên thiết bị bằng lệnh `clock set`

Ví dụ:

```
R2# clock set 14:30:10 27 Dec 2020
```

- `14`: giờ (hour)
- `30`: phút (minutes)
- `10`: giây (second)
- `27 Dec`: ngày và tháng (day month)
- `2020`: năm (year)

- Sau khi cấu hình thủ công, `show clock detail` sẽ hiển thị **time source: user configured**

### Hardware clock vs Software clock
- **Hardware clock** (đồng hồ phần cứng):
  - Là đồng hồ vật lý gắn trên bo mạch thiết bị (RTC - Real Time Clock)
  - Hoạt động độc lập, kể cả khi thiết bị mất nguồn
- **Software clock** (đồng hồ phần mềm):
  - Là đồng hồ do IOS quản lý, dùng cho các lệnh như `show clock`, ghi log, ...
  - Sau khi khởi động lại thiết bị, có thể sai lệch nếu chưa được đồng bộ (ví dụ qua NTP)
- Đây là **2 đồng hồ riêng biệt**, có thể lệch nhau nếu không được đồng bộ với nhau
