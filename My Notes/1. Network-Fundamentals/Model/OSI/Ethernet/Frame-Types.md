## Ethernet Frame Types

- **Unicast**
  - One sender → one receiver
  - Switch forwards to specific port

- **Broadcast**
  - One sender → all devices
  - Destination MAC: FF:FF:FF:FF:FF:FF

- **Multicast**
  - One sender → group of devices

- **Unknown Unicast**
  - Destination MAC not in MAC table
  - Switch will **flood** frame

---

## Switching Actions

- **Forward**
  - Known unicast → send to correct port

- **Flood**
  - Unknown unicast → send out all ports (except incoming)
  - Broadcast → send out all ports
  - Multicast → usually flooded (unless optimized)