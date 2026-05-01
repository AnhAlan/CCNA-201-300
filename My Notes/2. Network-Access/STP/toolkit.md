- Là tập hợp nhiều công cụ nhỏ của STP
- có vài công cụ có thể cấu hình cả toàn cục và cục bộ

# 1. PortFast
- để 1 port chuyển lên trạng thái forward tốn 30 giây, nhưng nếu đầu bên kia không phải switch thì việc tốn 30 giây cho mỗi lần lên forward là không cần thiết
- Portfast giúp port lập tức Forward mà không cần đợi 30 giây - tức không cần trải qua trạng thái listening và learning
- chỉ nên cấu cổng không phải trunk mode
- có 2 loại portfast
    * edge trunk: kết nối pc -> nên sử dụng thêm BPDU Guard
    * Network: có thể dùng để kết nối với switch -> yêu cầu switch có tính năng **bridge assurance**
- mặc dù có thể portfast 2 switch nhưng Cisco khuyến nghị không nên portfast giữa 2 switch
- một số trường hợp sủ dụng portfast ở trunk
    * kết nối với VMs với các vlan khác nhau
    * Router on a stick
- nếu PortFast nhận BPDU nó sẽ thoát khỏi chế độ PortFast và quay về trạng thái mặc định

# 2. BPDU Guard
- Nếu port nhận BPDU: → err-disable (shutdown port)
- Dùng cho PortFast edge
- Mục tiêu: chống cắm nhầm switch 

# 3. BPDU filder
- Mỗi port cứ 2 giây gửi BPDU -> nếu phía bên kia là pc hay giả mạo thì việc gửi BPDU sẽ tốn tài nguyên hoặc lộ thông tin
- BPDU filder sẽ chặn gửi BPDU
- BPDU filder sẽ hoạt động tốt hơn trên PortFast
- nếu nhận BPDU thì sẽ *Drop* -> do không tham gia vào stp

# 4. Root Guard
- nếu kết nối các mạng LAN khác sẽ tạo đường đi không tốt ưu
- Ngăn switch khác trở thành Root Bridge
- Nếu nhận BPDU “tốt hơn root hiện tại”: → port chuyển root-inconsistent (blocking)
- để kịch hoạt lại cổng đã blocking thì port đó phải ngưng nhận BPDU tốt hơn
- reset bằng cách: shutdown -> no shutdown
- nên đặt các cổng của Root Bridge -> để ngăn các switch khác chiếm Root Bridge

# 5. Loop Guard
- Bảo vệ khi mất BPDU bất thường -> xảy ra khi liên kết đơn -> truyền hoặc nhận 1 chiều
- Nếu không nhận BPDU: → port chuyển loop-inconsistent (blocking)
# 6. Up linkfast
- Dùng cho switch access (cũ – STP 802.1D)
- Khi uplink chính fail: → chuyển sang backup rất nhanh
- ít sử dụng - do tính năng cũ
# 7. Backbone fast
- Giúp hội tụ nhanh khi phát hiện path failure gián tiếp
- Rút ngắn thời gian chờ Max Age
- ít sử dụng - do tính năng cũ

# 8. Các loại kiểu port
- shr (shared): kết nối chia sẻ -> thường là half-duplex
- p2p: kết nối giữa các switch hoặc giữa rotuer -> thường là full-duplex
- Edge: cổng cấu hình portfast