- ARP – Address Resolution Protocol (Giao thức phân giải địa chỉ)
- Mục đích: Cho phép thiết bị Layer 2 (Ethernet) tìm ánh xạ giữa địa chỉ IP Layer 3 và địa chỉ MAC.
- Vấn đề: Switch/host biết địa chỉ IP (Layer 3) nhưng cần địa chỉ MAC (Layer 2) để gửi frame.

---

## 1. Quá trình ARP

- ARP Request (Who has ...?)
    - Host muốn gửi dữ liệu đến một địa chỉ IP cụ thể.
    - Nó gửi một gói ARP Request dưới dạng broadcast đến tất cả thiết bị trong mạng cục bộ.
    - Nội dung yêu cầu:
        + "Ai đang sở hữu IP X.X.X.X?"
        + "Hãy cho tôi biết địa chỉ MAC của bạn."

- ARP Reply
    - Thiết bị sở hữu IP được yêu cầu sẽ phản hồi bằng địa chỉ MAC của nó.
    - Phản hồi này được gửi dưới dạng unicast trực tiếp về thiết bị yêu cầu.

---

## 2. Lưu ý

- ARP chỉ hoạt động trong cùng subnet (broadcast domain).
- Thiết bị sẽ lưu các bản ghi ARP vào ARP Cache để tránh gửi yêu cầu lặp lại.
- ARP hoạt động trên Ethernet (Layer 2) nhưng có nhiệm vụ phân giải địa chỉ IP (Layer 3) thành địa chỉ MAC.