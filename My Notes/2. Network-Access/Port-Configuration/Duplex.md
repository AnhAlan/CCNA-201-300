- Duplex = the way two devices on the same port communicate with each other
- Layer: 1/2 (Physical + Data Link)
- Impact: transmission speed + collision risk

1. Half Duplex

- One-way data at a time
- Example: walkie-talkie → must speak and listen alternately
- Previously used hubs, prone to collisions, required CSMA/CD
- Speed: 10/100 Mbps

2. Full Duplex

- Two-way data simultaneously
- Example: telephone → speak and listen simultaneously
- No collisions
- Requires a switch + standard cable (Cat5e/6 or higher)
- Speed: 10/100/1000 Mbps


3. Auto Duplex
- Devices automatically negotiate duplex and speed
- Common CCNA commands:
- show interfaces → view duplex/speed
- interface gi0/1 → duplex full/auto, speed 100/auto

- Tip: Avoid mismatch duplexes (Full ↔ Half) → reduced throughput + more collisions

4. Config

* Switch(config)#int fa0/1
* Switch(config-if)#duplex full (recommend)
* Switch(config-if)# speed 100 (fa -> 100)
* make sure 2 devices conect use same duplex 
* use auto when
    + new version devices
    + if old version done use auto
* Ethernet
    + Ethernet 10, FastEthernet 100 : half \ full \ auto
    + GigabitEthernet 1000 : full \ auto
* Serial
    + allways full -> only config DTE & DCE

5. Note
- make sure 2 deives same duplex puzzle:
    * auto - auto
    * manual - manual
-> 