from netaddr import *
from _MySQL.Database import Database

class Inputhandler:

    def handleIPv4(self, inputString):
        return IPAddress(inputString).ipv4()
 
    def handleIPv6(self, inputString):
        return IPAddress(inputString).ipv6()

    def handleNetmask(self, inputString):
        nm = IPNetwork('0.0.0.0').netmask = inputString
        return nm


    def convertHostCountToSuffix(self, hostCount):
        if (hostCount <= 2):
            return 30
        if (hostCount <= 6):
            return 29
        if (hostCount <= 14):
            return 28
        if (hostCount <= 30):
            return 27
        if (hostCount <= 62):
            return 26
        if (hostCount <= 126):
            return 25
        if (hostCount <= 254):
            return 24
        if (hostCount <= 510):
            return 23
        if (hostCount <= 1022):
            return 22
        if (hostCount <= 2046):
            return 21
        if (hostCount <= 4094):
            return 20
        if (hostCount <= 8190):
            return 19
        if (hostCount <= 16382):
            return 18
        if (hostCount <= 32766):
            return 17
        if (hostCount <= 65534):
            return 16
        if (hostCount <= 1048574):
            return 12
        if (hostCount <= 16777214):
            return 8
        if (hostCount <= 268435454):
            return 4

# takes Userinput paste it into an Dictionary and returns it
    def handleNewNetwork(self, networkadress, subnetmask, hostCount):
        self.networkadress = str(networkadress)
        self.subnetmask = str(subnetmask)
        self.hostCount = int(hostCount)

        
        data = {}
        data['networkaddress'] = self.networkadress
        data['subnetmask'] = self.subnetmask

        #check how many hosts should be in the subnet and convert it into a Suffix
        data['subnet'] = self.convertHostCountToSuffix(self.hostCount)
        return data

# connect a IP address to a PC 
    def connectIPtoPC(self, listOfIPs,networkID,abteilung):
        # get an Instance of Database to directly safe the input
        db = Database('localhost','webadmin','password','projekt04')
        # for every subnet save the pc-ip assignment
        for i in range(1,len(listOfIPs)-1):
            ip = str(listOfIPs[i])
            pc = input('PC für '+ip+ ' = ')
            db.addressAssignment(ip, pc, networkID, abteilung)



    

