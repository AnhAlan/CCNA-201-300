Layer 2 switches do not have a physical IP for remote access.
To allow SSH/Telnet, we create an SVI (Switch Virtual Interface).

1. Create SVI (Management IP)
Switch(config)#int vlan 1
Switch(config-if)#ip add 192.168.1.5 255.255.255.0
Switch(config-if)#no shut

2. gateway
Switch(config)#ip default-gateway 192.168.1.1 (ip router)
- Ensures PCs from other subnets can reach the switch for SSH/Telnet.

3. Create User for SSH/Telnet Login
# Normal user
Switch(config)# username annk secret ccna

# Admin user
Switch(config)# username annk privilege 15 secret ccna

For SSH only: you also need hostname, domain name, and RSA key (read SSH.txt) 
Telnet does not require RSA key.

4.config line vty 
- line 0 15
- login local
- transport input ssh\telnet (or both if we want)

✅ Notes
Telnet: plain text → insecure
SSH: encrypted → preferred
Make sure VLAN used for SVI is active and connected to router for inter-LAN access.
