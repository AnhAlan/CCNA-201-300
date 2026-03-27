- By default, console access does not require a password. It’s recommended to set one for security.

R1(config)# line console 0      # only one physical console port
R1(config-line)# password ccna   # set console password
R1(config-line)# login           # enable authentication for console login

- After this, anyone accessing the console port must enter the password ccna.

