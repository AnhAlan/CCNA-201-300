
# 1. HSRP Configuration
## 1.1. Cấu hình cơ bản

```cisco
interface g0/0

 ip address 192.168.1.2 255.255.255.0

 standby 1 ip 192.168.1.254
```

---

## 1.2. Đặt Priority

```cisco
interface g0/0

 standby 1 priority 120
```

- Mặc định Priority = 100
- Priority cao hơn sẽ trở thành Active Router.

---

## 1.3. Bật Preempt

```cisco
interface g0/0

 standby 1 preempt
```

- Cho phép Router Priority cao giành lại vai trò Active khi hoạt động trở lại.

---

## 1.4. Đổi Hello/Hold Timer

```cisco
interface g0/0

 standby 1 timers 1 3
```

- Hello = 1s
- Hold = 3s

---

## 1.5. Authentication

### Plain Text

```cisco
interface g0/0

 standby 1 authentication Cisco123
```

### MD5

```cisco
key chain HSRP

 key 1

  key-string Cisco123

interface g0/0

 standby 1 authentication md5 key-chain HSRP
```

---

## 1.6. Interface Tracking

```cisco
interface g0/0

 standby 1 track g0/1 20
```

- Nếu g0/1 Down
- Priority giảm 20.

---

## 1.7. HSRP Version

### Version 1

```cisco
interface g0/0

 standby version 1
```

### Version 2

```cisco
interface g0/0

 standby version 2
```

---

## 1.8. Hiển thị trạng thái

```cisco
show standby
```

```cisco
show standby brief
```

```cisco
show standby all
```

---

## 1.9. Debug

```cisco
debug standby
```

---

## 1.10. Xóa cấu hình

```cisco
no standby 1 ip
```

---

# 2. VRRP Configuration

## 2.1. Cấu hình cơ bản

```cisco
interface g0/0

 ip address 192.168.1.2 255.255.255.0

 vrrp 1 ip 192.168.1.254
```

---

## 2.2. Priority

```cisco
interface g0/0

 vrrp 1 priority 120
```

---

## 2.3. Preempt

```cisco
interface g0/0

 vrrp 1 preempt
```

---

## 2.4. Timer

```cisco
interface g0/0

 vrrp 1 timers advertise 1
```

Advertisement Interval = 1 giây.

---

## 2.5. Authentication (VRRPv2)

```cisco
interface g0/0

 vrrp 1 authentication Cisco123
```

---

## 2.6. Interface Tracking

```cisco
interface g0/0

 vrrp 1 track 1 decrement 20
```

hoặc

```cisco
track 1 interface g0/1 line-protocol

interface g0/0

 vrrp 1 track 1 decrement 20
```

---

## 2.7. Hiển thị trạng thái

```cisco
show vrrp
```

```cisco
show vrrp brief
```

---

## 2.8. Debug

```cisco
debug vrrp events
```

```cisco
debug vrrp packets
```

---

## 2.9. Xóa cấu hình

```cisco
no vrrp 1 ip
```

---

# 3. GLBP Configuration

## 3.1. Cấu hình cơ bản

```cisco
interface g0/0

 ip address 192.168.1.2 255.255.255.0

 glbp 1 ip 192.168.1.254
```

---

## 3.2. Priority

```cisco
interface g0/0

 glbp 1 priority 120
```

---

## 3.3. Preempt

```cisco
interface g0/0

 glbp 1 preempt
```

---

## 3.4. Timer

```cisco
interface g0/0

 glbp 1 timers 1 3
```

Hello = 1

Hold = 3

---

## 3.5. Authentication

### Plain Text

```cisco
interface g0/0

 glbp 1 authentication Cisco123
```

### MD5

```cisco
key chain GLBP

 key 1

  key-string Cisco123

interface g0/0

 glbp 1 authentication md5 key-chain GLBP
```

---

## 3.6. Interface Tracking

```cisco
interface g0/0

 glbp 1 weighting track 1 decrement 20
```

hoặc

```cisco
track 1 interface g0/1 line-protocol

interface g0/0

 glbp 1 weighting track 1 decrement 20
```

---

## 3.7. Weighting

```cisco
interface g0/0

 glbp 1 weighting 120 lower 95 upper 110
```

- Weight mặc định = 100
- Lower: dưới giá trị này Router ngừng Forward.
- Upper: trên giá trị này Router Forward trở lại.

---

## 3.8. Load Balancing

### Round Robin (mặc định)

```cisco
interface g0/0

 glbp 1 load-balancing round-robin
```

---

### Weighted

```cisco
interface g0/0

 glbp 1 load-balancing weighted
```

---

### Host Dependent

```cisco
interface g0/0

 glbp 1 load-balancing host-dependent
```

---

## 3.9. Hiển thị trạng thái

```cisco
show glbp
```

```cisco
show glbp brief
```

---

## 3.10. Debug

```cisco
debug glbp events
```

```cisco
debug glbp packets
```

---

## 3.11. Xóa cấu hình

```cisco
no glbp 1 ip
```

---

# 4. Kiểm tra FHRP

## Kiểm tra Interface

```cisco
show ip interface brief
```

---

## Kiểm tra ARP

```cisco
show arp
```

---

## Kiểm tra MAC

```cisco
show mac address-table
```

---

## Kiểm tra Route

```cisco
show ip route
```

---

## Kiểm tra Track

```cisco
show track
```

---

## Ping

```cisco
ping <Virtual-IP>
```

---

## Traceroute

```cisco
traceroute <Destination-IP>
```

---

# 5. Lưu cấu hình

```cisco
copy running-config startup-config
```

hoặc

```cisco
write memory
```

---

# 6. Khôi phục cấu hình

```cisco
reload
```

---

# 7. Cheat Sheet

## HSRP

```cisco
standby <group> ip <virtual-ip>

standby <group> priority <priority>

standby <group> preempt

standby <group> timers <hello> <hold>

standby <group> authentication <password>

standby version 2

show standby brief
```

---

## VRRP

```cisco
vrrp <group> ip <virtual-ip>

vrrp <group> priority <priority>

vrrp <group> preempt

vrrp <group> timers advertise <sec>

show vrrp brief
```

---

## GLBP

```cisco
glbp <group> ip <virtual-ip>

glbp <group> priority <priority>

glbp <group> preempt

glbp <group> weighting 120 lower 95 upper 110

glbp <group> load-balancing round-robin

show glbp brief
```