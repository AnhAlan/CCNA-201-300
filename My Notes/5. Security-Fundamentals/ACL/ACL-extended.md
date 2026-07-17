# Extended ACLs
- có chức năng tương tự Standard ACL nhưng **chi tiết hơn**
- có thể lọc dựa trên:
    * Protocol
    * Source IP
    * Destination IP
    * Source Port
    * Destination Port
    * và nhiều trường khác (TCP flags, DSCP, TTL,...)
- có thể đặt tên hoặc số
- Numbered ACL sử dụng các dải:
    * 100 - 199
    * 2000 - 2699
- ACL Extended vẫn tuân thủ nguyên tắc xử lý từ trên xuống dưới
    * mục đầu tiên match sẽ được áp dụng
    * các mục phía dưới sẽ không được kiểm tra nữa
- cuối ACL luôn tồn tại **implicit deny**
    * `deny ip any any`
- có 2 loại:
    * Extended Numbered ACL
    * Extended Named ACL

---

# Cấu hình Extended ACL

- Numbered ACL

```bash
R1(config)# access-list <number> {permit | deny} protocol source wildcard destination wildcard [options]
```

Ví dụ

```bash
R1(config)# access-list 100 permit tcp any host 1.1.1.1 eq 80
```

- Named ACL

```bash
R1(config)# ip access-list extended <name>
```

```bash
R1(config-ext-nacl)# [sequence-number] {permit | deny} protocol source destination [options]
```

---

# Matching the Protocol

- Extended ACL có thể lọc theo giao thức (Protocol)

```bash
R1(config)# ip access-list extended ICPC
```

```bash
R1(config-ext-nacl)# deny ?
```

Các lựa chọn gồm

- protocol number (0-255)
- tên giao thức
    * ip
    * tcp
    * udp
    * icmp
    * ospf
    * eigrp
    * gre
    * ...

Có thể nhập bằng:

- protocol number
- tên protocol

Ví dụ

```bash
deny icmp
deny tcp
deny ospf
deny 6
```

---

## Protocol = ip

Nếu chọn protocol là `ip`

```bash
deny ip any any
```

thì ACL sẽ match **mọi gói IPv4**

bao gồm

- TCP
- UDP
- ICMP
- OSPF
- GRE
- ...

---

## TCP

```bash
deny tcp ?
```

Sau protocol sẽ nhập

- Source IP

Các lựa chọn

- A.B.C.D
- any
- host
- object-group

Ví dụ

```bash
deny tcp any ?
```

Sau Source sẽ nhập

- Destination IP

Ví dụ

```bash
deny tcp any any
```

hoặc

```bash
deny tcp any host 10.1.1.1
```

Lưu ý

```bash
deny tcp any
```

không phải câu lệnh hợp lệ vì Cisco yêu cầu phải khai báo đầy đủ Destination.

---

# Ví dụ Protocol

Cho phép toàn bộ IPv4

```bash
permit ip any any
```

Chặn mạng `10.0.0.0/24` gửi UDP đến host `192.168.1.1`

```bash
deny udp 10.0.0.0 0.0.0.255 host 192.168.1.1
```

Chặn host `172.16.1.1` ping mạng `192.168.0.0/24`

```bash
deny icmp host 172.16.1.1 192.168.0.0 0.0.0.255
```

---

# Matching TCP/UDP Port Number

Với TCP và UDP có thể lọc thêm theo Port.

Cú pháp

```bash
permit|deny
protocol
source-address
[source-port]
destination-address
[destination-port]
```

Có thể dùng

- eq (=)
- gt (>)
- lt (<)
- neq (!=)
- range (l r)

Ví dụ

```bash
deny tcp any host 1.1.1.1 eq 80
```

Nghĩa là

- deny mọi TCP đến host 1.1.1.1
- destination port = 80

---

## Port có thể nhập

- số

```bash
eq 443
```

- tên dịch vụ

```bash
eq www
eq https
eq ftp
eq ssh
eq telnet
```

---

# Ví dụ

Cho phép mạng `10.0.0.0/24` truy cập HTTPS đến host `2.2.2.2`

```bash
permit tcp 10.0.0.0 0.0.0.255 host 2.2.2.2 eq 443
```

Chặn UDP đến host `3.3.3.3` trên dải port 20000-30000

```bash
deny udp any host 3.3.3.3 range 20000 30000
```

Cho phép TCP

- source network `172.16.1.0/24`
- source port > 9999
- destination host `4.4.4.4`
- destination port khác 23

```bash
permit tcp 172.16.1.0 0.0.0.255 gt 9999 host 4.4.4.4 neq 23
```

---

# Quy tắc nhớ

Thứ tự chuẩn

```text
permit|deny
+
protocol
+
source address
+
source port (optional)
+
destination address
+
destination port (optional)
+
other options (optional)
```

Nếu chỉ có một host

```bash
host <ip>
```

Nếu là mọi địa chỉ

```bash
any
```

---

# Vị trí đặt ACL

Do Extended ACL xác định rất chi tiết loại lưu lượng nên thường đặt **gần Source**.

Lợi ích

- loại bỏ sớm các gói tin bị deny
- giảm lưu lượng không cần thiết trên mạng

Ngược lại

- Standard ACL thường đặt gần Destination.

---

# Một số option nâng cao (CCNA chỉ nên biết)

Sau Destination IP và Destination Port có thể thêm các điều kiện khác.

- ack
    * Match TCP ACK flag

- fin
    * Match TCP FIN flag

- syn
    * Match TCP SYN flag

- established
    * Match các TCP session đã được thiết lập (ACK hoặc RST)

- ttl
    * Match theo TTL của IPv4 packet

- dscp
    * Match theo giá trị DSCP (Differentiated Services Code Point)
    * Dùng để phân loại mức ưu tiên của gói tin khi triển khai QoS.