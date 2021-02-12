from netaddr import *
from inputhandler.Inputhandler import Inputhandler


class Converter:

    def convertIPv4inIPv6(ipv4):
        ipV6 = IPAddress(ipv4).ipv6()
        print (ipV6)
        return ipV6 

    def convertIPv6inIPv4(ipv6):
        ipV4 = IPAddress(ipv6).ipv4()
        print (ipV4)
        return ipV4 
   
    def convertV4ToBinary(ipv4):
        return IPAddress(ipv4).bits()

    def convertV6ToBinary(ipv6):
        return IPAddress(ipv6).bits()

    def convertSubnetmaskToBinary(subnetmask):
        return IPAddress(subnetmask).bits()

    convertSubnetmaskToBinary('255.255.255.0')


    #  takes a Dictionary as attribute from the inputhandler and converts it into an IPNetwork Objekt and returns it
    def convertToNetwork(self, data):
        ipNetwork = IPNetwork(data['networkaddress'])
        ipNetwork.netmask = data['subnetmask']
        return ipNetwork

# inputV4 = Inputhandler.handleIPv4(Inputhandler)

# converter = IPv4ToIPv6(inputV4)
# converter.convert()

# converter2 = IPv6ToIPv4(converter.convert())
# converter2.convert()

    
