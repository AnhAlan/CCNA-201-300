# NTP Stratum Hierarchy

- **Khái niệm:** Là mô hình phân cấp dạng cây (Tree-based model) trong giao thức NTP, được dùng để sắp xếp và định vị khoảng cách từ một thiết bị mạng tới nguồn thời gian chuẩn gốc.
- **Mục đích:**
  - **Phân tải (Load Balancing):** Tránh việc hàng triệu thiết bị cùng truy cập vào đồng hồ chuẩn gây quá tải.
  - **Tăng tính dự phòng (Redundancy):** Cho phép tự động chuyển sang nguồn thời gian khác khi máy chủ cấp trên gặp sự cố.
  - **Đảm bảo độ chính xác:** Tự động chọn đường đi có độ trễ nhỏ nhất và loại bỏ nguồn thời gian bị sai lệch (falseticker).

---

## Các cấp độ Phân tầng (Stratum Levels)

- **Stratum 0 (Primary Reference Clocks):**
  - Là thiết bị phần cứng tạo thời gian gốc tuyệt đối (Đồng hồ nguyên tử Cesium/Rubidium, GPS, CDMA, WWVB).
  - **Lưu ý:** Không kết nối trực tiếp vào mạng IP mà nối với máy chủ NTP qua cổng chuyên dụng (Serial, PPS).

- **Stratum 1 (Primary Time Servers):**
  - Kết nối trực tiếp với thiết bị Stratum 0.
  - Được xem là các máy chủ thời gian chính trên Internet (mất độ trễ cực nhỏ do kết nối phần cứng).

- **Stratum 2 (Secondary Time Servers):**
  - Nhận thời gian qua mạng từ một hoặc nhiều máy chủ Stratum 1.
  - Thường trao đổi dữ liệu ngang hàng (peering) với các máy Stratum 2 khác để xác minh và kiểm tra chéo độ chính xác.

- **Stratum 3 – 15 (Clients & Downstream Servers):**
  - Mỗi cấp tiếp theo nhận thời gian từ cấp ngay trên nó theo công thức: $Stratum_{n+1} = Stratum_n + 1$.
  - Hầu hết các máy tính cá nhân, router, switch và server doanh nghiệp hoạt động ở cấp Stratum 3 hoặc 4.

- **Stratum 16 (Unsynchronized / Invalid):**
  - Đánh dấu trạng thái thiết bị **hoàn toàn chưa được đồng bộ**, mất kết nối mạng hoặc nguồn thời gian không đáng tin cậy.

---

## Quy tắc hoạt động chính

- **Cơ chế cộng tầng:** Khi thiết bị A (Stratum $N$) đồng bộ từ thiết bị B (Stratum $M$), Stratum của A sẽ là $M + 1$.
- **Độ chính xác & Độ trễ:** Càng xuống cấp Stratum cao hơn (con số lớn hơn), độ chính xác càng giảm nhẹ do độ trễ truyền dẫn trên đường truyền mạng (Network Latency & Jitter).
- **Kết nối Ngang hàng (Peering):** Cho phép các server cùng cấp Stratum so sánh thời gian để phát hiện và loại bỏ server bị lỗi.
- **Chống vòng lặp (Loop Prevention):** NTP tự động ghi nhận đường đi để tránh tình trạng hai máy chủ lấy thời gian xoay vòng của nhau.