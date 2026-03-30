- ARP – Address Resolution Protocol
- Purpose: Allows Layer 2 devices (Ethernet) to discover the Layer 3 IP address → MAC address mapping.
- Problem: Switch/host knows IP (Layer 3) but needs MAC address (Layer 2) to send the frame.

1. ARP Process
- ARP Request (Who has …?)
- Host wants to send data to a specific IP.
- It broadcasts an ARP Request to all devices in the local network.
- Request asks: “Who has IP X.X.X.X? Tell me your MAC address.”

- ARP Reply
- The device with the requested IP responds with its MAC address.
- This reply is sent as unicast directly back to the requester.

2. Attention
- ARP is used only within a local subnet (broadcast domain).
- Devices cache ARP entries to avoid repeated requests.
- Works at Layer 2 (Ethernet) but resolves Layer 3 IP → MAC.