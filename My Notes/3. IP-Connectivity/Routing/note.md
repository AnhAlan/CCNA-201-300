- Steps to select a routing protocol for sending data

1. Longest Prefix Match (MOST IMPORTANT)
    Choose the route with the longest subnet mask (/ largest value)
    This means the most specific match, not “closest” 
    Example:

    Destination IP: 10.1.1.19

    Routes:
    RIP: 10.1.1.16/28 
    OSPF: 10.1.1.0/24 
    EIGRP: 10.1.0.0/26 (does NOT match)

    Valid matches:
    10.1.1.16/28
    10.1.1.0/24

    Choose: 10.1.1.16/28 (because /28 is longer than /24)

2. Administrative Distance
- Used only when prefix lengths are equal
- Choose the route with the lowest AD (more trustworthy)

3. Metric
- Used only when AD is equal
- Choose the route with the lowest metric (better path)