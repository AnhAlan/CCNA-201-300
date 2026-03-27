1. loopback interface
    It's a virtual interface on the router/switch.
    It's not connected to any physical hardware → it's always up if configured.
    Used for:
    Remote device management (e.g., SSH/Telnet)
    Providing a stable IP source for routing protocols (OSPF, BGP, etc.)
    ex:
    Router(config)# interface loopback0
    Router(config-if)# ip address 10.1.1.1 255.255.255.0

2. loopback address
    This is a special IP address used for self-referencing devices.
    Standard range: 127.0.0.0/8, most common is 127.0.0.1.
    Used for:
    + Testing the TCP/IP stack (ping 127.0.0.1)
    + Testing internal services that do not go to the external network
    + It is not necessarily assigned to the loopback interface, but it is common to assign 127.0.0.1 or 127.x.x.x to this interface.