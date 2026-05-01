# 1. VTP (vlan trunk protocol)
- tự động đồng bộ cấu hình vlan giữa các switch trong cùng hệ thống
- giúp tiếp kiệm thời gian cấu hình toàn bộ switch 

# 2. Cách hoạt động
- vtp hoạt động thông qua 
    * các đường trunk (ISL hoặc 802.1Q)
    * giữa quảng bá (advertised) chứa thông tin vlan: ID, name, status,..

# 3. Các chế độ vtp
## 3.1. server
- tạo / sữa / xóa vlan -> gửi update cho các switch khác
- nếu vtp server nhận vtp quảng bá (advertised) cao hơn -> tự động cập nhật theo 
- Có thể có nhiều server trong domain
## 3.2. client
- chỉ nhận vlan từ switch server
## 3.3. transparent
- không tham gia đồng bộ vlan -> nhưng vẫn cho vlan di qua trunk (nếu vtp version 2 trở lên) -> hoạt động độc lập
- switch vẫn tạo vlan nhưng không propagate (tuyên truyền)

# 4. VTP domain và password
- vtp domain là tên nhóm switch dùng chung vtp -> phải giống nhau mới đồng bộ
- có thể đặt password để bảo vệ mạng khỏi cập nhật không mong muốn

# 5. vtp revision number
- mỗi lần server thay đời vlan -> số revision tăng lên
- các switch khác chỉ chấp nhận vlan mới nếu số revision cao hơn (càng nhiều vlan -> revision càng cao)
- nếu thay đổi tên VTP domain -> reset revision thành 0
- nếu chuyển đôi VTP mode sang transparent -> reset revision thành 0
- lưu ý:
    * nếu dùng 1 switch cũ có hệ thống trước đó với revision cao hơn (nhưng không có vlan dùng) -> có thể ảnh hưởng hoặc xóa sạch vlan trên hệ thống -> gọi là vtp bomb
    * nếu sử dụng switch khác cắm vào đảm bảo revision không lớn hơn các switch khác -> nhỏ hơn hoặc bằng

# 6. ba version VTP 
## 6.1. version 1
- cơ bản: chỉ hổ trợ dãy vlan 1 -> 1005
- không hổ trợ token ring
## 6.2. version 2
- hổ trợ token ring (lỗi thời)
- hổ trợ transparent mode
- vlan 1 -> 1005
- client: lưu database vlan nhưng không sữa được
## 6.3. version 3
- hổ trợ đầy đủ vlan (1006 -> 4094)
- hổ trợ priacte vlan (PVLAN)
- VTPv3 có thể hỗ trợ phân phối một số thông tin STP/MST trong một số hệ thống
- bảo mật cao hơn (mật khẩu)
- có thể chỉ định duy nhất primary server duy nhất được phép cập nhật vlan
