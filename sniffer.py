from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

print("Starting Network Sniffer...")

sniff(prn=packet_callback, count=10)