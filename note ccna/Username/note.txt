1. User on Devices
Users are created on network devices (switches, routers).
They are used for:
Logging into console
Logging into VTY lines (SSH/Telnet)
Access control based on privilege level

2. How created user
- user annk 

# Normal user
username annk password ccna      # password in plain text (not encrypted)
username annk secret ccna        # password encrypted (recommended)

# User with access control
username annk privilege 15 password/secret ccna

// privilege level (0 - 15 because filed has 4 bits)
0 : only logout -> not usually use
1 : User EXEC mode (default) → cannot configure device
2 - 14: Custom levels → can allow specific commands 
15 : privilege EXEC mode (admin) -> full controll, login to EXEC mode instead of user EXEC mode