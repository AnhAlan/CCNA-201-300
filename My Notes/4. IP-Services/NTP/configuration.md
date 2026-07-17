# NTP Configuration

# nslookup

- Sử dụng trên PC để kiểm tra DNS.
- Cho phép phân giải:
    * Domain name → IP address (Forward lookup)
    * IP address → Domain name (Reverse lookup)

Ví dụ:

```bash
> nslookup time.google.com

> nslookup 8.8.8.8
```

---

# NTP Configuration

## show ntp associations

```bash
R1# show ntp associations
```

- Hiển thị các NTP server mà router đang cấu hình và trạng thái kết nối.

Ví dụ:

```
address             Ref clock       st       when       poll    reach    delay     offset     disp
*~216.239.35.0      .GOOG.          1        43         64      17       62.007    1401.54    0.918
+~216.239.35.8      .GOOG.          1        43         64      17       64.007    1416.54    0.939
```

## Ký hiệu trạng thái

| Ký hiệu | Ý nghĩa |
|-|-|
| `*` | Sys.peer - NTP server đang được router sử dụng |
| `+` | Candidate - NTP server có thể được chọn nếu server hiện tại lỗi |
| `#` | Server được chọn nhưng không phải sys.peer |
| `-` | Outlier - Nguồn thời gian có sai lệch lớn |
| `x` | Falseticker - Nguồn thời gian không đáng tin cậy |
| `~` | NTP server được cấu hình thủ công |

---

## Các thông số

| Thông số | Ý nghĩa |
|-|-|
| address | Địa chỉ IP của NTP server |
| Ref clock | Nguồn thời gian tham chiếu |
| st | Stratum của NTP server |
| when | Thời gian kể từ lần cập nhật cuối |
| poll | Khoảng thời gian giữa các lần gửi request NTP |
| reach | Trạng thái khả năng kết nối |
| delay | Độ trễ mạng tới NTP server |
| offset | Sự khác biệt thời gian giữa router và NTP server |
| disp | Độ sai lệch dự đoán của nguồn thời gian |

Ví dụ:

```
.GOOG.
```

- Cho biết NTP server sử dụng nguồn thời gian của Google.

```
st 1
```

- NTP server có Stratum 1.

---

# show ntp status

```bash
R1# show ntp status
```

- Kiểm tra trạng thái đồng bộ thời gian.

Ví dụ:

```
Clock is synchronized, stratum 2
```

Ý nghĩa:

- Router đã đồng bộ với NTP server.
- Router có Stratum 2.

Lưu ý:

- Nếu router đồng bộ với NTP server Stratum 1:
    * Router sẽ trở thành Stratum 2.
- Router có thể cung cấp thời gian cho các thiết bị khác.

---

# show clock detail

```bash
R1# show clock detail
```

- Hiển thị:
    * Thời gian hiện tại.
    * Nguồn thời gian.
    * Trạng thái đồng bộ.

---

# Hardware Clock và Software Clock

## Hardware Clock

- Là đồng hồ phần cứng của thiết bị.
- Hoạt động bằng pin CMOS.
- Lưu giữ thời gian kể cả khi thiết bị tắt.

Khi router khởi động:

```
Hardware Clock
       |
       |
Software Clock
```

- Hardware clock được dùng để khởi tạo software clock.

---

# NTP Design trong mạng

## Mạng nhỏ

- Có thể cho router đồng bộ trực tiếp với public NTP server.

Ví dụ:

```
Router
  |
  |
Google NTP Server
```

---

## Mạng lớn

Không nên:

```
Tất cả router
      |
      |
Internet NTP Server
```

Vì:
- Tốn tài nguyên.
- Phụ thuộc Internet.

Nên thiết kế:

```
        Public NTP Server
              |
              |
        Core Router
              |
      ----------------
      |              |
    Router        Router
```

- Chỉ một số router đồng bộ Internet.
- Các router còn lại đồng bộ NTP nội bộ.

---

# NTP Source Interface

## Cấu hình Loopback Interface

```bash
R1(config)# interface loopback0
R1(config-if)# ip address 10.1.1.1 255.255.255.255
```

---

## Chọn nguồn gửi NTP

```bash
R1(config)# ntp source loopback0
```

Ý nghĩa:

- Tất cả NTP message gửi đi sẽ sử dụng IP của Loopback0.

Ưu điểm:

- Interface vật lý bị down vẫn có thể hoạt động.
- Địa chỉ loopback luôn ổn định.

Ví dụ:

```
R1 Loopback0
10.1.1.1
      |
      |
     NTP
      |
      |
     R2
```

R2:

```bash
R2(config)# ntp server 10.1.1.1
```

---

# Lưu ý khi dùng Loopback

- Loopback interface khác với loopback address.

## Loopback Interface

Ví dụ:

```
interface loopback0
ip address 10.1.1.1 255.255.255.255
```

Là interface ảo trên router.

---

## Loopback Address

- Là dải địa chỉ:

```
127.0.0.0/8
```

- Dành riêng cho localhost.
- Không dùng để định tuyến giữa các router.

---

# NTP Server Mode

## ntp master

Khi không có NTP server bên ngoài:

- Chọn một router làm NTP server nội bộ.

Cấu hình:

```bash
R1(config)# ntp master
```

Mặc định:

```
Stratum 7
```

Có thể chỉ định:

```bash
R1(config)# ntp master 5
```

Router trở thành:

```
Stratum 5
```

---

## Kiểm tra

```bash
R1# show ntp associations
```

Ví dụ:

```
*~127.127.1.1 .LOCL. 7
```

Ý nghĩa:

- `127.127.1.1`:
    * Địa chỉ NTP internal clock.
- `.LOCL.`:
    * Local clock.
- `7`:
    * Stratum của router.

Các router khác đồng bộ với R1:

```
R1
Stratum 7
 |
 |
R2
Stratum 8
```

---

# NTP Symmetric Active Mode

- Là chế độ hai thiết bị NTP đồng bộ ngang hàng (peer-to-peer).

Khác với:

```
Client ----> Server
```

Peer:

```
R2 <----> R3
```

Cấu hình:

R2:

```bash
R2(config)# ntp peer 10.0.22.3
```

R3:

```bash
R3(config)# ntp peer 10.0.22.2
```

---

# NTP Authentication

- Là tính năng xác thực NTP.
- Không bắt buộc (optional).
- Giúp đảm bảo router chỉ đồng bộ với NTP server tin cậy.

---

# Các lệnh Authentication

## Bật authentication

```bash
ntp authenticate
```

---

## Tạo key

```bash
ntp authentication-key <key-id> md5 <password>
```

Ví dụ:

```bash
ntp authentication-key 1 md5 6604
```

---

## Chọn key tin cậy

```bash
ntp trusted-key <key-id>
```

Ví dụ:

```bash
ntp trusted-key 1
```

---

## Sử dụng key khi kết nối server

```bash
ntp server <ip-address> key <key-id>
```

Ví dụ:

```bash
ntp server 10.0.12.1 key 1
```

---

# Ví dụ NTP Authentication

## R1 - NTP Server

IP:

```
10.0.12.1
```

Cấu hình:

```bash
R1(config)# ntp authenticate

R1(config)# ntp authentication-key 1 md5 6604

R1(config)# ntp trusted-key 1
```

---

## R2 - NTP Client

```bash
R2(config)# ntp authenticate

R2(config)# ntp authentication-key 1 md5 6604

R2(config)# ntp trusted-key 1

R2(config)# ntp server 10.0.12.1 key 1
```

R2:

- Tạo key 1.
- Password là `6604`.
- Tin tưởng key 1.
- Kết nối R1 bằng key 1.

---

# Authentication Key Encryption Type

Cú pháp:

```bash
ntp authentication-key <id> md5 <password> <encryption-type>
```

Ví dụ:

```bash
ntp authentication-key 1 md5 6604 7
```

## Encryption Type

| Type | Ý nghĩa |
|-|-|
| 0 | Plain text |
| 7 | Encrypted |

Ví dụ:

Type 0:

```
ntp authentication-key 1 md5 6604 0
```

- Password lưu dạng plaintext.
- Có thể nhìn thấy trong config.

Type 7:

```
ntp authentication-key 1 md5 7 <encrypted-string>
```

- Password được mã hóa trong running-config.

Lưu ý:

- Tham số encryption type là optional.
- Thực tế thường dùng:
    * `0`
    * `7`
- Không phải mọi giá trị trong khoảng `<0-4294967295>` đều được sử dụng.

---

# Kiểm tra NTP

## Xem trạng thái

```bash
show ntp status
```

## Xem NTP server

```bash
show ntp associations
```

## Xem cấu hình NTP

```bash
show running-config | include ntp
```