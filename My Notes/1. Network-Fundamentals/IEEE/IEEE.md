# IEEE 802 Standards Overview

## Layer 2 / Switching (IEEE 802.1)
- `802.1D` → STP (Spanning Tree Protocol, chống loop)
- `802.1Q` → VLAN tagging (gắn VLAN ID vào frame Ethernet)
- `802.1w` → RSTP (Rapid STP, hội tụ nhanh hơn STP)
- `802.1s` → MSTP (Multiple STP instances, nhiều VLAN mapping)
- `802.1X` → Network access control (Port-based authentication, dùng trong WiFi/Enterprise)
- `802.1AB` → LLDP (Link Layer Discovery Protocol) — giao thức khám phá thiết bị lớp 2, tương tự CDP nhưng là chuẩn mở (không riêng của Cisco)

## Ethernet (IEEE 802.3)
- `802.3` → Ethernet LAN có dây
- `802.3u` → Fast Ethernet (100 Mbps)
- `802.3ab` → Gigabit Ethernet over copper (1000Base-T)
- `802.3z` → Gigabit Ethernet over fiber (1000Base-X)
- `802.3ae` → 10 Gigabit Ethernet (10G)
- `802.3ba` → 40G / 100G Ethernet
- `802.3af` → PoE (Power over Ethernet) — cấp nguồn tối đa ~15.4W
- `802.3at` → PoE+ — cấp nguồn tối đa ~30W
- `802.3bt` → PoE++/UPoE — cấp nguồn tối đa ~60–100W

## Wireless (IEEE 802.11)
- `802.11a` → 5 GHz, tốc độ cao (cũ)
- `802.11b` → 2.4 GHz, tốc độ thấp
- `802.11g` → 2.4 GHz, phổ biến trước đây
- `802.11n` → WiFi 4 (2.4/5 GHz, MIMO)
- `802.11ac` → WiFi 5 (5 GHz, tốc độ cao)
- `802.11ax` → WiFi 6/6E (hiệu năng + nhiều thiết bị)
- `802.11be` → WiFi 7 (rất mới, cực nhanh)

## Security / Access Control (IEEE 802.1 + network security)
- `802.1X` → Authentication (RADIUS, Enterprise WiFi)
- `WPA/WPA2/WPA3` → chuẩn bảo mật WiFi (không thuộc 802.1 nhưng hay đi kèm 802.11)

## QoS (Quality of Service)
- `802.1p` → Priority tagging (ưu tiên traffic trong LAN)

## Tổng thể IEEE quan trọng
- `802.1` → Switching / VLAN / STP / Security
- `802.3` → Ethernet có dây
- `802.11` → Wireless (WiFi)
- `802.1p` → QoS trong Layer 2

---

## Mức độ cần thiết

### Đối với CCNA (200-301)
Đủ dùng, thậm chí hơi rộng hơn phạm vi thi một chút. CCNA thực chất tập trung sâu vào:
- `802.1Q` (VLAN tagging) — rất quan trọng, hay hỏi
- `802.1D` / `802.1w` (STP/RSTP) — quan trọng, có thể hỏi cấu hình
- `802.3` cơ bản (Ethernet, tốc độ, cáp)
- `802.11` các chuẩn WiFi cơ bản (a/b/g/n/ac/ax) — chủ yếu để nhận biết, không đi sâu
- `802.1X` — biết khái niệm là đủ, ít khi hỏi sâu

Các chuẩn sau **thường không nằm trọng tâm CCNA**, mà chủ yếu xuất hiện ở CCNP (switching) hoặc trong thực tế doanh nghiệp lớn:
- `802.1s` (MSTP)
- `802.3ae` / `802.3ba` (10G/40G/100G)

### Đối với thực tế công việc
Danh sách trên đã cover gần hết các chuẩn thường gặp. Hai nhóm nên biết thêm để "đủ dùng" hơn trong thực tế:
- **PoE** (`802.3af` / `802.3at` / `802.3bt`) — rất hay gặp khi cấp nguồn cho AP, camera IP, điện thoại IP
- **LLDP** (`802.1AB`) — giao thức khám phá thiết bị lớp 2, hay dùng thay/kèm CDP (Cisco)

**Kết luận**: Để thi CCNA thì thừa đủ; để làm việc thực tế thì thêm PoE và LLDP là tương đối trọn vẹn.
