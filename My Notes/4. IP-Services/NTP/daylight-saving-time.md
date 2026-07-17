# Daylight Saving Time (DST)

- **DST** (Daylight Saving Time) → chỉnh đồng hồ nhanh hơn 1 giờ vào mùa hè, và lùi lại 1 giờ (trả về bình thường) vào mùa đông (tùy theo quy định từng quốc gia)
- không phải tất cả quốc gia đều làm cấu hình
## Cấu hình DST lặp lại hằng năm (recurring)

```
R2(config)# clock summer-time VNS recurring 2 Sunday March 02:00 1 Sunday November 02:00
```

- `VNS`: tên viết tắt của múi giờ khi đang trong giờ DST (zone name) — có thể đặt tùy ý
- `recurring`: nghĩa là quy tắc này sẽ được **lặp lại hằng năm** (không cần cấu hình lại mỗi năm)
- `2 Sunday March 02:00`: thời điểm **bắt đầu** DST → Chủ nhật thứ 2 của tháng 3, lúc 02:00 (đồng hồ sẽ chỉnh nhanh thêm 1 giờ)
- `1 Sunday November 02:00`: thời điểm **kết thúc** DST → Chủ nhật thứ 1 của tháng 11, lúc 02:00 (đồng hồ trở về giờ bình thường)

> Cú pháp đầy đủ:
> ```
> clock summer-time <zone> recurring [week day month hh:mm week day month hh:mm [offset]]
> ```
> - `week`: tuần thứ mấy trong tháng (1–4, hoặc `first`/`last`)
> - `day`: thứ trong tuần (Sunday, Monday, ...)
> - `month`: tháng
> - `hh:mm`: giờ áp dụng
> - `[offset]`: số phút chỉnh lệch (mặc định là 60 phút nếu không ghi rõ)

## Cấu hình DST một lần (không lặp lại)
- Nếu không dùng `recurring`, có thể dùng `date` để chỉ định một ngày cụ thể, chỉ áp dụng đúng 1 lần (không tự lặp lại năm sau):
```
clock summer-time <zone> date <date month year hh:mm> <date month year hh:mm> [offset]
```
