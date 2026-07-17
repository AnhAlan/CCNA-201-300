# Neightbor discover protocol 
- là giao thức được dùng với IPv6
- thay thế ARP - IPv4
- IPCMv6 với Multicast để tìm các MAC khác

- gồm 2 tin nhắn được dùng
    * mời hàng xóm - Neighbor soliciation (NS) = ICMPv6 type 135
    * Neighbor Advertisement (NAS) -> ICMPv6 type 136

# R1 Ping R2
- khi R1 ping đến IPv6 R2
- R1 sẽ đóng gói tin đó vào khung Ethernet nhưng phải cần MAC R2
- R1 sẽ gửi NS (neighor Soliciation) cho R2
    * SRC IP: R1
    * DST IP: R2 Solicited-node Multicast address
    * SRC MAC: R1
    * DST MAC: Multicast Address based trên R2 Solicited-node address
- khi R2 nhận gói tin NS, gửi lại MAC của R2 cho R1
    * SRC IP: R2
    * DST IP: R1 
    * SRC MAC: R2
    * DST MAC: R1

# IPv6 Neighbor Table

- IPv6 **không sử dụng ARP** như IPv4 nên không có **ARP Table**.
- Thay vào đó, IPv6 sử dụng **Neighbor Discovery Protocol (NDP)** để duy trì **IPv6 Neighbor Table**.
- Neighbor Table lưu thông tin ánh xạ giữa:
  - Địa chỉ IPv6 (IPv6 Address)
  - Địa chỉ MAC (Link-layer Address)
  - Trạng thái láng giềng (Neighbor State)
  - Cổng kết nối (Interface)

- Kiểm tra IPv6 Neighbor Table

Lệnh kiểm tra trên thiết bị Cisco:
`R1# show ipv6 neighbor`

**Kết quả hiển thị:**
```text
IPv6 Address                             Age  Link-layer Addr  State  Interface
FE80::C802:9FF:FE7C:8                      0  ca02.097c.0008   REACH  Gi0/0
2001:DB8::78:9ABC                          0  ca02.097c.0008   REACH  Gi0/0
- ý nghĩa:
    - **IPv6 Address:** Địa chỉ IPv6 của neighbor. Một thiết bị thường có ít nhất 2 dòng: **Link-Local** (`FE80::`) để giao tiếp nội bộ LAN và **Global Unicast** (`2001::`,...) để định tuyến toàn cầu.
    - **Age:** Thời gian (phút) từ lần cuối xác nhận neighbor còn sống. Số `0` nghĩa là vừa xác nhận (<1 phút); dấu `-` là bản ghi cấu hình tĩnh (Static).
    - **Link-layer Addr:** Địa chỉ MAC vật lý của neighbor dùng để đóng gói Ethernet Frame. Dấu `-` nghĩa là chưa tìm thấy MAC.
    - **Interface:** Cổng mạng (ví dụ: `Gi0/0`) trên thiết bị hiện tại kết nối trực tiếp đến neighbor.


Neighbor State

State	Ý nghĩa

INCOMPLETE	Đang tìm kiếm thông tin MAC Address của neighbor

REACH	Neighbor có thể truy cập được và đã xác nhận

STALE	Thông tin neighbor tồn tại nhưng chưa được xác nhận gần đây

DELAY	Đang chờ xác nhận lại trạng thái neighbor

PROBE	Đang gửi Neighbor Solicitation để kiểm tra neighbor
```

# chức năng khác NDP
- giúp host tự động phát hiện bộ định tuyến trong mạng cục bộ (router)
- 2 message được gửi
    * router Solicitaion (RS) = ICMPv6 type 133
        * gửi đến multicast address FF02::2 (all router)
        * yêu cầu router trên cục bộ xác định chính nó (router)
        * sẽ gửi đến các interface được bật khi kết nối với máy chủ
    * Router advertisement (RA) = ICMPv6 type 134
        * gửi đến multicast address FF02::1 (all nodes)
        * thông báo sự hiện diện và cung cấp các thông tin khác về liên kết (link)
        * được gửi để đáp lại RS message
        * vẫn gửi RA mỗi định kỳ kể cả không nhận RS
    
# SLAAC (Stateless Address Auto-Configuration)

- **SLAAC** stands for **Stateless Address Auto-Configuration** (Tự động cấu hình địa chỉ không trạng thái).
- Đây là cơ chế cho phép thiết bị IPv6 **tự động tạo địa chỉ IPv6** mà không cần sự quản lý của DHCPv6 Server.

---

## 1. Cách hoạt động

Host sử dụng hai loại thông điệp thuộc giao thức **NDP (Neighbor Discovery Protocol)**:

- **RS (Router Solicitation)**:
  - Host gửi yêu cầu (Multicast đến `FF02::2`) để tìm kiếm Router trên mạng local ngay khi bật card mạng.

- **RA (Router Advertisement)**:
  - Router phản hồi định kỳ hoặc trả lời ngay khi nhận được RS (Multicast đến `FF02::1`).
  - Gói RA cung cấp các thông tin quan trọng:
    - **IPv6 Prefix** của local link (ví dụ: `2001:DB8:1:1::/64`)
    - **Prefix Length** (thường là `/64`)
    - **Default Gateway** (địa chỉ Link-Local `FE80::...` của Router)
    - Các cờ cấu hình (Flags) xác định có dùng DHCPv6 hay không

---

## 2. Cách Host tạo địa chỉ IPv6 trọn vẹn

Sau khi nhận được **Prefix 64 bits** từ RA, Host tự tạo ra **Interface ID (64 bits cuối)** theo 1 trong 2 cách:
1. **EUI-64:** Tạo từ địa chỉ MAC vật lý của card mạng (chèn thêm `FF:FE` vào giữa và đảo bit thứ 7).
2. **Random/Privacy Extension:** Tạo ngẫu nhiên 64 bits để bảo mật thông tin thiết bị.

> **Công thức:** `IPv6 Address` = `Prefix (/64 từ RA)` + `Interface ID (64 bits tự tạo)`

---

## 3. Ví dụ chi tiết

1. **Router gửi RA:** Cung cấp Prefix `2001:DB8:1:1::/64`.
2. **Host có MAC:** `00:11:22:33:44:55`.
3. **Host tạo Interface ID (EUI-64):** `0211:22FF:FE33:4455`.
4. $\rightarrow$ **Địa chỉ IPv6 hoàn chỉnh:** `2001:DB8:1:1:0211:22FF:FE33:4455/64`.
5. **Kiểm tra trùng lập (DAD):** Host gửi thông điệp **Neighbor Solicitation** đến địa chỉ *Solicited-Node Multicast* của địa chỉ vừa tạo. Nếu không ai phản hồi, địa chỉ chính thức được gán cho Interface.

## 4. Configuration 
- Kịch bản R1 nhận Prefix và chuyển tiếp cho Host

### Bước 1: R1 xin IP/Prefix trên cổng Hướng tới ISP (g0/0)
```text
R1(config)# interface g0/0
R1(config-if)# ipv6 address autoconfig
R1(config-if)# no shutdown
```
### Bước 2: R1 cấu hình cổng Hướng về LAN (g0/1) để phát RA cho Host
```text
R1(config)# ipv6 unicast-routing              ! Bắt buộc: Bật định tuyến IPv6 để R1 biết phát gói RA
R1(config)# interface g0/1
R1(config-if)# ipv6 address 2001:DB8:1:2::1/64 ! Đặt IP tĩnh thuộc subnet LAN (hoặc dùng Prefix nhận từ ISP)
R1(config-if)# no shutdown                    ! Khi 'no shutdown', R1 tự động phát gói RA xuống LAN
```
# DAD (Duplicate Address Detection) - Phát hiện địa chỉ trùng lặp

- **DAD** là cơ chế quan trọng trong IPv6 dùng để kiểm tra xem một địa chỉ IPv6 (cả Link-Local lẫn Global Unicast) chuẩn bị gán cho interface có bị trùng với thiết bị nào khác trong cùng phân đoạn mạng LAN hay không.
- **Thời điểm thực hiện:** Ngay khi một địa chỉ IPv6 được cấu hình (tĩnh hoặc tự động qua SLAAC) và trước khi địa chỉ đó chính thức được đưa vào sử dụng.
- **Sử dụng 2 thông điệp ICMPv6 trong NDP:**
  - **NS (Neighbor Solicitation)**: Gói tin gửi đi để dò tìm.
  - **NA (Neighbor Advertisement)**: Gói tin phản hồi nếu có trùng lặp.
- Lưu ý: DAD chỉ có nhiệm vụ phát hiện địa chỉ IPv6 bị trùng, không có nhiệm vụ tự giải quyết việc trùng địa chỉ.
    * Nếu sử dụng SLAAC: Host sẽ tự tạo (generate) một địa chỉ IPv6 mới từ prefix nhận được và thực hiện DAD lại.
    * Nếu sử dụng DHCPv6: Host sẽ gửi yêu cầu để DHCPv6 Server cấp một địa chỉ IPv6 khác.
    * Nếu cấu hình Static: Quản trị viên phải cấu hình lại một địa chỉ IPv6 khác.

---

## Cách hoạt động chi tiết

1. **Khởi tạo (Tentative State):**
   - Địa chỉ IPv6 mới khởi tạo sẽ đi vào trạng thái tạm thời (Tentative). Interface chưa thể gửi/nhận dữ liệu bằng địa chỉ này.

2. **Gửi gói NS:**
   - Host gửi một gói **ICMPv6 NS** đến địa chỉ **Solicited-Node Multicast** tương ứng với chính địa chỉ IPv6 mà nó đang định dùng.
   - Địa chỉ nguồn (Source IPv6) của gói NS này được đặt là `::` (Unspecified Address) vì địa chỉ mới chưa được chính thức xác nhận.

3. **Xử lý phản hồi:**
   - **Trường hợp 1 (Duy nhất - Không trùng):** Không có thiết bị nào trả lời gói NA trong thời gian chờ $\rightarrow$ Địa chỉ IPv6 chính thức có hiệu lực và chuyển sang trạng thái an toàn để sử dụng.
   - **Trường hợp 2 (Trùng lặp - Duplicate):** Có một thiết bị khác trong LAN đang dùng địa chỉ đó $\rightarrow$ Thiết bị đó sẽ phản hồi lại bằng gói **ICMPv6 NA** $\rightarrow$ Host biết địa chỉ bị trùng, lập tức hủy địa chỉ này (báo lỗi Duplicated) và không đưa vào sử dụng.




