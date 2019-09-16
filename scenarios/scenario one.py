from scapy.all import *
import sys

ip=IPv6(src="fe80::200:ff:fe00:1", dst="fe80::200:ff:fe00:2")
icmp=ICMPv6EchoRequest()
p=(ip/icmp)
fs=fragment6(p,1280)
send(fs)