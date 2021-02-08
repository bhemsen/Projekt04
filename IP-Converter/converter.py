from netaddr import *
from ip4to6 import *
from ip6to4 import *
from inputhandler.inputhandler import Inputhandler

inputV4 = Inputhandler.handleIPv4(Inputhandler)

converter = IPv4ToIPv6(inputV4)
converter.convert()

converter2 = IPv6ToIPv4(converter.convert())
converter2.convert()

