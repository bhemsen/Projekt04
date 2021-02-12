from inputhandler.Inputhandler import Inputhandler
from _MySQL.Database import Database
from IPConverter.Converter import *
from Networks.Network import Network
from Outputhandler.Outputhandler import Outputhandler
from netaddr import * 
import os.path
import mysql.connector
import pprint
import time

# connect to a database with an Object of the class Database
db = Database('localhost','webadmin','password','projekt04')

# Create cbjekt from importet classes
inputhandler = Inputhandler()
converter = Converter()

userInput = inputhandler.handleNewNetwork()

# Convert the Inputstring into an IPNetwork Object
ipNetwork = converter.convertToNetwork(userInput)
networks = Network().createSubnets(userInput, ipNetwork)

# for every created network connect IP to PC
keys = networks.keys()

for key in keys:
    abteilung = input('Abteilung: ')
    fileName = db.addNetworks(key,abteilung)
    print(key)
    networkID = db.getNetworkID(IPNetwork(key).network,abteilung)
    inputhandler.connectIPtoPC(networks[key],networkID, fileName)


