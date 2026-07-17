# CDP - LLDP Overview

- **CDP (Cisco Discovery Protocol)** và **LLDP (Link Layer Discovery Protocol)** là hai giao thức dùng để **khám phá và trao đổi thông tin với các thiết bị lân cận (neighbor discovery)**.

- Neighbor ở đây được hiểu là các thiết bị **kết nối trực tiếp với nhau qua một liên kết Layer 2**.
    - Ví dụ: Router kết nối trực tiếp với Switch.
    - Switch kết nối trực tiếp với Switch khác.

- CDP và LLDP hoạt động tại **Layer 2 (Data Link Layer)** trong mô hình OSI.
    - Không cần sử dụng địa chỉ IP để trao đổi thông tin.
    - Hoạt động dựa trên địa chỉ MAC và Ethernet Frame.

- Mặc dù hoạt động ở Layer 2, các giao thức này có thể quảng bá một số thông tin ở Layer 3 như:
    - Management IP Address.
    - Network address.
    - ...

- **CDP**:
    - Là giao thức độc quyền của Cisco.
    - Chủ yếu được sử dụng trong môi trường thiết bị Cisco.

- **LLDP**:
    - Là giao thức chuẩn mở của **IEEE 802.1AB**.
    - Có khả năng hoạt động giữa các thiết bị của nhiều nhà sản xuất khác nhau.

> Tóm lại:
> - CDP = Cisco Discovery Protocol → Cisco proprietary.
> - LLDP = Link Layer Discovery Protocol → IEEE standard, hỗ trợ đa hãng.