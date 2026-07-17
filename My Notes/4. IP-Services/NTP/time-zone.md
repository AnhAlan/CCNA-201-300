# Configuring the time zone

- Cú pháp cấu hình múi giờ trên thiết bị:

```
R2(config)# clock timezone VIE 7
```

- `VIE`: tên viết tắt của múi giờ (zone name) — có thể đặt tùy ý (thường đặt theo tên quốc gia/khu vực để dễ nhận biết, ví dụ VIE = Vietnam)
- `7`: số giờ lệch (offset) so với UTC → ở đây là +7 giờ so với UTC

> Cú pháp đầy đủ: `clock timezone <zone-name> <hours> [minutes]`
> - `<hours>`: số giờ lệch so với UTC (bắt buộc)
> - `[minutes]`: số phút lệch thêm (tùy chọn, dùng cho các múi giờ lệch không tròn giờ, ví dụ Ấn Độ là UTC+5:30)

- Sau khi cấu hình, `show clock` hoặc `show clock detail` sẽ hiển thị thời gian theo múi giờ vừa đặt (VIE) thay vì UTC

Ví dụ:
```
R2# show clock
07:30:10.123 VIE Sat Dec 26 2020
```
