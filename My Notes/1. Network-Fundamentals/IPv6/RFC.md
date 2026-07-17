# RFC (Request for Comments) 
- là các tài liệu kỹ  thuật mô tả
    * chuẩn giao thức internet
    * quy tắc triển khai
    * cách thiết bị nên hoạt động
- IEFT (internet enginerring task force) viết nhiều RFC về TCP/IP, IPv6, DNS,...
- internet society quản lý hệ sinh thái RFC
- RFC 5952 IPv6 Address Text Representation đưa ra quy tắc chuẩn hóa cách ghi địa chỉ IPv6.
    * Một địa chỉ IPv6 có thể được viết theo nhiều cách khác nhau nhưng vẫn cùng một địa chỉ.
    * mặc dù nhiều tổ chức hoặc cá nhân không tuân theo
- RFC 5952 về quy tắt viết IPv6
    * các số 0 ở đầu mỗi nhóm PHẢI loại bỏ
    * :: chỉ nên rút gọn nhóm số 0 dài nhất, nếu trường hợp chỉ có 1 nhóm số 0 thì không sử dụng ":"
        * 2001:0000:0000:0000:0f2a:0000:0000:00b1
        * 2001::0f2a:0:0:b1
    * nếu có 2 dãy nhóm số 0 bằng nhau về độ dài chọn dãy nhóm bên trái cùng
        * 2001:0000:0000:0000:0f72:0000:0000:89b1
        * 2001::0f72:0:0:89b1
    * các ký tự là chữ cái VIẾT THƯỜNG
- lưu ý đây là KHUYẾN NGHỊ của RFC thôi