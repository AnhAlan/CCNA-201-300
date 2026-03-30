- Switch learns MAC from source of incoming frames.
- Switch remembers the port where the frame arrived.
- Timeout: Entry removed after ~5 minutes if inactive.
- Purpose:
    * Avoid unnecessary frame flooding.
    * Forward unicast frames to the correct port.