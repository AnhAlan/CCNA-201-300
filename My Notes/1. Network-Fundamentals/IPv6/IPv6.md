# IPV6

- IPv4 ra đời vào năm 1981, sử dụng địa chỉ 32 bit.
- IPv5 ra đời khoảng năm 1980 nhưng chỉ là phiên bản thử nghiệm, không được triển khai rộng rãi.
- IPv6 ra đời năm 1998 (RFC 2460), sử dụng địa chỉ 128 bit.

- IPv6 hỗ trợ:
    - QoS (Quality of Service)
    - Multicast
    - Mobility

> IPv6 có nhiều cải tiến so với IPv4, tuy nhiên không đồng nghĩa IPv6 tự động bảo mật hơn IPv4.

---

# Thập lục phân (Hexadecimal)

## Các hệ cơ số

- Binary / Base 2 / ký hiệu `0b`
    - Sử dụng các chữ số:
    ```
    0, 1
    ```

- Decimal / Base 10 / ký hiệu `0d`
    - Sử dụng các chữ số:
    ```
    0 - 9
    ```

- Hexadecimal / Base 16 / ký hiệu `0x`
    - Sử dụng:
    ```
    0 - 9, A - F
    ```

---

## Chuyển Binary sang Hexadecimal

- Mỗi chữ số Hexadecimal tương ứng với 4 bit.

Ví dụ:

```
0b11011011
```

Chia thành:

```
1101 1011
```

Đổi từng nhóm:

```
1101 = D
1011 = B
```

Kết quả:

```
0b11011011 = 0xDB
```

---

# Lý do ra đời IPv6

- IPv4 không đủ địa chỉ cho sự phát triển của Internet hiện nay.
- IPv4 sử dụng 32 bit:

```
2^32 địa chỉ
```

- Mặc dù có các giải pháp như:
    - VLSM
    - CIDR
    - NAT

nhưng đây chỉ là các giải pháp tạm thời.

---

# Quản lý địa chỉ IPv4

IPv4 được quản lý bởi:

```
IANA (Internet Assigned Numbers Authority)
```

IANA phân phối địa chỉ IPv4 cho các tổ chức khu vực:

- ARIN
    - Bắc Mỹ

- APNIC
    - Châu Á - Thái Bình Dương

- RIPE NCC
    - Châu Âu

- LACNIC
    - Mỹ Latinh

- AFRINIC
    - Châu Phi


## IPv4 Exhaustion

- Năm 2011:
    - IANA cạn kiệt kho IPv4.

- Năm 2015:
    - ARIN cạn kiệt IPv4.

---

# Cấu trúc IPv6

- IPv6 sử dụng 128 bit.
- Được biểu diễn dưới dạng số Hexadecimal.
- Gồm 32 ký tự Hexadecimal.
- Chia thành 8 nhóm.
- Mỗi nhóm gồm 4 ký tự Hexadecimal.

Ví dụ:

```
2001:0DB8:001B:20A1:0020:0080:0000:34BD
```

Cấu trúc:

```
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
```

---

# IPv6 Prefix Length

IPv6 thường sử dụng:

```
/64
```

Ý nghĩa:

- 64 bit đầu:
    - Network Prefix

- 64 bit sau:
    - Interface ID

Ví dụ:

```
2001:DB8:1234:5678::/64
```

---

# Các phương pháp rút gọn IPv6

## 1. Loại bỏ các số 0 đứng đầu trong mỗi nhóm

Ví dụ:

Ban đầu:

```
2001:0DB8:001B:20A1:0020:0080:34BD
```

Sau khi rút gọn:

```
2001:DB8:1B:20A1:20:80:34BD
```

---

## 2. Thay các nhóm 0 liên tiếp bằng dấu `::`

Ví dụ:

Ban đầu:

```
2001:0DB8:0000:0000:0000:0000:0080:34BD
```

Loại bỏ số 0 đầu:

```
2001:DB8:0:0:0:0:80:34BD
```

Thay nhóm 0 liên tiếp:

```
2001:DB8::80:34BD
```

---

## Lưu ý khi sử dụng `::`

- Chỉ được sử dụng `::` một lần trong một địa chỉ IPv6.
- Vì `::` đại diện cho một hoặc nhiều nhóm `0000`.

Ví dụ:

```
2001:0000:0000:0000:20A1:0000:0000:34DB
```

Không được viết:

```
2001::20A1::34DB
```

Vì không xác định được:

- Có bao nhiêu nhóm 0 ở bên trái.
- Có bao nhiêu nhóm 0 ở bên phải.

Cách viết đúng:

```
2001::20A1:0:0:34DB
```

# IPv6

## 1. Chia subnet IPv6 từ prefix ISP cấp

- Khi doanh nghiệp yêu cầu sử dụng IPv6 nhưng ISP chỉ cung cấp prefix:

```
/48
```

- Trong mạng LAN IPv6 thường sử dụng:

```
/64
```

- Ta có:

```
64 - 48 = 16 bit
```

=> Doanh nghiệp có thể sử dụng 16 bit để tạo subnet.

Cấu trúc:

```
| 48 bit ISP | 16 bit Subnet | 64 bit Host |
```

Ví dụ:

```
2001:00B8:8B00:0001:0000:0000:0000:00BD
```

Phân chia:

```
2001:00B8:8B00
```

- 48 bit được ISP cấp.


```
0001
```

- 16 bit subnet.


```
0000:0000:0000:00BD
```

- 64 bit dành cho Interface ID (Host).

---

## 2. Tìm prefix của IPv6

### Trường hợp prefix length là bội số của 4

- Mỗi ký tự Hexadecimal tương ứng:

```
4 bit
```

- Mỗi nhóm IPv6:

```
16 bit = 4 ký tự Hex
```

- Ta đếm từ trái sang phải đến khi đủ prefix length.

---

Ví dụ:

```
300D:00F2:00E2:00A2:00B2:00C2:00D2:00E2 /56
```

Ta có:

```
56 bit / 4 = 14 ký tự Hex
```

14 ký tự tương ứng:

```
300D:00F2:00E2:00
```

Vậy prefix:

```
300D:00F2:00E2:00A2::/56
```

Lưu ý:

- Không bỏ ký tự `A2`.
- Vì nó không phải là các số 0 đứng đầu.

---

## 3. Trường hợp prefix length không phải bội số của 4

- Khi prefix length không chia hết cho 4.
- Prefix sẽ kết thúc giữa một ký tự Hex.
- Cần chuyển ký tự đó sang Binary để xác định bit.

Ví dụ:

```
2001:0DB8:8B00:0001:FB89:017B:0020:0011 /93
```

Ta biết:

```
1 ký tự Hex = 4 bit
```

92 bit tương ứng:

```
23 ký tự Hex
```

Ký tự thứ 24 sẽ chứa bit thứ 93.

Địa chỉ:

```
2001:0DB8:8B00:0001:FB89:017B:0020:0011
```

Đếm:

```
2001:0DB8:8B00:0001:FB89:017B
```

là 24 ký tự Hex.

Ta xét ký tự cuối của nhóm:

```
017B
```

Ký tự:

```
B
```

Chuyển sang Binary:

```
B = 1011
```

Vì prefix là /93:

- Bit đầu tiên của B thuộc prefix.
- Các bit còn lại thuộc host.

Giữ bit đầu:

```
1011
```

Lấy bit đầu:

```
1
```

Các bit host đặt về 0:

```
1000
```

Đổi lại Hex:

```
1000 = 8
```

Vậy:

```
2001:0DB8:8B00:0001:FB89:0178::/93
```

---

## 4. Tạo subnet IPv6

Ví dụ:

```
2001:00B8:8B00:0001:0000:0000:0000:00BD /64
```

64 bit đầu là network prefix:

```
2001:00B8:8B00:0001
```

64 bit sau dành cho host.

Subnet có thể tạo:

Subnet 1:

```
2001:00B8:8B00:0001::/64
```

Subnet 2:

```
2001:00B8:8B00:0002::/64
```

Vì:

- 16 bit subnet nằm giữa prefix ISP và host.
- 64 bit cuối dành cho host.

---

## 5. Cấu hình IPv6 trên Router Cisco

### Bật định tuyến IPv6

Mặc định router Cisco tắt IPv6 routing.

Lệnh:

```
R1(config)# ipv6 unicast-routing
```

Chức năng:

- Cho phép router định tuyến các gói tin IPv6.
- Tương tự như bật IPv4 routing.


## Cấu hình IPv6 cho interface

Ví dụ:

```
R1(config)# interface g0/0
R1(config-if)# ipv6 address 2001:DB8::1/64
R1(config-if)# no shutdown
```

Tương tự IPv4:

- Gán địa chỉ IP.
- Bật interface bằng `no shutdown`.
