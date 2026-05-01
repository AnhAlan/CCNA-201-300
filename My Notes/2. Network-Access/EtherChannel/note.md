- Oversubscription (vượt mức): xảy ra khi tổng băng thông từ host đổ lên access switch lớn hơn băng thông uplink lên distribution / core switch
    * với 24 pc dùng fastEthernet nối switch: 24 * 100 mbps = 2400 mbps
    * switch access nối swtich distribution dùng 1 gigabitethernet: 1000 mbps
    * Oversubscription = tổng host / tổng access = 2400 / 1000 ~ 2.4 -> tỷ lệ 2.4:1 
    * mặc dù băng thông không đủ xử lý nhưng với các tỷ lệ: 3:1, 4:1 -> vẫn dùng được với các văn phòng
    * tỷ lệ 1:1 ứng dụng thời gian thực
- với tỷ cao lệ ta nên dùng Etherchannel để tăng tổng băng thông

# 1. Etherchannel
- Etherchannel là nối nhiều cổng giữa 2 switch thay vì 1 cổng, và các cổng này hoạt động như 1 cổng
    * Nếu chỉ nối nhiều cổng bình thường chắc chắn sẽ xảy STP và nhiều cổng sẽ bị blocking
    * nên nhiều cổng hoạt động như 1 cổng sẽ không xảy ra loop và xử lý tốc độ cao hơn
- tên gọi khác của Etherchannel: 
    * port channel
    * LAG (link aggregation group)
- khi có một gói tin đi qua, dựa vào flow là giao tiếp giữa 2 node của mạng, được xác định thuật toán **hashing** để xác định gói tin đi qua link nào. Đó là load balance của LAG

# 2. Load balance của LAG
- một gói tin đi qua, xác định flow bằng cách hashing
    * MAC destination / soure
    * TP destionation / soure
    * TCP / UDP port soure / destionation
    * hoặc kết hợp các yếu tố trên
    * có thể cấu hình load-balance theo nhu cầu (tức các option có sẵn)
- các gói tin cùng flow sẽ đi qua một link duy nhất để
    * tránh gói tin đến sai thứ tự
    * đảm bảo TCP không bị giảm hiệu năng
    * Một flow KHÔNG thể vượt quá băng thông của 1 link
- hệ quả:
    * trường hợp ít flow nhưng dữ liệu lớn -> mất cân bằng -> nhiều gói tin đi qua cùng 1 link
    * nhiều flow nhỏ -> khi đó các flow được phân tán đều giữa các link -> load balance tốt hơn

# 3. Ba phương pháp cấu hình EtherChannel
## 3.1. PAGP - port aggregation protocol
- chỉ hoạt động trên cisco
- tự động đàm phám
- Mode:
    * auto: chờ phía bên kia (passive)
    * desirable: chủ động gửi gói PAgP

## 3.2. LACP - Link aggregation control protocol
- tiêu chuẩn IEEE 802.3AD - tương thích nhiều hãng
- Mode:
    * passive: chờ (giống auto)
    * active: chủ động (giống desirable)
## 3.3. Static EtherChannel
- cấu hình thủ công gộp cổng
- mode: on (static) -> không gửi gói PAGP hay LACP
- không tự phát hiện lỗi sai -> không linh hoạt
- khuyến khích không dùng

# 3.4 Lưu ý
- static: chỉ tối đa sử dụng 8 port
- LACP: 16 port
    * nếu sử dụng 16 port -> 8 forward và 8 standby mode
    * standby: dự phòng không truyền dữ liệu
- PAGP: 8 port (max)
- PAgP và LACP đều có cơ chế phát hiện mismatch cấu hình
- LACP mạnh và tiêu chuẩn hơn → được khuyến nghị sử dụng
- Các port muốn gộp lại → phải cùng channel-group number
    * interface f0/1
        * channel-group 1 mode active
    * interface f0/2
        * channel-group 1 mode active
- tuy nhiên giữa 2 switch có thể khác số channel
    * switch A: fa0/1 fa0/2 -> channel-group 1
    * switch B: fa0/1 fa0/2 -> channel-group 5
- Đảm bảo các port của chính switch đó cùng channel là được
- lưu ý chế độ channel: auto - auto -> không tạo EtherChannel
- có thể gộp link layer 3
    * interface range g0/1 - 2
        * no switchport
        * channel-group 1 mode active
- Đảm bảo các yếu tố của giao diện để có thể thành LAG
    * cùng Duplex
    * cùng speed
    * cùng switchport mode (access / trunk)
    * cùng vlan, native vlan
    * không khớp -> không tạo LAG
- Mỗi EtherChannel là độc lập nên:
    * 2 thiếu bị bắc buộc cùng protocol (LACP / PAGP / static)
    * không bắt buộc cùng thuật toán hash
    * Có thể chọn thuật toán hash:
        * MAC-based
        * IP-based
        * hoặc kết hợp
    * L2 thường dùng MAC
    * L3 thường dùng IP
    * tùy thiết kế và lưu lượng mạng

