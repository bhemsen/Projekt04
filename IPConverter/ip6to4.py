from netaddr import *

class IPv6ToIPv4:
    def __init__(self, ip):
        self.ip = ip

    def printIP(self):
        print(self.ip)

    def convert(self):
        ipV4 = IPAddress(self.ip).ipv4()
        print (ipV4)
        return ipV4 