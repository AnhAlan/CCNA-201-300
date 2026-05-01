- Các host nằm khác mạng không thể giao tiếp trực tiếp (không ping được nhau)
- Vì chúng thuộc broadcast domain khác nhau
- Dữ liệu không thể tự “nhảy” sang mạng khác nếu không có thiết bị trung gian
- Routing ra đời để giải quyết vấn đề này
- Router giúp kết nối các mạng khác nhau
- Đóng vai trò như “người dẫn đường” cho gói tin
- Nhờ routing, các host khác mạng có thể ping và trao đổi dữ liệu với nhau

# 1. Routing
- gồm có 2 kiểu routing
    * IGP - Internal Gateway Protocol
    * EGP - external Gateway protocol

## 1.1. IGP
- Routing bên trong 1 hệ thống tự trị (hay AS - Autonomous System)
- gồm các protocol:
    * RIP
    * OSPF
    * EIGRP
    * IS-IS
- Các protocol sử dụng Algorithm:
    * distance vector: RIP, EIGRP
    * Link-state: OSPF, IS-IS
- thường dùng trong nội bộ công ty / tổ chức
- mục tiêu: tìm đường nhanh, tối ưu nội bộ

## 1.2. EGP
- Routing giữa các hệ thống tự trị AS
- Hiện tại chỉ còn protocol BGP được sử dụng
- BGP sủ dụng algorithm là Path-vector

# 2. Algorithm
## 2.1. Distance vector routing
- có trước link-state -> 1980s
- RIPv1 và IGRP (tiền thân EIGRP) của cisco
- chỉ gửi cho router neighbor gồm:
    * điểm đến mạng mà Router biết
    * và metric tới mạng đó
- còn được gọi là "routing by rumor" -> vì nó chỉ biết các router liền kề và chỉ biết các thông tin mà router liền kề nói ra
- 

# 2.2. Link state routing
- Mỗi router sẽ tạo bản đồ y nhau
- quảng bá cho các rotuer liền kề -> và các router liền kề gửi cho các router liền kề khác (khá giống với BFS)
- dùng *map* để khái quá bản đồ tính toán các tuyến đường tốt nhất cho mỗi điểm đến
- link state dùng nhiều tài nguyên cpu
- nhanh phản ứng để theo cấu trúc mạng thay đổi

# 3. Metric
- các bảng định tuyến sẽ chọn tuyến đường tốt nhất mà nó biết
- dùng metrix thấp nhất
- mỗi giao thức sẽ có metric khác nhau
- nếu có hơn 2 đường đi nằm trong cùng 1 mạng nhưng cùng 1 metrix -> dùng ECMP (equal cost multi path)
    * thay vì chọn 1 tuyến đường -> nó sẽ chọn nhiều tuyến đường cùng 1 lúc
    * chỉ xảy ra khi 2 cost bằng nhau
    * đối với static routing thì không có ECMP -> nên có value là 0

## 3.1. Rip
- metric là hop-count, tức khi gói tin đi qua router khác thì sẽ giảm 1 giá trị xuống (gần giống TTL)
- tối đa hop-count của Rip là 15 -> nếu qua hơn 15 router -> gói tin sẽ drop
- các băng thông trên các đường router sẽ không quan tâm

# 3.2. EIGRP
- metric là deplay -> tổng băng thông thấp + độ trễ cộng dồn

# 3.3. OSPF
- metric là cost được tính: refeced bandwith / interface bandwith trên 1 giao điện
- mỗi tuyến đường sẽ tính tổng cộng dồn và chọn cost thấp nhất

# 3.4 IS-IS
- metric là cost được admin tự cấu hình
- mặc định là 10 mỗi băng thông -> phải cấu hình chuẩn

# 4. AD - Administrative Distance
- 1 công ty hay hệ thống có thể sử dụng hơn 2 protocol
- nếu các protocol sử dụng metric khác nhau 
    * RIP dùng metric la hop-count
    * OSPF dùng metric là cost
- do không biết lựa chọn protocol nào để quyết định sử dụng -> chọn protocol nào có AD thấp nhất
- mỗi protocol sẽ có AD khác nhau
    * nối trực tiếp: 0
    * Static: 1
    * external BGP: 20
    * EIGRP: 90
    * IGRP: 100
    * OSPF: 110
    * IS-IS: 115
    * RIP: 120
    * external EIGRP: 170
    * Internal BGP: 200
    * *unknow*: 255 -> không tin tươnger
- AD ở trên được xếp hạng bởi Cisco
- có thể chỉnh AD
    * khi có Dynamic và satic
    * tăng AD static sao cho lớn hơn Dynamic <-> AD static > AD dynamic
    * gọi là Floating static routing

- lưu ý: chọn route protocol dựa vào (Route-Selection)
    * subnet-mask match mà lớn nhất
    * lowest AD
    * Lowest Metric
