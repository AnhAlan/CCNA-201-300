# 1. DTP - Dynamic trunk protocol
- DTP chỉ tác dụng giữa các switch của **cisco** -> giao thức độc quyền 
- DTP: tự động thương lượng trạng thái switchport giữa 2 switch -> giúp 2 switch cùng chế độ
    * 
- các chế độ DTP:
    * access: luôn là access -> không bao giờ lên trunk, không chạy DTP negotiation
    * trunk: luôn là trunk -> không thương lượng DTP
    * dynamic desirable: chủ động đề nghị tạo trunk
    * dynamic auto: chờ bên kia đề nghị -> thụ động
- các trường hợp có thể xảy ra giữa 2 thiết bị thương lượng:
    * trunk + trunk/dynamic auto/dynamic = trunk
    * desirable + auto = trunk (do bên desirable chủ động)
    * auto + auto = access
    * access + mọi chế độ = access
    * access + trunk = mistmach hoặc giao diện hoạt động không đúng (%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on FastEthernet0/1 (10), with Switch FastEthernet0/1 (1).)
# 2. Tính bảo mật
- DTP chỉ quan tâm thương lượng 2 switch nên có 1 thiết bị bên ngoài giả switch sẽ ảnh hưởng đến tính an toàn 
- vì vậy nên tắt DTP
- mặc định các switch đều bật DTP
    * đối với switch cũ: mặc định trên cổng ethernet -> desirable
    * đối với switch mới: mặc định trên ethernet -> auto
- tắt DTP: vào giao diện và
    * int g0/1
    * switchport nonegotiate
    * hoặc để giao diện access là DTP tự tắt
- lưu ý:
    * chỉ tắt được DTP khi port đang chế độ trunk
    * Chỉ trunk tĩnh mới tắt được DTP, dynamic thì không
    * Chế độ access tự động tắt DTP
# 3. Cấu hình
- int e0/0
    * switchport mode dynamic auto // chế độ auto
    * switchport mode dynamic desirable // chế độ desirable

# 4. Xem cấu hình
- xem chế độ DTP ở
    * show interface trunk

# 5. Đối với switch hổ trợ cả 802.1Q và ISL
## 5.1. Encapsulation
- có 2 loại
    * ISL (inter-switch link-cisco proprietary)
    * 802.1Q (dot1q) chuẩn IEEE
- swich cisco đời cũ có hổ trợ cả 2 nhưng sau này các switch mới đã loại bỏ ISL và chỉ hổ trợ 802.1q 
## 5.2. Khi không chỉ định encapsulation (đối với 2 switch hổ trợ cả 2)
- Nếu cấu hình trunk mà không chỉ định rõ encapsulation:
- DTP sẽ tự động:
    * thương lượng encapsulation chung giữa 2 switch
    * chọn loại mà cả 2 cùng hỗ trợ
- Kết quả: Kết nối trunk sẽ dùng encapsulation được thống nhất
## 5.3. Quy tắc chọn encapsulation
- Nếu cả 2 switch đều hỗ trợ: ISL sẽ được chọn (ưu tiên cao hơn)
- Nếu 1 bên không hỗ trợ ISL: dùng 802.1Q