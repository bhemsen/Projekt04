from netaddr import *
from ip4to6 import *
from ip6to4 import *

print(IPAddress('192.0.2.15').ipv4())

converter = IPv4ToIPv6('192.168.0.1')
converter.printIP()
