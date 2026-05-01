# 1. SVIs (switch virtual interface)
- giao diện ảo gắn ip cho multilayer switch
- gắn ip để làm default gateway cho các pc trong cùng vlan
- cho phéo routing nội bộ giữa các vlan trên chính switch đó
# 2. Configute
## 2.1. Đảm bảo Multilayer switch có khả năng định tuyến
- mặc định switch layer 3 tắt routting -> phải bật
- R1(config)# ip routing
## 2.2. Có thể cấu hình ip lên giao diện thật
- đối với switch layer 3 có các tính năng của switch layer 2 và router
- ta có thể cấu hình mỗi cổng (port) là 1 giao diện
- mặc định port trên switch layer 3 là layer 2 nên ta phải chuyển port sang layer 3
- R1(config)# int g0/1
- R1(config - if)# no switchport // switchport là layer 2 
- R1(config - if)# ip add <ip> // do port lên layer 3 nên ta có thể gắn ip
- nhược điểm:
    * mỗi port thuộc 1 mạng duy nhất
    * không đủ rộng cho nhiều vlan
## 2.3. cấu hình SVIs
- vào giao diện mỗi vlan để đặt ip
- R1(config)# interface vlan 10
- R1(config - if)# ip add <ip>
- R1(config - if)# no shutdown
- tạo SVI cho vlan 10 và gắn ip kích hoạt interface
# 3. Các điều kiện để giao diện SVIs lên up/up
## 3.1. Vlan phải tồn tai trên switch
- phải tạo vlan bằng lệnh hoặc cổng layer 2 được cấu hình vlan 
- R1(confif)# vlan <vlan-id> // tạo vlan
- R1(config)# int g0/1
- R1(config - if)# switchport mode access
- R1(config - ìf)# switch access vlan 10 // tự tạo vlan 10 nếu chưa có vlan 10

## 3.2. Cổng phải acces vlan hoặc trunk vlan
- int g0/1
- switchport mode access 
- switchport access vlan <vlan-id>
- hoặc
- switchport trunk encapsulation dot1q
- switchport mode trunk
- switchport trunk allowed vlan <vlan-id>
## 3.3. Giao diện phải được "no shutdown"
- int vlan 10
- no shutdown
## 3.4. Vlan không "shutdown"
- shutdown vlan 10 -> không nên

# 4. Lưu ý
- Mode trunk không áp dụng cho SVIs vì SVis là giao diện ảo
- mode access cũng không áp dụng cho SVIs do SVIs ảo luôn
- trunk và access chỉ áp dụng trên giao diện vật lý
- ACL có thể áp dụng cả:
    * giao diện vật lý (layer 3)
    * SVIs
    * sub-interface
    * ...
- SVI có thể chuyển tiếp DHCP request từ client đến DHCP server bằng ip helper-address
     * int vlan 10
     * ip hepler-address <ip-dhcp-server> (không có khai báo subnet-mask)
