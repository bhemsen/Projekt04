from netaddr import *
from ip4to6 import *
from ip6to4 import *
from Inputhandler.inputHandler import *

converter = IPv4ToIPv6('192.168.0.255')
converter.convert()

converter2 = IPv6ToIPv4(converter.convert())
converter2.convert()

