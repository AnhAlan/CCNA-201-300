- User on Devices
- User được tạo trên các thiết bị mạng (switch, router).
- User được dùng để:
    - Đăng nhập vào console
    - Đăng nhập vào VTY lines (SSH/Telnet)
    - Kiểm soát truy cập dựa trên privilege level

---

- Cách tạo user
- user annk

- User thông thường
    - username annk password ccna      # mật khẩu dạng plain text (không mã hóa)
    - username annk secret ccna        # mật khẩu đã được mã hóa (khuyến nghị)

- User có phân quyền truy cập
    - username annk privilege 15 password/secret ccna

---

- privilege level (0 - 15 vì dùng 4 bit)
    - 0 : chỉ logout → ít khi dùng
    - 1 : User EXEC mode (mặc định) → không thể cấu hình thiết bị
    - 2 - 14: mức tùy chỉnh → có thể cấp quyền một số lệnh cụ thể
    - 15 : Privileged EXEC mode (admin) → toàn quyền, đăng nhập thẳng vào chế độ EXEC đặc quyền thay vì User EXEC