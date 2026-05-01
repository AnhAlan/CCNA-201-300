# 1. ROAS - Router on a sitck
- 1 router có 1 port đại diện 1 ip -> nhiều vlan ta cần nhiều port -> hạn chế
- ta sẽ làm mỗi port có thể chứa nhiều vlan -> chia interface thành sub-interface
- mỗi sub-interface đại diện 1 vlan
- dùng trunk 802.1Q để mang nhiều vlan
# 2. Cách hoạt động
- switch gửi trunk lên router
- router nhận frame có tag vlan
- router sẽ
    * tách vlan theo sub-interface
    * routing giữa các vlan
- router sẽ gửi lại frame cho switch
# 3. Cấu hình
- R1(config)# int g0/1.10
- R1(config - subif)# encapsulation dot1q 10 
- R1(config - subif)# ip add <ip> <subnet-mask>
- R1(config - subif)# no shutdown // không cần thiết do sub-interfaec luôn up/up
- lưu ý:
    * g0/1.10 : 10 ở đây là id giao diện không phải dành cho vlan 10
    * thường id đi cùng vlan nên sẽ cấu hình vlan-id trùng id sub-interface
    * dot1q là chuẩn IEEE trunk
    * thường các host sẽ để gateway là ip sub-interface
    * có trường hợp host để ip gateway là SVis của switch (switch layer 3) và switch đó sẽ routing các node mạng khác