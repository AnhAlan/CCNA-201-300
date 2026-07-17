Power over Ethernet (PoE)

- 1 cáp LAN = vừa truyền dữ liệu vừa cấp nguồn điện
- Không cần adapter nguồn riêng cho thiết bị

---

- Thiết bị sử dụng PoE:
    * Access Point (AP)
    * IP Camera
    * IP Phone
    * IoT devices
    * → Nói chung: thiết bị mạng đặt xa ổ điện

---

- Cách hoạt động

    - Gồm 2 thành phần chính:
        + PSE (Power Sourcing Equipment)
            → Switch hoặc injector cung cấp nguồn điện
        + PD (Powered Device)
            → Thiết bị nhận điện (AP, camera, v.v.)

---

- Quy trình đơn giản:
    * Switch kiểm tra thiết bị có hỗ trợ PoE hay không
    * Nếu có → cấp nguồn
    * Nếu không → không cấp nguồn (tránh cháy thiết bị)

---

- Cơ chế nhận diện:
    * Cisco Discovery Protocol (CDP) – của Cisco
    * Link Layer Discovery Protocol (LLDP) – chuẩn chung

---

- Chuẩn PoE

![alt text](images/standard.png)

---

- Các mức PoE (PoE / PoE+ / UPOE / UPOE+)

![alt text](images/inside.png)