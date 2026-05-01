# 1. Native Vlan
- Native VLAN = VLAN untagged trên trunk
- Là VLAN không gắn thẻ (untagged) trên trunk link
- Native VLAN vẫn tồn tại trong VLAN database của switch
- Khi switch/router nhận frame không tag trên trunk → sẽ gán vào native VLAN
- Default: VLAN 1 (ít bảo mật)
- Nếu giao diện không phải trunk:
    * Switch access port → vẫn thuộc VLAN (untagged trong VLAN đó)
    * Router L3 interface → không tham gia VLAN (không có tagging, không có native VLAN)

# 2. Có 2 phương pháp cấu hình vlan native
## 2.1. Cấu hình trên giao diện sub - interface
- R1(config)# int g0/1.10
- R1(config- if)# encapsulation dot1q 10 native
- không gắn thẻ -> thuộc native vlan
- Sub-interface .10 chỉ là tên logic, còn dot1q 10 mới là vlan-id 10 thật   

## 2.2. Cấu hình trực tiếp trên interface (không tham gia vlan)
- gắn ip lên giao diện vật lý thì giao diện đó là layer 3 và không có trunk
- tức không tham gia vlan và không có **native vlan** luôn
- không trunk - không Vlan tagging - không native vlan

# 3. Vlan mismatch
- lỗi này xảy ra khi 2 đầu trunk có native vlan khác nhau 
- ví dụ:
    * Switch A: native vlan 10
    * Switch B: native vlan 20
- khi A gủi -> B nhận và hiểu native vlan thuộc 20
- sai vlan -> sai broadcast domain -> dẫn đến  
    * mất kết nối
    * chạy sai (khó debug)
    * lỗi bảo mật
    * thường các Switch sẽ liên tục thông báo lỗi Mistmatch
    * %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (10), with SwitchB GigabitEthernet0/1 (20)