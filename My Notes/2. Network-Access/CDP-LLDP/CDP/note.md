# CDP - Cisco Discovery Protocol

- Là giao thức **proprietary** của Cisco.
- Hoạt động ở **Layer 2 (Data Link)**.
- Mặc định được **enable** trên hầu hết các interface.
- Gửi các gói tin đến địa chỉ **multicast MAC**: `0100.0CCC.CCCC`.
- Chỉ các **neighbor kết nối trực tiếp** mới nhận và xử lý gói CDP.
- Router/Switch **không forward** các gói CDP, nên các neighbor không kết nối trực tiếp sẽ không nhận được.
- Mặc định gửi **CDP Advertisement** mỗi **60 giây**.
- Khi nhận được CDP Advertisement, thiết bị sẽ lưu thông tin neighbor vào **CDP Neighbor Table**.
- Nếu neighbor mất kết nối, thông tin vẫn được giữ trong bảng với **Holdtime mặc định là 180 giây**.
- Sau 180 giây nếu không nhận được CDP Advertisement mới, neighbor sẽ bị xóa khỏi bảng.
- **CDPv2** được sử dụng mặc định (CDPv1 là phiên bản cũ).

---

# Kiểm tra CDP

- `show cdp`
- `show cdp traffic`
- `show cdp interface`
- `show cdp neighbors`
- `show cdp neighbors detail`

`show cdp neighbors detail` hiển thị thêm nhiều thông tin của neighbor như:

- IOS Version
- Platform
- Management IP
- VTP Domain
- Native VLAN
- Duplex
- Capabilities
- ...

> CDP thường hiển thị nhiều thông tin chi tiết hơn LLDP.

---

# Cấu hình CDP

## Xem thông tin một neighbor

```cisco
show cdp entry <hostname>
```

Ví dụ:

```cisco
show cdp entry R2
```

## Tắt CDP toàn bộ thiết bị

```cisco
R1(config)# no cdp run
```

## Tắt CDP trên một interface

```cisco
R1(config)# interface g0/0
R1(config-if)# no cdp enable
```

## Thay đổi chu kỳ gửi CDP Advertisement

```cisco
R1(config)# cdp timer <seconds>
```

Ví dụ:

```cisco
R1(config)# cdp timer 30
```

- Cấu hình khoảng thời gian giữa các lần thiết bị gửi CDP Advertisement đến neighbor.
- Mặc định: 60 giây.
- Timer càng nhỏ → neighbor được cập nhật nhanh hơn nhưng tạo thêm lưu lượng CDP.
- Timer chỉ ảnh hưởng đến tần suất gửi CDP, không ảnh hưởng đến thời gian xóa neighbor.

## Thay đổi Holdtime

```cisco
R1(config)# cdp holdtime <seconds>
```

Ví dụ:

```cisco
R1(config)# cdp holdtime 120
```

- Cấu hình thời gian một neighbor được giữ trong CDP Neighbor Table nếu không nhận được CDP Advertisement mới.
- Mặc định: 180 giây.
- Khi hết thời gian Holdtime mà không có CDP Advertisement mới → neighbor bị xóa khỏi bảng.
- Holdtime thường lớn hơn CDP timer để tránh xóa nhầm neighbor khi một vài gói CDP bị mất.

## Tắt CDPv2

```cisco
R1(config)# no cdp advertise-v2
```