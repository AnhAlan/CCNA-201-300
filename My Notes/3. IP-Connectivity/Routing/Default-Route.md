- Trong routing, default route là “đường đi dự phòng cuối cùng” khi router không biết gửi packet đi đâu.
- router 1 là router ra internet
    * R1(config)# ip route 0.0.0.0 0.0.0.0 <ip ra intetnet>
- cách lan truyền default route cho các rotuer khác biết
    * đối với RIP và OSPF
        * default-information originate
    * đối với EIGRP
        * cách 1. ip default-network x.x.x.x
        * x.x.x.x là subnet-mask mạng là rouer 1 nối với mạng ISP (hay ra internet)
        * cách 2: 
            * ip route 0.0.0.0 0.0.0.0 <next-hop>
            * router eigrp 1
                * redistribute static

- tức ip đích không match với route nào sẽ gửi về next-hop của 0.0.0.0/0