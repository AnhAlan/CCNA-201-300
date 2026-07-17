# LLDP - Link Layer Discovery Protocol

- Là giao thức chuẩn mở của **IEEE 802.1AB**.
- Hoạt động ở **Layer 2 (Data Link)**.
- Mặc định **disable trên Cisco**.
- Một thiết bị có thể chạy **CDP và LLDP cùng lúc**.
- LLDP gửi các gói tin đến địa chỉ **multicast MAC**:

```
01:80:C2:00:00:0E
```

- Cách xử lý của thiết bị tương tự CDP:
    - Chỉ neighbor kết nối trực tiếp nhận được.
    - Switch không forward frame LLDP.
    - Neighbor nhận được sẽ lưu thông tin vào LLDP Neighbor Table.

- LLDP gửi **Advertisement message mỗi 30 giây**.
- Holdtime mặc định: **120 giây**.
- LLDP có thêm **reinitialization delay (reinit delay)**:
    - Là khoảng thời gian trì hoãn trước khi khởi tạo lại LLDP.
    - Giúp link ổn định trước khi gửi advertisement.
    - Nội dung này thường vượt mức CCNA.

---

# Cấu hình LLDP

## Bật LLDP toàn bộ thiết bị

```cisco
R1(config)# lldp run
```

## Tắt LLDP toàn bộ thiết bị

```cisco
R1(config)# no lldp run
```

---

# Bật LLDP trên interface

## Chỉ gửi LLDP (Transmit)

```cisco
R1(config)# interface g0/0
R1(config-if)# lldp transmit
```

- Interface chỉ gửi LLDP Advertisement.
- Không nhận LLDP từ neighbor.
- Nếu nhận frame LLDP sẽ bỏ qua.

---

## Chỉ nhận LLDP (Receive)

```cisco
R1(config)# interface g0/0
R1(config-if)# lldp receive
```

- Interface chỉ nhận LLDP Advertisement.
- Không gửi LLDP.

---

# Cấu hình Timer

## Thay đổi chu kỳ gửi LLDP

```cisco
R1(config)# lldp timer <seconds>
```

Ví dụ:

```cisco
R1(config)# lldp timer 60
```

---

## Thay đổi Holdtime

```cisco
R1(config)# lldp holdtime <seconds>
```

Ví dụ:

```cisco
R1(config)# lldp holdtime 180
```
- Thời gian neighbor được giữ trong bảng LLDP nếu không nhận được Advertisement mới.
- Hết thời gian này → xóa neighbor.
- Mặc định: 120 giây.

---

## Cấu hình Reinitialization Delay

```cisco
R1(config)# lldp reinit <seconds>
```

Ví dụ:

```cisco
R1(config)# lldp reinit 5
```

- Khoảng thời gian chờ trước khi LLDP khởi tạo lại sau khi thay đổi trạng thái interface.
- Giúp tránh gửi LLDP khi link chưa ổn định.
---

# Kiểm tra LLDP

```cisco
show lldp
```

Thông tin tổng quan.

```cisco
show lldp traffic
```

Thống kê LLDP gửi/nhận.

```cisco
show lldp interface
```

Thông tin LLDP trên interface.

```cisco
show lldp neighbors
```

Danh sách neighbor.

```cisco
show lldp neighbors detail
```

Thông tin chi tiết neighbor:

- Hostname
- Management IP
- Port ID
- Platform
- Capabilities
- ...

---

# Lưu ý

- LLDP không hiển thị được một số thông tin độc quyền của Cisco như:
    - VTP Domain
    - Một số thông tin Cisco proprietary

Lý do:

- VTP là giao thức độc quyền của Cisco.
- LLDP là chuẩn IEEE nên không quảng bá các thông tin riêng của Cisco.