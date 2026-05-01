# 1. xác định giao diện inside và outside

* R1(config)# int g0/0
    * ip nat inside
* R1(config)# int g0/1
    * ip nat outside
- inside → mạng LAN (private IP)
- outside → mạng WAN/Internet (public IP)

# 2. (option hay dùng với NAT) sử dụng ACL permit các dãy ip mong muốn ra internet

* R1(config)# access-list 1 permit 172.16.0.0 0.0.0.255
    + subnet 172.16.0.0/24 mới được phép ra permit

# 3. cấu hình nat pool dãy ip public

* R1(config)# ip nat pool POOL1 100.0.0.1 100.0.0.2 netmask 255.255.255.0

    +chỉ có 2 ip public được chọn
    +nếu có máy thứ 3 sử dụng nat -> không được sủ dụng

# 4. áp dụng nat pool và ACL
* R1(config)# ip nat inside soure list 1 pool POOL1

    + NAT từ trong → ngoài
    + Chỉ IP match ACL
    + Dùng IP trong pool

# 5. sử dụng PAT để tối ưu ip public

* R1(config)# ip nat inside soure list 1 interface gigabitethernet 0/1 overload
    + các host sẽ sử dụng ip của int g0/1 (đảm bảo interface outside) làm ip public và phân biệt bằng port-number
    + router dựa vào bảng nat để xác định đâu là gói tin của host nào


# 6. các configura khác

- R1(config)# ip nat pool pool-name start-ip end-ip prefix-length <prefix-length>
- R1(config)# ip nat pool pool-name start-ip end-ip netmask <subnet-mask>
    + 2 cấu hình trên đều xác định subnet của ip public, chỉ khác cách khai báo

- R1(config)# ip nat inside source list <access-list> pool <pool-name>
    + ACL các ip hợp lệ để được NAT

- R1(config)# ip nat inside source list <access-list> pool <pool-name> overload
    + ACL các ip hợp lệ để được NAT ip public và port-number

- R1(config)# ip nat inside source list access-list interface interface overload
    + ACL các ip hợp lệ để được PAT (lấy ip của router outside làm ip public với port-number)

- R1# show ip nat translation
    + Bảng NAT hiển thị: Inside local, inside global, outside local, outside global, port (PAT)
    + inside local: IP private thật của host trong LAN
    + inside global: IP public sau khi NAT (là ip public hoặc ip interface router outside)
    + outside local: IP thật của server ngoài Internet
    + outside global: IP của server ngoài nhìn từ phía inside (thường trùng với outside local trừ khi NAT ở ngoài - hiếm)

- R1# show ip nat  statistics
    + xem bảng thống kê NAT: Router tra bảng thống kê để biết gói tin của Router hay

- R1(config)#no ip nat ?
    + Dùng để xóa cấu hình NAT (config), không phải xóa NAT table
    + Xóa NAT dùng pool: no ip nat inside source list 1 pool POOL1
    + Xóa NAT dùng interface (PAT): no ip nat inside source list 1 interface g0/1 overload
    + ...

- R1(config)# clear ip nat translation *
    + '*' : option toàn bộ session
    + Xóa toàn bộ NAT session hiện tại
    + Không xóa cấu hình NAT
First line with two spaces after.  
And the next line.




