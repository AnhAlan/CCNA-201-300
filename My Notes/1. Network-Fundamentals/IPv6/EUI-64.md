# 1. Configuration IPv6 Address (EUI-64)

## EUI-64 là gì?

- EUI (Extended Unique Identifier):
    - Mã định danh duy nhất mở rộng.

- EUI-64 là phương pháp chuyển đổi địa chỉ MAC 48 bit thành Interface ID 64 bit.

- Interface ID này có thể được sử dụng làm phần Host của địa chỉ IPv6 `/64`.

- EUI-64 **không phải là một loại địa chỉ IPv6**.
    - Đây chỉ là phương pháp tạo Interface ID IPv6 từ địa chỉ MAC.

---

# Cách chuyển đổi địa chỉ MAC sang EUI-64

## Bước 1: Chia địa chỉ MAC thành hai phần

MAC có 48 bit:

Ví dụ:

```
12:34:56:78:90:AB
```

Chia thành:

```
12:34:56 | 78:90:AB
```

---

## Bước 2: Chèn FFFE vào giữa

Thêm:

```
FFFE
```

vào giữa hai phần MAC.

Kết quả:

```
12:34:56:FF:FE:78:90:AB
```

Hoặc viết dạng nhóm IPv6:

```
1234:56FF:FE78:90AB
```

### FFFE là gì?

- FFFE không phải là từ viết tắt.
- Đây là giá trị Hexadecimal cố định được thêm vào khi tạo EUI-64.
- Mục đích:
    - Mở rộng MAC 48 bit thành Interface ID 64 bit.

---

# Bước 3: Đảo ngược U/L bit (bit thứ 7)

- Trong byte đầu tiên của MAC có một bit đặc biệt gọi là:

```
U/L bit (Universal/Local bit)
```

- Bit này quyết định MAC là:

```
0 -> UAA (Universally Administered Address)

1 -> LAA (Locally Administered Address)
```

---

Ví dụ:

MAC:

```
12:34:56:78:90:AB
```

Byte đầu tiên:

```
12
```

Chuyển sang Binary:

```
12 = 00010010
```

U/L bit là bit thứ 7 tính từ trái sang:

```
00010010
      ^
      U/L bit
```

Bit này đang là:

```
1
```

Đảo bit:

```
1 -> 0
```

Byte mới:

```
00010000
```

Đổi lại Hex:

```
10
```

---

Sau khi đảo bit:

MAC mới:

```
10:34:56:78:90:AB
```

Chèn FFFE:

```
10:34:56:FF:FE:78:90:AB
```

EUI-64:

```
1034:56FF:FE78:90AB
```

---

# Cấu hình IPv6 sử dụng EUI-64 trên Cisco Router

Vào interface:

```
R1(config)# interface g0/0
```

Cấu hình IPv6:

```
R1(config-if)# ipv6 address 2001:db8::/64 eui-64
```

Bật interface:

```
R1(config-if)# no shutdown
```

Router sẽ tự động tạo phần Interface ID dựa trên MAC.

---

# Tại sao phải đảo U/L bit?

## Địa chỉ MAC gồm hai loại

### UAA (Universally Administered Address)

- MAC được gán bởi nhà sản xuất.
- Có tính duy nhất trên toàn cầu.

Ví dụ:

```
MAC của card mạng
```

---

### LAA (Locally Administered Address)

- MAC được quản trị viên cấu hình thủ công.
- Không đảm bảo duy nhất toàn cầu.

---

# Xác định UAA hay LAA

Dựa vào U/L bit:

```
U/L bit = 0
```

=> UAA

```
U/L bit = 1
```

=> LAA

---

# Ý nghĩa đảo U/L bit trong EUI-64

Khi tạo IPv6 Interface ID:

- EUI-64 đảo ngược U/L bit.

Mục đích:

- Nếu MAC ban đầu là UAA:

```
U/L = 0
```

Sau khi đảo:

```
U/L = 1
```

- Nếu MAC ban đầu là LAA:

```
U/L = 1
```

Sau khi đảo:

```
U/L = 0
```

---

# Ví dụ hoàn chỉnh

MAC:

```
00:25:96:12:34:56
```

Chia:

```
00:25:96 | 12:34:56
```

Chèn FFFE:

```
00:25:96:FF:FE:12:34:56
```

Đảo U/L bit:

Byte đầu:

```
00 = 00000000
```

U/L bit:

```
0 -> 1
```

Byte mới:

```
02
```

EUI-64:

```
0225:96FF:FE12:3456
```

IPv6 hoàn chỉnh:

```
2001:DB8::0225:96FF:FE12:3456/64
```

---

# CCNA cần nhớ
- với IPv6 có sẵn 201:8:9:10:: / 64
- nếu ta sử dụng EUI-64 sẽ tạo IPv6 giao diện từ UPv6 trên -> tức tạo interface Host cho end-host 
- EUI-64 tạo Interface ID 64 bit từ MAC 48 bit - tạo 64 bit cuối - tức phần HOST
- Chèn `FFFE` vào giữa MAC.
- Đảo U/L bit trong byte đầu tiên.
- EUI-64 chỉ tạo Interface ID, không phải loại IPv6.
- IPv6 `/64` thường dùng:
    - 64 bit Network Prefix.
    - 64 bit Interface ID.


