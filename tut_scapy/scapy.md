# Scapy Tutorial

## Capture Packets
scapy.sendrecv.AsyncSniffer
scapy.sendrecv.sniff

## Send Packets

scapy.sendrecv.srp
scapy.sendrecv.srp1
scapy.sendrecv.srploop

scapy.sendrecv.sr
scapy.sendrecv.s1
scapy.sendrecv.srloop

## Craft Packets

### Data Link Layer
scapy.layers.l2 : Ether, ARP, LLC, STP

### Internet Layer
scapy.layers.inet: IP, ICMP

### Transport Layer
scapy.layers.inet: TCP, UDP

### Presentation layer
scapy.layer.tls
scapy.layer.x509

### Application Layer
scapy.layers.http
scapy.layers.dhcp
scapy.layers.dns
scapy.layers.tftp

## Packets
scapy.packet
Raw, Packet

## Answering Machines
scapy.ansmachine
BOOTP, DHCP, DNS, ARP

## Automaton
TLS, TFTP
scapy.automaton

## Others
scapy.arch.windows
scapy.base_classes.Net
scapy.conf
scapy.supersocket
scapy.utils

## Other protocols
scapy.contrib
