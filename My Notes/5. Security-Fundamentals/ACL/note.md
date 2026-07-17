# ACL (Access Control List) - Danh sách kiểm soát truy cập

- ACL có nhiều công dụng:
    * Kiểm soát quyền truy cập vào tài nguyên mạng.
    * Hoạt động như một bộ lọc gói tin (*packet filter*).
    * Cho phép hoặc từ chối lưu lượng dựa trên nhiều tiêu chí như:
        - Địa chỉ IP nguồn.
        - Địa chỉ IP đích.
        - Giao thức (TCP, UDP, ICMP, ...).
        - Cổng nguồn/cổng đích (đối với Extended ACL).

# Cách ACL hoạt động

- ACL được tạo trong **Global Configuration Mode** trên router.

- Ví dụ:

    * Nếu IP nguồn = `192.168.1.0/24` → `permit`
    * Nếu IP nguồn = `192.168.2.0/24` → `deny`
    * Nếu IP nguồn = `any` → `permit`

- Việc tạo ACL trong Global Configuration **chưa làm ACL có hiệu lực**.
- Muốn ACL hoạt động, phải **gắn (apply)** ACL vào một interface bằng lệnh `ip access-group`.

## Hướng áp dụng ACL

ACL có thể được áp dụng theo hai hướng:

- **Inbound**: kiểm tra gói tin **ngay khi đi vào** interface.
- **Outbound**: kiểm tra gói tin **ngay trước khi rời khỏi** interface.

> **Lưu ý:** Một interface chỉ có thể áp dụng **một ACL cho mỗi hướng và mỗi giao thức** (ví dụ: một IPv4 ACL inbound và một IPv4 ACL outbound). Có thể đồng thời áp dụng một ACL inbound và một ACL outbound trên cùng interface.

## ACL gồm các ACE

- ACL được tạo thành từ nhiều **ACE (Access Control Entry)**.
- Một ACL có thể chứa một hoặc nhiều ACE.
- Mỗi ACE gồm:
    * Điều kiện so khớp (*match condition*).
    * Hành động (`permit` hoặc `deny`).

## Thứ tự các ACE rất quan trọng

- Router kiểm tra các ACE **từ trên xuống dưới** theo thứ tự sequence number.
- Khi một gói tin **khớp (match)** với một ACE:
    * Router thực hiện hành động (`permit` hoặc `deny`).
    * Dừng kiểm tra các ACE còn lại.

> Vì vậy, các ACE nên được sắp xếp từ **cụ thể** đến **tổng quát** để tránh các điều kiện phía trên làm các ACE phía dưới không bao giờ được kiểm tra.

## Implicit Deny

- Cuối mỗi ACL luôn tồn tại một ACE mặc định:

```text
deny any
```

- ACE này **không hiển thị trong cấu hình**, nhưng luôn tồn tại.
- Nếu một gói tin không khớp với bất kỳ ACE nào trong ACL thì router sẽ áp dụng **implicit deny** và loại bỏ gói tin.