## Ethernet Frame Types

- **Unicast**
    - Một thiết bị gửi → một thiết bị nhận
    - Switch sẽ chuyển frame đến đúng port tương ứng

- **Broadcast**
    - Một thiết bị gửi → tất cả thiết bị trong mạng
    - Destination MAC: FF:FF:FF:FF:FF:FF

- **Multicast**
    - Một thiết bị gửi → một nhóm thiết bị

- **Unknown Unicast**
    - MAC đích không có trong bảng MAC của switch
    - Switch sẽ **flood** frame ra tất cả các port

---

## Switching Actions

- **Forward**
    - Unicast đã biết → gửi đúng port đích

- **Flood**
    - Unknown unicast → gửi ra tất cả port (trừ port nhận vào)
    - Broadcast → gửi ra tất cả port
    - Multicast → thường bị flood (nếu không có tối ưu như IGMP snooping)