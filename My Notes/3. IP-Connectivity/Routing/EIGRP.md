# 1. EIGRP

- EIGRP - Enhanced Interior Gateway Routing Protocol (Giao thức định tuyến cổng nội bộ nâng cao)
- Phiên bản cũ là IGRP (Interior Gateway Routing Protocol)
- Ban đầu là giao thức độc quyền Cisco, sau đó được công bố một phần thành chuẩn mở
- Là giao thức định tuyến Dynamic, Hybrid (Advanced Distance Vector)
- Administrative Distance
	* Internal EIGRP: 90
	* External EIGRP: 170
- Multicast: 224.0.0.10
- Protocol Number: 88
- EIGRP tối ưu hơn RIP
	* Hội tụ nhanh nhờ thuật toán DUAL
	* Metric mặc định dựa trên Bandwidth và Delay
	* Không giới hạn 15 hop
	* Hỗ trợ unequal-cost load balancing (variance)
	* Chỉ gửi Partial Update khi topology thay đổi
	* Tránh loop nhờ Feasibility Condition và DUAL
- EIGRP chỉ trở thành Neighbor khi cùng AS Number
	* Ví dụ:
		** router eigrp 1
		** router eigrp 2
		** Không trở thành Neighbor
- Có thể chỉ định Wildcard Mask để quảng bá chính xác interface
	* ví dụ:
		** network 10.0.0.0 0.0.0.255
- Wildcard Mask
	* wildcard = 255.255.255.255 - subnet mask
	* ví dụ:
		** 255.255.255.0 -> 0.0.0.255
		** 255.255.0.0 -> 0.0.255.255

# 2. Metric

- Metric mặc định được tính từ
	* Bandwidth
	* Delay
- Metric nhỏ hơn sẽ được ưu tiên

# 3. Distance

## 3.1. Feasible Distance (FD)

- Là metric tốt nhất từ router hiện tại đến đích
- FD là metric của Successor

## 3.2. Reported Distance (RD)

- Là metric Neighbor báo về
- Là khoảng cách từ Neighbor đến đích

# 4. Successor

## 4.1. Successor

- Là đường đi tốt nhất
- Có metric nhỏ nhất
- Được đưa vào Routing Table
- Có thể có nhiều Successor nếu cùng metric

## 4.2. Feasible Successor

- Là đường dự phòng (Backup)
- Không nằm trong Routing Table
- Được lưu trong Topology Table
- Điều kiện
	* RD < FD
- Khi Successor mất
	* Được thay thế ngay
	* Không cần chạy lại DUAL

## 4.3. Feasibility Condition

- Điều kiện chọn Feasible Successor
	* RD < FD
- Đảm bảo không xảy ra Routing Loop

## 4.4. Khi Successor bị lỗi

- Có Feasible Successor
	* Thay thế ngay
	* Cập nhật FD mới

- Không có Feasible Successor
	* Gửi Query đến Neighbor
	* Chạy lại thuật toán DUAL
	* Tính toán đường đi mới

# 5. Load Balancing

- Equal-cost Load Balancing
	* Nhiều đường có cùng metric

- Unequal-cost Load Balancing
	* Sử dụng Variance
	* Điều kiện
		** Metric <= Variance × FD
	* Ví dụ
		** FD = 100
		** Variance = 2
		** Metric = 150 -> sử dụng
		** Metric = 180 -> sử dụng
		** Metric = 250 -> không sử dụng

- Mặc định tối đa 4 đường
	* Có thể thay đổi bằng maximum-paths

# 6. Neighbor

- Điều kiện hình thành Neighbor
	* Cùng AS Number
	* Cùng K-value
	* Cùng subnet
	* Interface không Passive

# 7. Table

- Neighbor Table
	* Lưu thông tin Neighbor

- Topology Table
	* Lưu toàn bộ Route học được
	* Chứa Successor
	* Chứa Feasible Successor

- Routing Table
	* Chỉ chứa Successor