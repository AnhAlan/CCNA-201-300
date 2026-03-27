Standard Ethernets

1. MDI (Medium Dependent Interface)
    It is a standard port on end devices such as PCs, routers, and firewalls.
    The transmit (TX) / receive (RX) signals are fixed:
    TX outputs to pins 1/2
    RX receives to pins 3/6
    If connecting directly between two MDIs, a crossover cable is required.

2. MDI-X (MDI Crossover)
    It's a rotating TX/RX port (switch ports are usually MDI-X).
    TX/RX is automatically switched if needed → easily connect devices without a crossover cable.
    Switch port: defaults to MDI-X, allowing straight-through cable connection to PC/router/firewall.

3. Which devices
    Switch, Hub -> MDI-X 
    PC / Router / firewall -> MDI

    * is meas:
    PC → Switch, use a straight-through cable.
    Switch → Switch, use a crossover cable, unless the port supports Auto-MDIX (modern ports automatically switch between TX/RX).
