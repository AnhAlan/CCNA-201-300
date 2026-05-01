# 1.EIGRP
- EIGRP - Enhanced Interior Gateway Routing Protocol (Giao thức định tuyến cổng nội bộ nâng cao)
- phiên bản cũ là: IGRP (Interior Gateway Routing Protocol)
- từng là độc quyền Cisco nhưng đã public 
- EIGRP sẽ tối ưu hơn so với RIP;
    * hội tụ nhanh hơn (DUAL)
    * metric tốt hơn (bandwidth, delay)
    * không bị giới hạn 15 hop
    * hỗ trợ unequal-cost load balancing (variance)
    * gửi update khi có thay đổi (partial update)
    * hạn chế loop (feasibility condition)
- Multicast: 224.0.0.10
- trong khi rip load balance khi metric bằng nhau thì EIGRP là IGP duy nhất có thể câng bằng dù metric khác nhau (tệ một chút)
    * lệnh variance (mặc định = 1)
    * cho phép load balance unequal-cost
- EIGRP 2 != EIGRP 1
    * không kết nối khi khác AS
- nếu lệnh không thêm rõ phần prefix (/) thì nó sẽ tự động dùng classfull
- EIGRP thêm prefix bằng wild-card định danh rõ ràng
    * ví dụ: network 10.0.0.0 0.0.0.255
- wild-card của cisco
    * 255.255.255.0 -> có wild-card là 0.0.0.255
    * cách tính: wildcard = 255.255.255.255 - subnet mask

# 2. Distance
## 2.1. FD - feasible distance
- là metric tốt nhất từ router hiện tại đến đích
- FD = metric của đường đi tốt nhất (successor)

## 2.2. RD - reported distance
- là metric mà neighbor báo về
- là khoảng cách từ *neighbor* đến đích

## 2.3. Successor
- là đường đi tốt nhất (metric nhỏ nhất)
- được đưa vào bảng routing 
- có thể có nhiều successor nếu metric bằng nhau

## 2.4. Feasible Successor
- Đường dự phòng (backup)
- Không nằm trong routing table, mà nằm trong topology table
- Phải thỏa: RD < FD
    * Router liền kề đến đích phải có metric nhỏ hơn metric router chính nó đến đích    
    * nếu metric router liền kề lớn hơn tức nó đi ngược lại qua router chính nó hoặc đi đường khác có metric lớn hơn
- Khi route chính mất -> dùng ngay (không cần tính lại)

## 2.4. Feasibility condition
- là điều kiện để chọn router liền kề thành feasible successor
- điều kiện: RD < FD
- hợp lệ sẽ có hơn 2 tuyến đường đi
- đảm bảo không loop

## 2.5 Khi successor lỗi
- trường hợp 1: có Feasible Successor
    * Feasible Successor sẽ lên làm successor
    * cập nhật FD theo đường mới
-trường hợp 2: không có Feasible Successor
    * khi đó router mới sẽ gửi query và chạy lại  DUAL full recomp

# 3. load balance
- equal-cost load balancing khi
    * nhiều đường có cùng metric
- unequal-cost load balancing -> cho phép dùng thêm các đường tệ hơn 1 chút
    * dùng variance
    * cho phép dùng đường metric lớn hơn
    * điều kiện: metric <= variance * FD (best)
        * ví dụ: với FD = 100 và variance = 2
        * 2 * 100 = 200
        * Path B: FD = 150 -> sử dụng
        * Path C: FD = 180 -> sử dụng
        * Path D: FD = 250 → không sử dụng
- số đường tối đa mặc định: 4
    * có thể chỉnh bằng: maximum-paths