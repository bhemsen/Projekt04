from netaddr import *


class Converter:

    def convertIPv4inIPv6(self, ipv4):
        ipV6 = IPAddress(ipv4).ipv6()
        print (ipV6)
        return ipV6 

    def convertIPv6inIPv4(self, ipv6):
        ipV4 = IPAddress(ipv6).ipv4()
        print (ipV4)
        return ipV4 
   
    def convertV4ToBinary(self, ipv4):
        return IPAddress(ipv4).bits()

    def convertV6ToBinary(self, ipv6):
        return IPAddress(ipv6).bits()

    def convertSubnetmaskToBinary(self, subnetmask):
        return IPAddress(subnetmask).bits()



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

    
