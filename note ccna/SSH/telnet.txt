Telnet uses TCP port 23
Data is plain text → can be captured by Wireshark

1. Create User for Telnet Login
# Normal user
R1(config)# username annk secret ccna

# Admin user (privilege 15)
R1(config)# username annk privilege 15 secret ccna

⚠ No need to configure hostname, domain name, or RSA key for Telnet. Those are only for SSH.

2. config Telnet
R1(config)# line vty 0 15
R1(config-line)# login local             # only allow locally created users
R1(config-line)# transport input telnet  # allow only Telnet access

# Key Notes
Telnet does not encrypt data → insecure
SSH is preferred for secure remote management