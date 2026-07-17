- Theo mặc định, truy cập console không yêu cầu mật khẩu. Tuy nhiên, nên đặt mật khẩu để tăng bảo mật  

- R1(config)# line console 0      # chỉ có 1 console port vật lý  
- R1(config-line)# password ccna   # đặt mật khẩu cho console  
- R1(config-line)# login           # bật xác thực khi đăng nhập console  

- Sau khi cấu hình, bất kỳ ai truy cập console đều phải nhập mật khẩu ccna  