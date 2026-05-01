- Rip - Routing information protocol (Giao thức thông tin định tuyến)
- có metric: hop-count, tối đa là 15
    * mỗi router là 1 hop
    * di tới 16 router = unreachable (không tới được)
- có 3 version:
    * RIPv1 -> IPv4
    * RIPv2 -> IPv4
    * RIPv3 -> IPv6

# 1. Message
- Rip có 2 gói tin
    * Request: hỏi rotuer liền kề bật rip -> để gửi gói tin cho nhau
    * Reponse: gửi nội bộ bảng định tuyến
- mỗi update gói tin sẽ được gởi mỗi 30 giây

# 2. Version

## 2.1. RIPv1
- chỉ quảng bá các classfull gồm A, B và C
- không hổ trợ VLSM và CIDR (tức không hổ trợ các mạng không có chia subnet-mask)
    * với mạng 10.1.1.0/24 thì sẽ bị hiểu thành 10.0.0.0 A
    * 172.16.192.0/18 ->  172.16.0.0 B
- chỉ gửi message đến broadcast *255.255.255.255*
- các Router nội bộ sẽ nhận

## 2.2. RIPv2
- có hổ trợ VLSM và CIDR
- các gói tin RIP sẽ mang theo subnet mask trong update
- multicast: **224.0.0.9**
- chỉ rotuer RIP mới nhận -> giảm tải mạng
- Subnet quảng bá gửi kèm:
    * Network 
    * Subnet mask (prefix length) 
- các router sẽ quét tất các interface 
    * check ip thuộc network nào
    * Interface có bật RIP không
    * Nếu có RIP -> send/recive RIP update qua interface đó
- mặc định RIPv2 bật auto-summary
    * auto-summary là: Khi gửi route qua khác class network boundary -> RIP sẽ tự gom về classful network
        * khi có 2 mạng là 192.168.1.0/24 và 192.168.2.0/24 -> RIP sẽ gom thành 192.168.0.0/16 để gửi ra ngoài
    * ta nên tắt auto-summary do:
        * Gây sai route trong:
        * VLSM
        * WAN nhiều subnet
        * Topology phức tạp

# 2.3. RIPv3
- sử dụng trong IPv6
- Về bản chất giống RIPv2 nhưng mở rộng IPv6

# 3. Một số lưu ý
- rip
    * network 10.0.0.0
- khi khai báo network 10.0.0.0 thì Router sẽ so sánh với classful network 10.0.0.0/8 Tức là kiểm tra interface nào có IP thuộc 10.x.x.x
    * ví dụ 2 giao diện sử dụng RIP có ip 10.0.12.1/24 và 10.0.13.1/24 sẽ **MATCH** 
- network không nói router mạng được quảng bá -> mà nói giao diện nào đang bật RIP -> router sẽ quảng bá prefix của giao diện đó
- nếu Router dùng RIP kết nối không phải *layer 3* thì nó vẫn gửi gói RIP update tới giao diện đó -> sẽ tạo ra lưu lượng mạng không cần thiết
    * R1(config-router)# passive-interface g2/0
    * lệnh sẽ không gửi bảng định tuyến đến giao diện đso
    * nhưng vẫn gửi bảng định tuyến của giao diện đó đến các mạng layer 3 khác
- quảng bá 0.0.0.0/0 ra internet
    * ip route 0.0.0.0 0.0.0.0 <ip giao diện ra internet>
    * báo với router khác là router này sẽ ra internat đối với các gói tin muốn gửi ra ngoài
- R1(config-router)# default-information orginate
    * chia sẻ default router đến các router khác trong cùng AS