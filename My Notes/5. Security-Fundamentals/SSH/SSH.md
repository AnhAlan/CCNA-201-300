# SSH (Secure Shell) – TCP port 22

- SSH sử dụng TCP port 22  
- SSH = Secure Shell (giao thức truy cập từ xa có mã hóa)

## 1. Đặt HOSTNAME

- R1# → R1(config)#  
- R1(config)# hostname R1  

+ Hostname là tên thiết bị dùng trong network
+ Bắt buộc để tạo FQDN cho SSH

## 2. IP Domain Name (FQDN)

- R1(config)# ip domain name annk.com  

+ FQDN = Fully Qualified Domain Name  
+ FQDN = Hostname + Domain name → R1.annk.com  
+ Dùng để tạo RSA key cho SSH

## 3. Tạo RSA Key

- R1(config)# crypto key generate rsa  
- hoặc: crypto key generate rsa modulus 2048  

+ RSA = thuật toán mã hóa bất đối xứng dùng cho SSH  
+ 512 bits → yếu  
+ 1024 bits → trung bình  
+ 2048 bits → khuyến nghị (recommended)

## 4. Enable Secret

- R1(config)# enable secret ccna  

+ Enable secret = mật khẩu vào privileged EXEC mode  
+ Được hash an toàn hơn password thường

## 5. Tạo User

- R1(config)# username annk secret ccna  

- R1(config)# username annk privilege 15 secret ccna  

+ privilege 15 = quyền admin cao nhất  
+ secret = mật khẩu được mã hóa

## 6. SSH Version

- R1(config)# ip ssh version 2  

+ SSH v2 = phiên bản an toàn hơn  
+ Một số thiết bị hiển thị 1.99 (hỗ trợ v1 + v2)

## 7. VTY Lines (Remote Access)

- R1(config)# line vty 0 15  
- R1(config-line)# login local  
- R1(config-line)# transport input ssh  

+ VTY = Virtual Terminal lines (cổng remote login)
+ login local = dùng user database nội bộ
+ chỉ cho phép SSH (không Telnet)

## 8. (Optional) ACL giới hạn SSH

- R1(config)# access-list 10 permit 192.168.1.100  
- R1(config)# line vty 0 15  
- R1(config-line)# access-class 10 in  

+ Chỉ PC 192.168.1.100 được SSH vào thiết bị  
+ access-class dùng để lọc truy cập VTY

## 9. SSH từ PC

- ssh -l username ip-address  
- ssh username@ip-address  

+ 2 cách đăng nhập SSH từ terminal

---

# SSH Full Configuration

- hostname R1  
- ip domain-name annk.com  

- crypto key generate rsa modulus 2048  

- username admin privilege 15 secret 123456  

- ip ssh version 2  
- ip ssh time-out 90  
+ Thời gian chờ đăng nhập SSH (90 giây)

- ip ssh authentication-retries 2  
+ Số lần nhập sai password tối đa

- access-list 10 permit 192.168.1.100  

---

- line vty 0 15  
- banner login # Welcome to R1. Unauthorized access prohibited! #  
+ Banner hiển thị khi SSH login

- session-limit 2  
+ Giới hạn 2 phiên SSH cùng lúc

- logging synchronous  
+ Không làm gián đoạn khi nhập lệnh

- login local  
- transport input ssh  

- exec-timeout 5 0  
+ Tự logout sau 5 phút không hoạt động

- access-class 10 in  
+ Chỉ cho phép IP trong ACL truy cập SSH