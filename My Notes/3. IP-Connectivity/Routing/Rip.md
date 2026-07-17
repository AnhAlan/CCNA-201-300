# 1. RIP

- RIP - Routing Information Protocol (Giao thức thông tin định tuyến)
- Là giao thức Dynamic Routing kiểu Distance Vector
- Metric
	* Hop Count
	* Mỗi Router = 1 Hop
	* Tối đa 15 Hop
	* Metric = 16 -> Unreachable
- Administrative Distance
	* RIP = 120
- Transport
	* UDP Port 520 (IPv4)
	* UDP Port 521 (RIPng)
- Chu kỳ gửi Update
	* Mỗi 30 giây
	* Khi topology thay đổi sẽ gửi Triggered Update
- Có 3 phiên bản
	* RIPv1 -> IPv4
	* RIPv2 -> IPv4
	* RIPng (RIPv3) -> IPv6

# 2. Message

- RIP có 2 loại Message
	* Request
		** Yêu cầu Neighbor gửi Routing Table
	* Response
		** Chứa Routing Update
		** Được gửi định kỳ mỗi 30 giây
		** Gửi ngay khi topology thay đổi (Triggered Update)

# 3. Version

## 3.1. RIPv1

- Chỉ hỗ trợ Classful Routing
- Không hỗ trợ VLSM
- Không hỗ trợ CIDR
- Không gửi Subnet Mask trong Update
- Broadcast
	* 255.255.255.255
- Auto Summary mặc định

## 3.2. RIPv2

- Hỗ trợ Classless Routing
- Hỗ trợ VLSM
- Hỗ trợ CIDR
- Gửi kèm Prefix Length (Subnet Mask)
- Multicast
	* 224.0.0.9
- Chỉ Router chạy RIP mới nhận Update
- Mặc định bật Auto Summary
	* Nên tắt bằng no auto-summary

## 3.3. RIPng

- Dùng cho IPv6
- Tương tự RIPv2
- UDP Port 521

# 4. Network

- Lệnh network dùng để chọn Interface chạy RIP
- Không dùng để quảng bá trực tiếp Network
- Router sẽ kiểm tra các Interface thuộc Major Network
	* Ví dụ
		** network 10.0.0.0
		** Interface 10.1.1.1/24 -> Match
		** Interface 10.2.1.1/24 -> Match
		** Interface 192.168.1.1/24 -> Không Match

# 5. Auto Summary

- Mặc định RIPv2 bật Auto Summary
- Khi Route đi qua Classful Boundary
	* RIP sẽ tự động gộp Route về Classful Network
- Ví dụ
	* 172.16.1.0/24
	* 172.16.2.0/24
	* Gửi thành 172.16.0.0/16
- Không nên dùng trong
	* VLSM
	* CIDR
	* WAN nhiều Subnet
	* Topology phức tạp

# 6. Passive Interface

- Chặn gửi RIP Update trên Interface
- Vẫn quảng bá Network của Interface đó đến Router khác
- Giảm lưu lượng không cần thiết
- Tăng bảo mật

# 7. Default Route

- Tạo Default Route
	* ip route 0.0.0.0 0.0.0.0 <next-hop>

- Quảng bá Default Route
	* default-information originate

# 8. Loop Prevention

- Split Horizon
	* Không quảng bá Route trở lại Interface đã học

- Route Poisoning
	* Khi Route bị lỗi
		** Metric = 16

- Poison Reverse
	* Gửi lại Route với Metric = 16

- Hold-down Timer
	* Tạm thời không nhận Route kém hơn

- Triggered Update
	* Gửi Update ngay khi Topology thay đổi

# 9. Timer

- Update Timer
	* 30 giây

- Invalid Timer
	* 180 giây

- Hold-down Timer
	* 180 giây

- Flush Timer
	* 240 giây