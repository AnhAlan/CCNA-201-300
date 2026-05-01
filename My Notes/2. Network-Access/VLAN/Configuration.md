# 1. vlan 
- show vlan bri
- show vlan summary
- show mac address-table vlan 10
- show spanning-tree vlan 10
- show interfaces trunk
- show interfaces switchport
- vlan <vlan-id>
    * name <vlan-name>
    * exit
- interface f0/1
- switchport mode access
- switchport access vlan <vlan-id>

# 2. ROAS
- show ip interface brief
- show running-config
- show ip route
- show arp
- interface g0/0
- no shutdown
- interface g0/0.<sub-id>
- encapsulation dot1Q <vlan-id>
- ip address <ip> <mask>
- interface g0/0.<sub-id>
- encapsulation dot1Q <vlan-id> native (nếu native VLAN)

# 3. SVIs
- show ip interface brief
- show interfaces vlan <vlan-id>
- show running-config interface vlan <vlan-id>
- show ip route
- show arp
- interface vlan <vlan-id>
    * ip address <ip> <mask>
    * no shutdown
- ip routing (bật Layer 3 switch)
- interface f0/1
- switchport access vlan <vlan-id>
- int g0/1
    * encapsulation dot1q 10 
- int g0/1
    * encapsulation dot1q 10 native    



