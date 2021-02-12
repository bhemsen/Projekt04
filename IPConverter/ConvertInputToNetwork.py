from netaddr import *
class ConvertInputToNetwork:
    def __init__(self):
            pass


#  takes a Dictionary as attribute from the inputhandler and converts it into an IPNetwork Objekt and returns it
    def convertToNetwork(self, data):
        ipNetwork = IPNetwork(data['networkaddress'])
        ipNetwork.netmask = data['subnetmask']
        return ipNetwork

