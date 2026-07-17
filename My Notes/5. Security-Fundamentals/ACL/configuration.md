# Các lệnh ACL (Standard & Extended)

> **Lưu ý**
>
> - Standard ACL: chỉ lọc theo **Source IP**.
> - Extended ACL: lọc theo **Protocol + Source IP + Destination IP + Port + ...**
> - ACL xử lý **từ trên xuống dưới**, dòng đầu tiên match sẽ được áp dụng.
> - Cuối mọi ACL đều có **implicit deny**:
>
> ```cisco
> deny ip any any
> ```

---

# 1. Tạo ACL Numbered

## Standard

```cisco
access-list <1-99 | 1300-1999> {permit | deny} <source> <wildcard>
```

Ví dụ

```cisco
access-list 1 deny host 1.1.1.1
access-list 1 permit any
```

> **Note**
>
> - Chỉ match Source IP.
> - Không thể chỉnh sửa từng dòng, muốn sửa thường phải xóa rồi tạo lại.

---

## Extended

```cisco
access-list <100-199 | 2000-2699> {permit | deny} protocol source destination [options]
```

Ví dụ

```cisco
access-list 100 deny tcp any host 10.1.1.1 eq 80
access-list 100 permit ip any any
```

> **Note**
>
> - Match theo Protocol, IP, Port,...
> - Thích hợp khi cần lọc lưu lượng chi tiết.

---

# 2. Tạo ACL Named

## Standard

```cisco
ip access-list standard <name>
```

Ví dụ

```cisco
ip access-list standard OFFICE
```

---

## Extended

```cisco
ip access-list extended <name>
```

Ví dụ

```cisco
ip access-list extended WEB-FILTER
```

> **Note**
>
> - Nên dùng Named ACL vì dễ chỉnh sửa, thêm, xóa từng dòng.

---

# 3. Thêm Rule vào Named ACL

Standard

```cisco
[sequence] permit source wildcard
[sequence] deny source wildcard
```

Extended

```cisco
[sequence] permit protocol source destination [options]
[sequence] deny protocol source destination [options]
```

Ví dụ

```cisco
10 deny tcp any host 10.1.1.1 eq 80
20 deny icmp any any
30 permit ip any any
```

> **Note**
>
> - Sequence Number giúp chèn hoặc xóa từng dòng dễ dàng.
> - Nếu không nhập, Cisco sẽ tự đánh số.

---

# 4. Thêm Remark

Numbered

```cisco
access-list 100 remark Block HTTP
```

Named

```cisco
remark Block HTTP
```

> **Note**
>
> - Chỉ dùng để ghi chú.
> - Không ảnh hưởng đến hoạt động ACL.

---

# 5. Áp dụng ACL vào Interface

Inbound

```cisco
interface g0/0
ip access-group <ACL> in
```

Outbound

```cisco
interface g0/0
ip access-group <ACL> out
```

Ví dụ

```cisco
ip access-group 100 in
```

```cisco
ip access-group WEB-FILTER out
```

> **Note**
>
> - **in**: kiểm tra khi gói vừa đi vào Router.
> - **out**: kiểm tra trước khi gói rời Router.
> - Extended ACL thường đặt gần **Source**.
> - Standard ACL thường đặt gần **Destination**.

---

# 6. Gỡ ACL khỏi Interface

```cisco
no ip access-group <ACL> in
```

```cisco
no ip access-group <ACL> out
```

> **Note**
>
> - Chỉ bỏ việc áp dụng ACL.
> - ACL vẫn còn tồn tại trong cấu hình.

---

# 7. Xóa ACL

## Numbered

```cisco
no access-list <number>
```

Ví dụ

```cisco
no access-list 100
```

---

## Named

```cisco
no ip access-list standard <name>
```

```cisco
no ip access-list extended <name>
```

Ví dụ

```cisco
no ip access-list extended WEB-FILTER
```

> **Note**
>
> - Xóa toàn bộ ACL.

---

# 8. Chỉnh sửa ACL Named

```cisco
ip access-list extended WEB-FILTER
```

Ví dụ

```cisco
10 deny tcp any host 10.1.1.1 eq 80
20 permit ip any any
```

> **Note**
>
> - Numbered ACL không thuận tiện để chỉnh sửa.
> - Named ACL được khuyến khích sử dụng.

---

# 9. Sequence Number

Ví dụ

```cisco
10 permit tcp any any
20 deny icmp any any
30 permit ip any any
```

> **Note**
>
> - Quyết định thứ tự xử lý ACL.
> - ACL luôn kiểm tra từ số nhỏ đến lớn.

---

# 10. Chèn Rule vào giữa

```cisco
15 deny udp any any
```

Ví dụ

```text
10 permit tcp any any
15 deny udp any any
20 deny icmp any any
30 permit ip any any
```

> **Note**
>
> - Chỉ cần chọn số nằm giữa hai dòng hiện có.

---

# 11. Xóa một Rule

```cisco
no 20
```

> **Note**
>
> - Chỉ xóa dòng có Sequence Number tương ứng.
> - Chỉ áp dụng cho Named ACL.

---

# 12. Resequence ACL

```cisco
ip access-list resequence <ACL> <start> <increment>
```

Ví dụ

```cisco
ip access-list resequence WEB-FILTER 10 10
```

> **Note**
>
> - Đánh số lại toàn bộ ACL.
> - Không làm thay đổi nội dung ACL.

---

# 13. Hiển thị ACL

Hiển thị tất cả

```cisco
show access-lists
```

hoặc

```cisco
show ip access-lists
```

Hiển thị ACL cụ thể

```cisco
show access-lists 100
```

```cisco
show access-lists WEB-FILTER
```

> **Note**
>
> - Hiển thị các rule.
> - Hiển thị số lần match của từng rule.

---

# 14. Kiểm tra ACL trên Interface

```cisco
show ip interface
```

hoặc

```cisco
show ip interface g0/0
```

Ngoài ra

```cisco
show running-config interface g0/0
```

> **Note**
>
> - Kiểm tra ACL nào đang được áp dụng.
> - Kiểm tra hướng **in** hay **out**.

---

# 15. Xem Running Configuration

```cisco
show running-config
```

hoặc

```cisco
show running-config interface g0/0
```

> **Note**
>
> - Kiểm tra toàn bộ cấu hình ACL và Interface.

---

# 16. Xóa Counter Match

Toàn bộ ACL

```cisco
clear access-list counters
```

ACL cụ thể

```cisco
clear access-list counters 100
```

> **Note**
>
> - Chỉ xóa bộ đếm (match counter).
> - Không xóa ACL.

---

# 17. Quy trình cấu hình ACL

### Bước 1

Tạo ACL

```cisco
ip access-list extended WEB-FILTER
```

---

### Bước 2

Thêm Rule

```cisco
deny tcp any host 10.1.1.10 eq 80
deny tcp any host 10.1.1.10 eq 443
permit ip any any
```

---

### Bước 3

Áp dụng ACL

```cisco
interface g0/0
ip access-group WEB-FILTER in
```

---

### Bước 4

Kiểm tra

```cisco
show access-lists
show ip interface g0/0
```

---

# Ghi nhớ nhanh

- Standard ACL → gần **Destination**.
- Extended ACL → gần **Source**.
- Mỗi Interface chỉ áp dụng:
    - 1 ACL **Inbound**
    - 1 ACL **Outbound**
    - cho mỗi giao thức (IPv4, IPv6).
- Rule đầu tiên match sẽ được áp dụng.
- Cuối ACL luôn có:

```cisco
deny ip any any
```

- Named ACL được khuyến khích sử dụng hơn Numbered ACL vì dễ quản lý và chỉnh sửa.