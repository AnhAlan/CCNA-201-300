# FLSM (Fixed Length Subnet Mask)

- FLSM là kỹ thuật chia subnet với **cùng một subnet mask cho tất cả các mạng con**.

---

## Ý tưởng chính
- Tất cả subnet có kích thước bằng nhau.
- Mỗi subnet có cùng số lượng host.
- Dễ tính toán nhưng dễ lãng phí IP.

---

## Cách hoạt động
- Chọn một subnet mask chung.
- Chia mạng gốc thành nhiều subnet giống hệt nhau.
- Không quan tâm từng subnet cần bao nhiêu host.

---

## Đặc điểm

- Ưu điểm:
    + Dễ thiết kế và tính toán
    + Dễ triển khai
    + Phù hợp mạng nhỏ hoặc đơn giản

- Nhược điểm:
    + Lãng phí địa chỉ IP
    + Không linh hoạt
    + Không tối ưu tài nguyên mạng

---

## Ví dụ
- Mạng gốc: 192.168.1.0/24
- Chia thành 4 subnet bằng nhau:
    + /26 → mỗi subnet có 64 IP
    + Subnet 1: 192.168.1.0/26
    + Subnet 2: 192.168.1.64/26
    + Subnet 3: 192.168.1.128/26
    + Subnet 4: 192.168.1.192/26

---

## So sánh nhanh với VLSM
- FLSM:
    + Chia đều tất cả subnet
    + Dễ làm nhưng lãng phí
- VLSM:
    + Chia linh hoạt theo nhu cầu
    + Tối ưu IP hơn

---

## Ghi nhớ nhanh
- FLSM = Fixed size subnet
- 1 mask cho tất cả subnet
- Dễ nhưng không tối ưu