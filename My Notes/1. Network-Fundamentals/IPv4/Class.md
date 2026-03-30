- IPv4 has 32 bits

- Class A: 1 - 127
    1.0.0.0 -> 126.0.0.0
    each network has (2^24 - 2) host / mask

* 127.0.0.0 -> use for loopback (read loopback.txt)

- class B: 128 - 191
    128.0.0.0 -> 191.255.0.0
    2 first bits is 10xxxxxx is belong to B 
    2^14 = 16384 network

- Class C: 192 - 223
    start bits: 110xxxxx
    192.0.0.0 -> 223.255.255.0
    2^21 = 209715 network

- Class D: 225 - 239
    use for multicast address -> allowed devices send packet to group are assign
    224.0.0.5 -> ospf
    225.0.0.6 -> all ospf DR and BDR router
    undivided -> because represent for group
    save bandwidth
    224.0.0.0 -> 239.255.255.255
    -> some sub network belong for some purpose

- Class E: 240 - 255
    240.0.0 -> 255.255.255.255
    For research and testing purposes.


- 3 private IP ranges
    * 10.0.0.0/8 (10.0.0.0 -> 10.255.255.255)
    * 172.16.0.0/12 (172.16.0.0 → 172.31.255.255) 
    * 192.168.0.0/16 (192.168.0.0 → 192.168.255.255)