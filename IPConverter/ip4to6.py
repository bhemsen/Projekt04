from netaddr import *

class IPv4ToIPv6:
    def __init__(self, ip):
        self.ip = ip

    def printIP(self):
        print(self.ip)

    def convert(self):
        ipV6 = IPAddress(self.ip).ipv6()
        print (ipV6)
        return ipV6 
