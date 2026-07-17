# VLSM (Variable Length Subnet Mask)

- VLSM là kỹ thuật chia subnet với độ dài subnet mask khác nhau.
- Giúp sử dụng IP hiệu quả hơn (không bị lãng phí địa chỉ).

## Ý tưởng chính

- Không phải subnet nào cũng giống nhau
- Mỗi mạng có thể dùng mask khác nhau tùy nhu cầu host

---

## So sánh

- FLSM (Fixed Length Subnet Mask)
    - Tất cả subnet cùng kích thước
    - Dễ nhưng lãng phí IP

- VLSM
    - Subnet linh hoạt theo nhu cầu
    - Tối ưu IP


## Cách làm VLSM

- Bước 1: Sắp xếp mạng con theo số host giảm dần
- Bước 2: Chia subnet lớn trước
- Bước 3: Cấp phát IP liên tục
- Bước 4: Tính lại network / broadcast cho từng subnet


## Ví dụ ý tưởng
- 1 mạng /24
- Chia thành:
    - 50 hosts → /26
    - 25 hosts → /27
    - 10 hosts → /28

→ Không bị dư IP như chia đều

## Ghi nhớ nhanh

- VLSM = chia linh hoạt
- FLSM = chia đều
- Luôn cấp phát từ lớn → nhỏ
- Giúp tiết kiệm IPv4