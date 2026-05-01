This is a packet sent to all hosts in the same network (subnet).
Purpose: notification, device locator, ARP, etc.
Every host in the subnet receives and processes broadcast packets.

1. Limited Broadcast
    255.255.255.255

2. Subnet Broadcast
    Send to all hosts in a specific subnet
    Routeable if the router allows it
    How to determine: broadcast = network address OR (NOT subnet mask)
    For example: 192.168.1.0/26 → mask 255.255.255.192
    + Network: 192.168.1.0 → first host: 192.168.1.1
    + Last host: 192.168.1.62
    + Broadcast: 192.168.1.63
    + Next subnet 192.168.1.64/26 → broadcast = 192.168.1.127

3. Note
- nhiều broadcast không cần thiết sẽ làm chậm mạng -> giảm lưu lượng -> chia mạng nhỏ -> vlan - vlsm
