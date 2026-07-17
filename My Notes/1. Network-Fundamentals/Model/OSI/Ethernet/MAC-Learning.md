- Switch học địa chỉ MAC từ source của frame đi vào.
- Switch ghi nhớ port mà frame đã đi vào.
- Timeout: mục nhập sẽ bị xóa sau khoảng ~5 phút nếu không có hoạt động.
- Mục đích:
    * Tránh việc flood frame không cần thiết.
    * Chuyển tiếp (forward) frame unicast đến đúng port đích.