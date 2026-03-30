ICMP (Internet Control Message Protocol)**
- Used to test connectivity between two devices
- Measures Round-Trip Time (RTT): PC1 → PC3 → PC1

1. ICMP Messages Used in Ping:

- ICMP Echo Request
- ICMP Echo Reply

2. Default Behavior
* Cisco devices send 5 ICMP Echo Requests by default
* Default packet size is 100 bytes (Cisco)

3. Ping Output Symbols (Cisco):
 `!` → Successful reply
 `.` → No reply (timeout / failure)

4. Ping Output Example (Windows)

 `Reply from 192.168.1.1: bytes=32 time<1ms TTL=128`

5. Key Notes:**
- Ping operates at Layer 3 (Network Layer)
- The first ping may fail due to ARP resolution
  * Initially, the device only knows the destination IP
  * It must use ARP to learn the destination MAC address
  * After ARP is completed, subsequent pings succeed
- all devies on Ethernet need IP + MAC
