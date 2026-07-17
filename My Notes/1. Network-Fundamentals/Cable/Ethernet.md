Standard Ethernet

- 1. MDI (Medium Dependent Interface)
    - Đây là cổng tiêu chuẩn trên các thiết bị đầu cuối như PC, router và firewall.
    - Các tín hiệu truyền (TX) / nhận (RX) được cố định:
        + TX xuất ra chân 1/2
        + RX nhận vào chân 3/6
    - Nếu kết nối trực tiếp giữa hai thiết bị MDI, cần sử dụng cáp chéo (crossover cable).

- 2. MDI-X (MDI Crossover)
    - Đây là cổng có khả năng đảo TX/RX (các cổng switch thường là MDI-X).
    - TX/RX sẽ tự động được hoán đổi nếu cần → dễ dàng kết nối thiết bị mà không cần cáp chéo.
    - Cổng switch: mặc định là MDI-X, cho phép kết nối với PC/router/firewall bằng cáp thẳng (straight-through cable).

- 3. Những thiết bị nào
    - Switch, Hub -> MDI-X
    - PC / Router / Firewall -> MDI

    * Điều này có nghĩa là:
        + PC → Switch, sử dụng cáp thẳng (straight-through cable).
        + Switch → Switch, sử dụng cáp chéo (crossover cable), trừ khi cổng hỗ trợ Auto-MDIX (các cổng hiện đại tự động chuyển đổi TX/RX).