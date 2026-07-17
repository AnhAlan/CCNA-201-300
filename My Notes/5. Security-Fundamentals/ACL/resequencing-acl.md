# Resequencing ACL - Đánh lại số thứ tự ACL

- `resequence` dùng để **đánh lại sequence number** của các ACE trong một ACL.
- Thường sử dụng khi các sequence number không còn hợp lý (ví dụ: 5, 7, 8, 1000...), gây khó khăn khi quản lý hoặc chèn thêm ACE mới.
- `resequence` **không làm thay đổi thứ tự xử lý ACL**, mà chỉ thay đổi sequence number của các ACE.

## Cú pháp

```cisco
ip access-list resequence <acl-name | acl-number> <starting-sequence> <increment>
```

### Ví dụ

```cisco
R1(config)# ip access-list resequence 1 10 10
```

Ý nghĩa:

- Đánh lại sequence number của ACL **1**.
- ACE đầu tiên sẽ có sequence number là **10**.
- Các ACE tiếp theo sẽ tăng thêm **10**.

Ví dụ:

```text
10 deny 192.168.1.1
20 permit 192.168.2.0 0.0.0.255
30 deny 192.168.3.0 0.0.0.255
40 permit any
```

## Khi nào nên sử dụng?

- Sau khi thêm, xóa hoặc chỉnh sửa nhiều ACE khiến sequence number không còn liên tục.
- Muốn tạo khoảng trống giữa các ACE để dễ chèn thêm các mục mới sau này.
- Giúp ACL dễ đọc và dễ quản lý hơn.

# Standard Numbered ACL
- ip access-list resequence 1 10 10
# Standard Named ACL
- ip access-list resequence BLOCK_HOST 10 10
# Extended Numbered ACL
- ip access-list resequence 101 10 10
# Extended Named ACL
- ip access-list resequence WEB_FILTER 10 10