# Telnet – TCP port 23

- Telnet sử dụng TCP port 23  
- Data (dữ liệu) được truyền dạng plain text → có thể bị capture bằng Wireshark  
- Telnet = giao thức truy cập từ xa không mã hóa (insecure)

## 1. Create User for Telnet Login

- R1(config)# username annk secret ccna  

- R1(config)# username annk privilege 15 secret ccna  

+ Normal user = user thường  
+ privilege 15 = quyền admin cao nhất  

- Không cần hostname, domain name, RSA key  
+ Các bước đó chỉ dùng cho SSH

## 2. Configure Telnet (VTY lines)

- R1(config)# line vty 0 15  
- R1(config-line)# login local  
- R1(config-line)# transport input telnet  

+ VTY = Virtual Terminal lines (cổng truy cập từ xa)  
+ login local = dùng user database local  
+ chỉ cho phép Telnet access  

## Notes

- Telnet không mã hóa dữ liệu → rất dễ bị sniff password  
- SSH được ưu tiên dùng để quản trị từ xa an toàn hơn  