# 1. Bridge ID field
- spanning-tree vlan 10 root primary
- spanning-tree vlan 10 priority 4096
- interface gigabitEthernet 0/1
    * spanning-tree vlan 10 port-priority 64
    * spanning-tree vlan 10 cost 10
- spanning-tree vlan 20 root secondary

# 2. ToolKit STP
- spanning-tree portfast default // toàn cục -> áp dụng toàn bộ giao diện
- spanning-tree portfast bpduguard default // toàn cục
- interface g0/1
    * spanning-tree portfast // cục bộ
    * spanning-tree portfast 
    * spanning-tree guard root
    * spanning-tree guard loop
- spanning-tree uplinkfast // toàn cục
- spanning-tree backbonefast // toàn cục
- cả 2 là uplinkfast và backbonefast hiện nay ít dụng do đã có PVST+

# 3.BPDU ethernet Frame
- chỉ nên cấu hình nếu thật sự rành -> còn không để mặc định
- spanning-tree vlan 10 hello-time 2
- spanning-tree vlan 10 forward-time 15
- spanning-tree vlan 10 max-age 20

# 4. Version
- spanning-tree mode pvst
- spanning-tree mode rapind-pvst
- spanning-tree mode mst

# 5. Những thứ khác
- sw(config)# errdisable recovery interval <giay> 60 -> Sau 60 giây → switch tự bật lại port bị errdisable
- sw(config)# errdisable recovery cause bpduguard
    * Chỉ định nguyên nhân được auto recovery
    * Ở đây: BPDU Guard gây shutdown → sẽ tự recover



# 5. show
- show spanning-tree vlan 10
- show spanning-tree interface g0/1 detail
- show spanning-tree summary
- show errdisable recovery
- show interfaces status err-disabled
