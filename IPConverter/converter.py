from netaddr import *
from ip4to6 import *
from ip6to4 import *
from inputhandler.inputhandler import Inputhandler


class Converter:
   
    def convertV4ToBinary(ipv4):
        return IPAddress(ipv4).bits()

    def convertV6ToBinary(ipv6):
        return IPAddress(ipv6).bits()

    def convertSubnetmaskToBinary(subnetmask):
        return IPAddress(subnetmask).bits()

    convertSubnetmaskToBinary('255.255.255.0')



# inputV4 = Inputhandler.handleIPv4(Inputhandler)

# converter = IPv4ToIPv6(inputV4)
# converter.convert()

# converter2 = IPv6ToIPv4(converter.convert())
# converter2.convert()

    
