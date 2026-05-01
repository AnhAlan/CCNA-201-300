# 1. xem thông tin vlan
- show vtp status
- show vlan brief

# 2. Cấu hình VTP domain
- vtp domain <name>

# 3. Cấu hình VTP password
- vtp password 123456

# 4. Cấu hình VTP mode
- R1(confif)# 
    * vtp mode server
    * vtp mode client
    * vtp mode transparent

# 5. Cấu hình VTP version
vtp version 1
vtp version 2
vtp version 3

# 6. VTP pruning (tối ưu traffic VLAN)
- vtp pruning -> chỉ dùng trên server mode

# 7. Reset 
- nếu có switch mới cắm vào mô hình mạng -> ta nên reset revision về 0 bằng cách
- chuyển chế độ giữa 3 chế độ và đặt chế độ mong muốn ở cuối
- ví dụ switch muốn nó ở chế độ client
    * vtp mode server
    * vtp mode client
- an toàn khi đưa vào mô hình mạng
- hoặc đổi tên domain
    * vtp domain <new name>