from netaddr import * 

 
class Network:
    def __init__(self) -> None:
        pass

# take an IPNetwork object and the data dictionary the get the Suffix for subnets
# returns a dict containig the created subnets with a list of their ip's 
    def createSubnets(self, data, ipNetwork):
        subnets = list(ipNetwork.subnet(data['subnet']))
        networkList = {}
        for subnet in subnets:
            networkList[str(subnet)] = list(subnet)
        return networkList



