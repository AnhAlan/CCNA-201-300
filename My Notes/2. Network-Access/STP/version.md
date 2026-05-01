- IEEE và cisco đều có STP version riêng

# 1. IEEE: 
## 1.1. STP 802.1D
- tất cả vlan chia sẻ cùng stp
- không cân bằng tải

## 1.2. RSTP 802.1W
- nhanh hơn 802.1D
- tất cả vlan vẫn trong cùng STP

## 1.3. MSTP - 802.1S
- gom nhiều vlan vào 1 nhóm
- Giảm tài nguyên CPU
    * Có thể cân bằng tải (theo instance)
    * Dùng trong mạng lớn (enterprise)
# 2. Cisco
## 2.1. PVST 802.1D
- mỗi vlan đều có STP riêng
- loop backup -> blocking port mỗi vlan
- Hội tụ chậm (vì là STP cổ)

## 2.2. RSTP+ 802.1W
- mỗi vlan có RSTP riêng
    * Hội tụ nhanh
    * Cân bằng tải theo VLAN

# 3. Sự khác nhau RSTP và STP
- STP phụ thuộc timer -> Hội tụ chậm ~30–50s
- RSTP Không phụ thuộc timer kiểu cũ -> Dùng proposal/agreement (handshake) -> Hội tụ nhanh ~1–3s
- nếu RSTP phát hiện port edge (pc) lập tức forwarding, còn switch thì phải handshake
- STP: block -> listening -> learning -> forwarding -> disable
- RSTP: disaring -> learing -> forwarding
    * RSTP gộp Blocking + Listening → Discarding
- STP gồm có port role: Root Port - Designated Port - Non-designated (Blocking)
- RSTP gồm có port role: Root Port - Designated Port - Alternate Port - Backup Port 
- alternate port:  
    * Port dự phòng cho Root Port
    * Nhận BPDU tốt hơn từ switch khác
    * Đang ở trạng thái Discarding -> Khi Root Port fail → lên Forwarding ngay
- backup port:
    * xảy ra khi switch nối 2 dây vào hub -> 1 port là designed và 1 port backup
    * nếu port designed lỗi thì port backup lập tức lên designed port
- lưu ý: hub không tham gia STP, chỉ chuyển tiếp gói tin STP, và hub không cộng vào cost khi tính cost root
- mặc định cisco đời mới bật RSTP
- RSTP mặc định có uplink fast và backbone fast
- nếu các switch A dùng RSTP nối các switch B STP thì switch A sẽ hạ từ RSTP xuống STP để đồng bộ
    * nếu các switch chạy khác version có thể làm chậm xử lý
- STP thì chỉ có root bridge gửi BPDU, còn RSTP các switch đều gửi BPDU mỗi 2s