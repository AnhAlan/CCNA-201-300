*Mar 28 06:15:52.819: %CDP-4-DUPLEX_MISMATCH: duplex mismatch discovered on FastEthernet0/0 (not half duplex), with R1 FastEthernet0/0 (half duplex).*

- Lỗi CDP báo mismatch về duplex giữa hai thiết bị trên cổng FastEthernet0/0
- Một bên đang chạy full duplex (không phải half duplex)
- Bên còn lại đang chạy half duplex

---

## Loại lỗi
- Lỗi không đồng bộ duplex (duplex mismatch)
- Gây giảm hiệu suất mạng và tăng collision

---

## Nguyên nhân
- Một thiết bị cấu hình manual full duplex
- Thiết bị còn lại để half duplex hoặc auto nhưng thương lượng sai
- Không đồng nhất cấu hình giữa 2 đầu link

---

## Hậu quả
- Tốc độ truyền giảm
- Tăng frame error / collision
- Mất ổn định kết nối

---

## Cách khắc phục
- Cấu hình hai đầu phải cùng chế độ duplex

- Khuyến nghị:
    - Cả hai cùng auto
    - Hoặc cả hai cùng full duplex

- Ví dụ cấu hình:
    Switch(config)# interface fa0/0
    Switch(config-if)# duplex full