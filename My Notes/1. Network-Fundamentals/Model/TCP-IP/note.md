# TCP - UDP

- Layer 4: Chịu trách nhiệm truyền dữ liệu từ process (ứng dụng) của thiết bị nguồn đến process của thiết bị đích
- Cung cấp các dịch vụ truyền dữ liệu:
    * Truyền dữ liệu tin cậy (reliable delivery - TCP)
    * Phục hồi lỗi và truyền lại dữ liệu bị mất
    * Đảm bảo dữ liệu truyền đúng thứ tự (sequencing)
    * Kiểm soát luồng (flow control): tránh gửi quá nhanh so với khả năng xử lý của máy nhận

- Cung cấp lớp địa chỉ tầng 4 (Port Number)
    * Xác định ứng dụng / dịch vụ đang sử dụng giao thức
    * Hỗ trợ ghép kênh phiên (session multiplexing)

---

# Port Number / Session Multiplexing

- Session (phiên làm việc) là kết nối giữa 2 thực thể (client ↔ server)
    * Ví dụ: user truy cập server để trao đổi dữ liệu trong một khoảng thời gian

- Port number là số cổng dùng để:
    * Xác định ứng dụng / dịch vụ đang chạy trên cùng một thiết bị
    * Giúp máy tính phân biệt nhiều dịch vụ cùng lúc
    * IP xác định thiết bị, Port xác định dịch vụ trên thiết bị đó

---

# Phân loại Port

- Well-known ports (0 - 1023)
    * Do server sử dụng để lắng nghe dịch vụ
    * Được IANA quản lý
    * Ví dụ:
        * HTTP → 80
        * HTTPS → 443
        * SSH → 22
        * DNS → 53

- Registered ports (1024 - 49151)
    * Dành cho ứng dụng / dịch vụ được đăng ký
    * Ít cố định hơn well-known ports

- Ephemeral ports (49152 - 65535)
    * Port tạm thời do client tự động cấp khi kết nối
    * Ví dụ: 50000, 61001, 49521, ...

---

# Source Port & Destination Port

- Source Port (Src Port): cổng của thiết bị gửi
    * Xác định ứng dụng đang tạo kết nối
    * Giúp nhận phản hồi đúng tiến trình
    * Ví dụ: Chrome mở kết nối → Src Port 50000

- Destination Port (Dst Port): cổng của dịch vụ bên nhận
    * Xác định dịch vụ mà client muốn truy cập
    * Ví dụ: truy cập web → Dst Port 80 (HTTP)

---

# Ví dụ PC1 truy cập SV1 qua Internet

- Gói tin đi (Request):
    * IP Src: PC1
    * IP Dst: SV1
    * Src Port: 50000 (client tự chọn ngẫu nhiên)
    * Dst Port: 80 (HTTP service)

- Gói tin về (Response):
    * IP Src: SV1
    * IP Dst: PC1
    * Src Port: 80
    * Dst Port: 50000

---

# Ý nghĩa

- IP dùng để xác định thiết bị (host)
- Port dùng để xác định dịch vụ (application)
- Router xử lý ở Layer 3 (IP), không quan tâm port
- TCP/UDP xử lý ở Layer 4 (port + session)


# IANA (Internet Assigned Numbers Authority)

- IANA là tổ chức chịu trách nhiệm quản lý các tài nguyên số cốt lõi của Internet
- Hiện thuộc quyền quản lý của ICANN (Internet Corporation for Assigned Names and Numbers)

---

# IANA làm gì?

- Quản lý và cấp phát các tài nguyên quan trọng của Internet:
    * Địa chỉ IP (IPv4, IPv6)
    * Hệ thống tên miền gốc (DNS Root Zone)
    * Số hiệu giao thức (Protocol Numbers: TCP, UDP, ICMP,...)
    * Port Numbers (số cổng dịch vụ mạng)

---

# IANA và Port Number

- IANA chịu trách nhiệm chuẩn hóa và quản lý các dải port
- Gán các port cố định cho các dịch vụ phổ biến trên Internet
- Giúp tránh xung đột port giữa các ứng dụng toàn cầu

---

# Các dải Port do IANA quản lý

- Port number là trường 16 bit trong TCP/UDP
    * Giá trị nằm trong khoảng: 0 - 65535

- Well-known ports (0 - 1023)
    * Dành cho các dịch vụ hệ thống quan trọng
    * Được IANA quản lý chặt chẽ
    * Ví dụ:
        * HTTP → 80
        * HTTPS → 443
        * SSH → 22
        * DNS → 53

- Registered ports (1024 - 49151)
    * Dành cho các ứng dụng / dịch vụ được đăng ký với IANA
    * Thường dùng bởi phần mềm bên thứ ba
    * Không cố định như well-known ports

- Dynamic / Ephemeral ports (49152 - 65535)
    * Port tạm thời do hệ điều hành tự cấp phát
    * Dùng cho client khi khởi tạo kết nối ra ngoài Internet
    * Mỗi kết nối có thể dùng một port khác nhau

# Tóm tắt nhanh

- IANA = tổ chức chuẩn hóa tài nguyên Internet
- Với Port:
    * Gán port cố định cho dịch vụ phổ biến
    * Quản lý tránh trùng port toàn cầu
    * Đảm bảo tính thống nhất giữa các hệ thống mạng

# 1. TCP - Transmission control protocol

- Là giao thức hướng kết nối (Connection-oriented)
    * Hai thiết bị phải thiết lập kết nối trước khi truyền dữ liệu
- Truyền dữ liệu đáng tin cậy (Reliable Delivery)
- Đảm bảo dữ liệu đến đúng thứ tự (Sequencing)
- Kiểm soát luồng dữ liệu (Flow Control)
    * Điều chỉnh tốc độ gửi để tránh bên nhận bị quá tải
- Có cơ chế phát hiện lỗi và truyền lại dữ liệu (Retransmission)

---

## TCP Segment

- Các Field trong TCP Header (không cần nhớ hết cho CCNA)
- Source Port: 16 bit
- Destination Port: 16 bit
- Sequence Number: 32 bit
    * Đánh số byte đầu tiên của dữ liệu trong Segment
- Acknowledgment Number: 32 bit (khi ACK = 1)
    * Xác nhận byte tiếp theo mà bên nhận mong muốn nhận được
- Sequence Number và Acknowledgment Number
    * Giúp TCP truyền dữ liệu đúng thứ tự
    * Giúp TCP đảm bảo truyền dữ liệu đáng tin cậy
- Flags (Control Bits)
    * Một số Flag quan trọng:
        * SYN: Thiết lập kết nối
        * ACK: Xác nhận dữ liệu
        * FIN: Đóng kết nối
- Window Size
    * Dùng cho Flow Control
    * Cho biết bên nhận còn có thể nhận thêm bao nhiêu byte dữ liệu

---

## Hướng kết nối

### Establishing Connection: Three-Way Handshake (Thiết lập kết nối)

- PC1 muốn truy cập HTTP trên Server
- PC1 phải thiết lập kết nối TCP trước
- Sử dụng hai Flag chính:
    * SYN (Synchronize)
    * ACK (Acknowledgment)

- Bước 1:
    * PC1 gửi TCP Segment
    * SYN = 1
    * Seq = x (số ngẫu nhiên)

- Bước 2:
    * Server gửi lại TCP Segment
    * SYN = 1
    * ACK = 1
    * Seq = y (số ngẫu nhiên)
    * Ack = x + 1

- Bước 3:
    * PC1 gửi TCP Segment
    * ACK = 1
    * Seq = x + 1
    * Ack = y + 1

- Sau bước 3, kết nối TCP được thiết lập

---

### Terminating Connection: Four-Way Handshake (Đóng kết nối)

- Bước 1:
    * PC1 gửi FIN

- Bước 2:
    * Server gửi ACK

- Bước 3:
    * Server gửi FIN

- Bước 4:
    * PC1 gửi ACK

- Sau bước 4, kết nối TCP kết thúc

---

## Sequence Number và Acknowledgment Number

- Mỗi bên tự chọn một Sequence Number ban đầu (Initial Sequence Number - ISN)
- ISN là số ngẫu nhiên nhằm tăng tính bảo mật

Ví dụ:

- PC1 gửi:
    * SYN
    * Seq = 10

- Server trả lời:
    * SYN + ACK
    * Seq = 50
    * Ack = 11

- PC1 gửi:
    * ACK
    * Seq = 11
    * Ack = 51

- Sau khi bắt đầu truyền dữ liệu:
    * Sequence Number tăng theo số byte dữ liệu đã gửi
    * Không phải lúc nào cũng tăng 1

- Acknowledgment Number
    * Luôn là số byte tiếp theo mà bên nhận mong muốn nhận được

Ví dụ:

- PC1 gửi 100 byte dữ liệu bắt đầu từ Seq = 11

- Server sẽ trả:
    * Ack = 111

=> Nghĩa là Server đã nhận đủ đến byte 110 và đang chờ byte 111

---

## TCP Retransmission

- TCP đảm bảo dữ liệu được truyền đầy đủ
- Sau khi gửi một Segment:
    * TCP sẽ chờ ACK từ bên nhận

- Nếu hết thời gian chờ (Retransmission Timeout - RTO) mà chưa nhận ACK:
    * TCP sẽ gửi lại Segment đó

- Nếu nhận được 3 Duplicate ACK:
    * TCP thực hiện Fast Retransmit
    * Không cần chờ hết thời gian RTO

- Segment truyền lại có:
    * Sequence Number giống Segment bị mất
    * Payload giống Segment trước

- Sau khi bên nhận nhận được Segment:
    * Bên nhận gửi ACK xác nhận
    * TCP tiếp tục truyền các Segment tiếp theo

---

## Ghi nhớ nhanh

- SYN: Thiết lập kết nối
- ACK: Xác nhận dữ liệu
- FIN: Kết thúc kết nối
- Seq: Byte đầu tiên của dữ liệu trong Segment
- Ack: Byte tiếp theo mà bên nhận mong muốn nhận
- RTO: Không có ACK → Gửi lại
- 3 Duplicate ACK → Fast Retransmit


# 2. UDP - User Datagram Protocol

- Là giao thức hướng không kết nối (Connectionless)
- Host không cần thiết lập kết nối trước khi gửi dữ liệu
- Không cung cấp truyền dữ liệu đáng tin cậy
    * Không có cơ chế ACK
    * Không có cơ chế Retransmission (truyền lại)
    * Có thể mất dữ liệu
- Không đảm bảo dữ liệu đến đúng thứ tự
    * Không có Sequence Number trong Header
- Không kiểm soát luồng dữ liệu (Flow Control)
- Header đơn giản, chỉ gồm 4 Field:
    * Source Port
    * Destination Port
    * Length
    * Checksum
- Header chỉ 8 byte nên tốc độ xử lý nhanh hơn TCP

---

# So sánh TCP và UDP

- TCP
    * Hướng kết nối (Connection-oriented)
    * Đáng tin cậy (Reliable)
    * Có ACK và Retransmission
    * Đảm bảo dữ liệu đến đúng thứ tự
    * Có Flow Control
    * Header lớn hơn (ít nhất 20 byte)
    * Chi phí xử lý cao hơn UDP

- UDP
    * Hướng không kết nối (Connectionless)
    * Không đảm bảo dữ liệu đến nơi
    * Không ACK
    * Không Retransmission
    * Không đảm bảo đúng thứ tự
    * Không Flow Control
    * Header nhỏ (8 byte)
    * Tốc độ nhanh hơn TCP

---

# Khi nào sử dụng?

- TCP
    * HTTP / HTTPS
    * FTP
    * SSH
    * SMTP
    * IMAP / POP3

- UDP
    * DNS
    * DHCP
    * TFTP
    * VoIP
    * Video Streaming
    * Online Gaming

---

# Ghi nhớ nhanh

- TCP = Tin cậy nhưng chậm hơn
- UDP = Nhanh nhưng không đảm bảo dữ liệu
- Ứng dụng cần độ chính xác → TCP
- Ứng dụng ưu tiên tốc độ, chấp nhận mất một ít dữ liệu → UDP

# Các dịch vụ sử dụng TCP

- FTP (Data) → 20
- FTP (Control) → 21
- SSH → 22
- Telnet → 23
- SMTP → 25
- DNS (Zone Transfer) → 53
- HTTP → 80
- POP3 → 110
- IMAP → 143
- HTTPS → 443
- SMB → 445
- RDP → 3389

---

# Các dịch vụ sử dụng UDP

- DHCP Server → 67
- DHCP Client → 68
- TFTP → 69
- SNMP → 161
- SNMP Trap → 162
- RIP → 520
- Syslog → 514
- NTP → 123

---

# Các dịch vụ sử dụng cả TCP và UDP

- DNS → 53
    * UDP: Truy vấn DNS thông thường
    * TCP: Zone Transfer hoặc phản hồi dữ liệu lớn

---

