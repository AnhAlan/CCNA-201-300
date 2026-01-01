from scapy.all import sniff

def show_packet(packet):
    if packet.haslayer("IP"):
        packet.show()

sniff(filter="ip", prn=show_packet, count=1)
