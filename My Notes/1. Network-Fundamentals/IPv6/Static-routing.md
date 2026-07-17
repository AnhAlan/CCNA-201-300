# Static routing 
- đối với IPv4 thì mặc định đã được bật
- IPv6 mặc định định tuyến là tắt nên phải cấu hình bật
    * R1(config)# ipv6 unicast-routing
- nếu không bật định tuyến ipv6 thì các gói tin ipv6 vẫn gửi và nhận tuy nhiên sẽ không được định tuyến

- Một tuyến đường (conected network - C) kết nối mạng sẽ tự động được thêm vào cho mỗi mạng được kết nối.

- Một tuyến đường máy chủ cục bộ (Local host - L) được tự động thêm cho mỗi địa chỉ được cấu hình trên bộ định tuyến.
- các tuyến đường cho link-local address không được thêm vào bảng định tuyến
- C 2001:DB8:0:1::/64 [0/0]
    * via gigabitethernet0/1, directly connected

- L 2001:DB8:0:1::1/128 [0/0]
    * via gigabitethernet0/1, recive

- L FF00::/8 [0/0]
    * via null0, recive 
    * tức các lưu lượng không match ở trên sẽ bị loại bỏ


# ipv6 static command
- lưu ý đây là lệnh routting tĩnh
- ipv6 route "DST / Prefix-length {next-hop | exit-interface [next-hop]}" [ad]

## Directly attacked - ip + interface
- chỉ định đầu ra là giao diện
- tuy nhiên chỉ hoạt động trên giao diện Serial
- R1(config)# ipv6 route 2001:db8:0:3::/64 se0/0
- tức các gói tin gửi đến 2001:db8:0:3::/64 phải đi qua se0/0 của R1

## recursive - nexthop - ip + nexthop
- xác định 'next-hop' là đầu ra
- R1(config)# ipv6 route 2001:db8:0:3::/64 2001:db8:0:12::2
- tức các gói tin đi qua 2001:db8:0:0::/64 phải đi qua giap diện có ip 2001:db8:0:12::/64
    * giao diện 2001:db8:0:12::2 là giao diện R1 nối - tức R2 hay R khác

## full specified - sử dụng cả hai là interface và nexthop
- kết hợp cả 2
    * R1(config)# ipv6 route 2001:db8:0:3::/64 g0/0 2001:db8:0:12::2
- các gói tin đến 2001:db8:0:12::/64 phải đi qua giao diện g0/0 có ip 2001:db8:0:3::/64
    * R2 g0/0 nối R1
    * tức chuyển gói tin đến R2

## network route - chuyển gói tin đến mạng (chưa cụ thể)
- R1(config)# ipv6 route 2001:db8:0:3::/64 2001:db8:0:12::2
    * tức gửi tin đến mạng 2001:db8:0:3::/64

## host route - chuyển gói tin đến mạng cụ thể /128
- R1(config) ipv6 route 2001:db8:0:3::100/128 2001:db8:0:12::2
    * gửi gói tin đến duy nhất 2001:db8:0:3::100 thông qua 2001:db8:0:12::2
## default route
- các tuyến đường không có trong bảng định tuyến sẽ gửi đến giao diện này
    * R1(config)# ipv6 route ::/0 2001:db8:0:23::1

## Sử dụng Link-local làm Next-hop
- IPv6 static route có thể sử dụng **địa chỉ Link-local** của router kế tiếp làm next-hop.
- Vì địa chỉ Link-local (`FE80::/10`) chỉ có phạm vi trong cùng một mạng local link, router cần biết **interface nào để gửi gói tin**.
- Do đó khi sử dụng Link-local làm next-hop phải khai báo thêm **exit-interface**.
- Ví dụ:
    * R1(config)# ipv6 route 2001:DB8:2::/64 GigabitEthernet0/0 FE80::2

 
# Backup Route (Floating Static Route)

## 1. Khái niệm

- **Backup route** là tuyến đường dự phòng, được sử dụng khi tuyến đường chính (**primary route**) bị lỗi.

- Thường sử dụng:
    * Dynamic routing protocol làm đường chính.
    * Static route làm đường dự phòng.

- Để static route chỉ hoạt động khi route chính mất, cần tăng **Administrative Distance (AD)**.

---

## 2. Administrative Distance (AD)

- AD dùng để quyết định độ ưu tiên giữa các route.

- Router sẽ chọn route có **AD nhỏ hơn**.

| Route | AD mặc định |
|---|---:|
| Connected | 0 |
| Static | 1 |
| EIGRP | 90 |
| OSPF | 110 |
| RIP | 120 |

---

## 3. Floating Static Route

- Là static route có AD **cao hơn route chính**.

- Static route mặc định:

```
AD = 1
```

- Vì AD nhỏ nên nó sẽ được ưu tiên hơn OSPF, EIGRP,...

Ví dụ:

```
Static Route = 1
OSPF         = 110
```

Router chọn:

```
Static Route
```

---

## 4. Cấu hình Static Route có AD

Cú pháp:

```
ipv6 route destination prefix-length next-hop [AD]
```

Ví dụ:

```
R1(config)# ipv6 route 2001:DB8:2::/64 2001:DB8:10::2 200
```

Trong đó:

```
200 = Administrative Distance
```

---

## 5. Ví dụ Backup cho OSPF

## Route chính

OSPF học được:

```
O 2001:DB8:2::/64 [110/20]
```

AD:

```
110
```

---

## Tạo static route dự phòng

```
ipv6 route 2001:DB8:2::/64 2001:DB8:10::2 200
```

Routing table:

```
O 2001:DB8:2::/64 [110/20]

S 2001:DB8:2::/64 [200/0]
```

Router chọn OSPF vì:

```
110 < 200
```

Static route nằm chờ làm backup.

---

## 6. Khi OSPF bị lỗi

OSPF route bị xóa:

```
O 2001:DB8:2::/64
```

Router sử dụng:

```
S 2001:DB8:2::/64 [200/0]
```

Static route trở thành đường chính tạm thời.

---

## 7. Lưu ý

- Backup route phải có AD **lớn hơn route chính**.

Ví dụ:

```
OSPF       AD 110 → Primary

Static     AD 200 → Backup
```

- Quy tắc:

```
AD nhỏ hơn  → ưu tiên
AD lớn hơn  → backup
```

- Floating Static Route thường dùng để backup cho:
    * OSPF
    * EIGRP
    * RIP

# Quan trọng

- IPv6 **không cần NAT** như IPv4 vì có không gian địa chỉ rất lớn.
    * Mỗi thiết bị có thể sử dụng địa chỉ Global Unicast riêng.
    * Tuy nhiên vẫn cần Firewall để bảo vệ mạng.

- IPv6 vẫn cần **Firewall**.
    * Không sử dụng NAT không có nghĩa là mạng IPv6 tự động an toàn.
    * Firewall dùng để kiểm soát lưu lượng vào/ra và bảo vệ thiết bị trong mạng.

- **Link-local address (`FE80::/10`) luôn tồn tại trên các interface IPv6.**
    * Được sử dụng cho giao tiếp nội bộ trên cùng một link.
    * Dùng trong các giao thức như NDP, OSPFv3 và giao tiếp giữa các router láng giềng.
    * Không được định tuyến ra ngoài mạng.

- IPv6 LAN thường sử dụng prefix mặc định: /64
    * 64 bit đầu dành cho Network Prefix.
    * 64 bit sau dành cho Interface ID (địa chỉ thiết bị).
- Prefix `/64` là chuẩn phổ biến cho mạng LAN IPv6 vì hỗ trợ SLAAC và EUI-64.



