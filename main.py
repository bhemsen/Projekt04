from inputhandler.inputhandler import Inputhandler
from _MySQL.database import Database
from IPConverter.ConvertInputToNetwork import ConvertInputToNetwork
from Networks.Network import Network
from Outputhandler.Outputhandler import Outputhandler
from netaddr import * 
import os.path
import mysql.connector
import pprint
import time

db = Database('localhost','webadmin','password','projekt04')

inputhandler = Inputhandler()

userInput = inputhandler.handleNewNetwork()

ipNetwork = ConvertInputToNetwork().convertToNetwork(userInput)

networks = Network().createSubnets(userInput, ipNetwork)

pp = pprint.PrettyPrinter(indent=4)

# for every created network connect IP to PC

keys = networks.keys()

for key in keys:
    abteilung = input('Abteilung: ')
    fileName = db.addNetworks(key,abteilung)
    print(key)
    networkID = db.getNetworkID(IPNetwork(key).network,abteilung)
    inputhandler.connectIPtoPC(networks[key],networkID, fileName)


