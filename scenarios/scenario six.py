from scapy.all import *
import sys

ip=IPv6(src="fe80::200:ff:fe00:1", dst="fe80::200:ff:fe00:2")
tcp=TCP()
F=IPv6ExtHdrFragment()
op=[Pad1()]
for i in range(0,1300): op=op+[Pad1()]
pad=[Pad1(),Pad1(),Pad1(),Pad1(),Pad1(),Pad1()]
D=IPv6ExtHdrDestOpt(options=op)

p=(ip/F/D/tcp/"PayLoad PayLoad PayLoad PayLoad PayLoad")
p.display()
fs=fragment6(p,1280)
send(fs)