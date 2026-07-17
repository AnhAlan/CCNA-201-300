# FHRP - First Hop Redundancy Protocols
- là nhóm giao thức giúp dự phòng default gateway cho host trong LAN
- thay vì:
    * 1 router làm gateway -> ta dùng nhiều router với 1 IP ảo làm gateway

# 1. Vấn đề FHRP giải quyết
- trong mạng, pc kết nối Router (là default gateway)
- khi Router down -> mất mạng dù LAN vẫn sống
- FHRP giải quyết:
    * tạo Virutal IP (VIP)
    * nhiều router chia vai:
        * 1 active
        * 1 standby (backup)
    
# 2. Các giao thức FHRP chính
## 2.1. HSRP (cisco độc quyền)
- HSRP - hot standby router protocol
- gồm Active và Standby
    * Active: đang xử lý traffic
    * Standby: dự phòng
- Client sẽ không biết router nào đang làm gateway
- chỉ biết 1 IP ảo (Virutal IP)
- gồm 2 version: HSRPv1 và HSRPv2
    * HSRPv2 hổ trợ nhiều group và hổ trợ IPv6
- Multicat IPv4:
    * HSRPv1: 224.0.0.2
    * HSRPv2: 224.0.0.102
- Virtual MAC:
    * V1: 0000.0C07.ACxx
    * v2: 0000.0C9F.Fxxx
    * xx / xxx = group ID
- Nếu mạng có nhiều VLAN hoặc subnet, có thể cấu hình mỗi VLAN/subnet sử dụng một Active Router khác nhau.
- Cách này giúp phân chia lưu lượng giữa các router (load sharing/load balancing giữa các VLAN), tránh chỉ một router xử lý toàn bộ traffic.
- ví dụ: 
    * vlan 10: R1 active và R2 standby
    * vlan 20: R2 active và R1 standby
    * đảm bảo các Router đều hoạt động

- UDP Port
    * 1985
- Hello Timer
    * mặc định 3 giây

- Hold Timer
    * mặc định 10 giây

- Election
    * Priority lớn hơn sẽ thắng.
    * Mặc định Priority = 100.
    * Nếu Priority bằng nhau thì Router có IP lớn hơn sẽ thắng.
- Preempt
    * Mặc định tắt.
    * Nếu bật thì khi Router Priority cao quay trở lại sẽ giành lại vai trò Active.
- Authentication
    * Plain Text
    * MD5
- Interface Tracking
    * Theo dõi trạng thái Interface.
    * Nếu Interface Down thì Priority sẽ giảm.
    * Có thể làm Router Active chuyển quyền cho Router khác.

- Nếu mạng có nhiều VLAN hoặc Subnet thì có thể cấu hình:
    * VLAN 10
        * R1 Active
        * R2 Standby
    * VLAN 20
        * R2 Active
        * R1 Standby

- Cách này giúp chia tải giữa các Router (Load Sharing).

- Lưu ý
    * HSRP không tự Load Balancing trong cùng một VLAN.
    * Muốn chia tải phải dùng nhiều Group trên nhiều VLAN/Subnet.
    * Nếu muốn nhiều Router cùng chia tải trong một VLAN thì dùng GLBP


## 2.2. GLBP (Cisco độc quyền)
- GLBP - Gateway Load Balancing Protocol
- Chỉ hoạt động trên thiết bị Cisco.
- Vừa dự phòng Gateway vừa Load Balancing.
- Tất cả Router đều có thể Forward Traffic.
- Client vẫn chỉ cấu hình 1 Virtual IP.
- Có 2 vai trò
    * AVG (Active Virtual Gateway)
        * Chịu trách nhiệm trả lời ARP.
    * AVF (Active Virtual Forwarder)
        * Chịu trách nhiệm Forward Traffic.

- Một AVG có thể quản lý nhiều AVF.
- Mỗi AVF có Virtual MAC riêng.
- Khi Client ARP Virtual IP
    * AVG sẽ trả về Virtual MAC khác nhau.
    * Các Client sẽ được chia sang nhiều Router.
- Hỗ trợ tối đa
    * 4 AVF trong một Group.

- Có nhiều thuật toán chia tải
    * Round Robin (mặc định)
    * Weighted
    * Host-dependent

- UDP Port
    * 3222

- Multicast IPv4
    * 224.0.0.102

- Hello Timer
    * mặc định 3 giây

- Hold Timer
    * mặc định 10 giây

- Priority
    * mặc định 100

- Có hỗ trợ Preempt.
- Virtual MAC
    * 0007.B4xx.xxxx

- Authentication
    * Plain Text
    * MD5

- Interface Tracking
    * Có hỗ trợ.

- Ưu điểm
    * Dự phòng Gateway.
    * Load Balancing trong cùng VLAN.
    * Tận dụng toàn bộ Router.

- Nhược điểm
    * Chỉ Cisco.
    * Cấu hình phức tạp hơn HSRP.

- HSRP yêu cầu các router trong cùng một nhóm HSRP phải nằm trong cùng một mạng Layer 2 (cùng broadcast domain) để trao đổi gói Hello.

- Điều này có nghĩa:
    - Hai router không cần kết nối trực tiếp với nhau bằng cáp.
    - Chúng có thể đi qua một hoặc nhiều switch Layer 2.
    - Chỉ cần chúng vẫn thuộc cùng VLAN (cùng broadcast domain).

- Ví dụ:
    - Router A ↔ Switch ↔ Switch ↔ Router B
    - Cả hai interface đều thuộc VLAN 10.
    - Hai router vẫn có thể trao đổi gói Hello và hoạt động HSRP bình thường.

- Lưu ý:
    - HSRP sử dụng địa chỉ multicast để gửi gói Hello.
    - HSRPv1: 224.0.0.2
    - HSRPv2: 224.0.0.102
    - Các gói Hello chỉ tồn tại trong cùng broadcast domain.
    - Router Layer 3 sẽ không chuyển tiếp các gói multicast này sang mạng khác.
    - Vì vậy, các router trong cùng nhóm HSRP phải thuộc cùng một VLAN hoặc cùng một mạng Layer 2.

## 2.3. VRRP (Chuẩn mở)
- VRRP - Virtual Router Redundancy Protocol
- Chuẩn mở.
- Hoạt động trên nhiều hãng
    * Cisco
    * Juniper
    * Huawei
    * Mikrotik
    * Arista
    * ...

- Chỉ có
    * Master
    * Backup

- Client chỉ biết Virtual IP.
- Master sẽ xử lý toàn bộ Traffic.
- Backup chờ thay thế.
- Chỉ Master trả lời ARP.
- Nếu Master chết thì Backup sẽ trở thành Master.
- Election
    * Priority lớn hơn sẽ thắng.
    * Priority mặc định = 100.
    * Priority = 255 thường dành cho Router sở hữu IP thật.
- VRRP mặc định có Preempt.
- Hello Timer (Advertisement)
    * mặc định 1 giây
- Master Down Interval
    * khoảng 3 giây
- IP Protocol
    * 112

- Không dùng TCP hoặc UDP.
- Multicast IPv4
    * 224.0.0.18

- Virtual MAC
    * 0000.5E00.01xx
    * xx là VRID.

- Authentication
    * VRRPv2 có.
    * VRRPv3 loại bỏ Authentication.

- Interface Tracking
    * Có hỗ trợ.

- Hỗ trợ IPv6
    * VRRPv3

- Ưu điểm
    * Chuẩn mở.
    * Tương thích nhiều hãng.
- Nhược điểm
    * Không Load Balancing trong cùng VLAN.