# Scapy Tutorial

## Network Concepts

### Network Models
* TCP/IP
* OSI

### Datagrams

* PDU = Protocol data unit : Header + Data
* MTU = Maximum transmission unit, maximum payload

MAX(Eth) = 6 + 6 + 2 + MTU + 2 = 1518
MTU(Eth) = 1500 bytes

Datagram = Header + Data
* L2: Frame
* L3: Packet
* L4: Segment

### Error Correction

* Checksum
* CRC

## Capture Packets
* scapy.sendrecv.sniff
* scapy.sendrecv.AsyncSniffer

## Send Packets

* scapy.sendrecv.srp
* scapy.sendrecv.srp1
* scapy.sendrecv.srploop
* scapy.sendrecv.sr
* scapy.sendrecv.s1
* scapy.sendrecv.srloop

## Craft Packets

### Data Link Layer

* scapy.layers.l2.Ether
* scapy.layers.l2.ARP

### Internet Layer

* scapy.layers.inet.IP
* scapy.layers.inet.ICMP

### Transport Layer

* scapy.layers.inet.TCP
* scapy.layers.inet.UDP

### Presentation layer

* scapy.layers.tls

### Application Layer

* scapy.layers.http
* scapy.layers.dhcp
* scapy.layers.dns
* scapy.layers.tftp

## Other protocols
* scapy.contrib.modbus
* scapy.contrib.mqtt
* scapy.contrib.opc

## Answering Machines

* ARP
* BOOTP
* DHCP
* DNS

## Automaton

 * TLS
 * TFTP
 
## Helpers
 * scapy.arch.windows
 * scapy.base_classes.Net
 * scapy.conf
 * scapy.supersocket
 * scapy.utils
 
## Packet API

* Raw
* Packet

## Custom Protocols
