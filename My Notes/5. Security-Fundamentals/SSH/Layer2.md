# Switch Layer 2 – Truy cập từ xa (SSH / Telnet)

- Switch Layer 2 không có địa chỉ IP vật lý để truy cập từ xa  
- Để dùng SSH/Telnet, cần tạo SVI (Switch Virtual Interface)  

## 1. Tạo SVI (IP quản trị)

- Switch(config)#int vlan 1  
- Switch(config-if)#ip add 192.168.1.5 255.255.255.0  
- Switch(config-if)#no shut  

## 2. Default Gateway

- Switch(config)#ip default-gateway 192.168.1.1 (ip router)  
- Cho phép PC ở mạng khác truy cập switch qua SSH/Telnet  

## 3. Tạo User đăng nhập SSH/Telnet

- User thường  
- Switch(config)# username annk secret ccna  

- User admin  
- Switch(config)# username annk privilege 15 secret ccna  

- Chỉ dùng SSH cần thêm hostname, domain name và RSA key (xem SSH.txt)  
- Telnet không cần RSA key  

## 4. Cấu hình line VTY

- line 0 15  
- login local  
- transport input ssh telnet (hoặc cả hai nếu cần)  

## Ghi chú

- Telnet: truyền dữ liệu dạng plain text → không an toàn  
- SSH: đã mã hóa → nên sử dụng  
- VLAN dùng cho SVI phải active và kết nối được với router để truy cập liên mạng  