import mysql.connector
from netaddr import *
from mysql.connector import Error
import sys
import os.path
from Outputhandler.Outputhandler import Outputhandler


class Database: 
    def __init__(self,host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.output = Outputhandler()
        self.data = {}

        self.mydb = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database
        )

        self.cursor = self.mydb.cursor(prepared=True)


    def getAbteilungen(self):
        sql = "SELECT ID, Abteilung FROM abteilungen"
        data = []

        self.cursor.execute(sql)

        result = self.cursor.fetchall()

        for row in result:
            row = list(row)
            data.append(row)
            
        print (data)
        return data

    
    def addNetworks(self, network, abteilung):
        ip= IPNetwork(network)
        sql = "INSERT INTO `netze` (`ID`, `netzadresse`, `broadcastadresse`, `subnetzmaske`, `abteilung`) VALUES (NULL, %s, %s, %s, %s)"

        # create a file for the network

        self.data['name'] = 'Abteilung_'+abteilung
        self.data['content'] = '#\n# IP-Adresszuordung für das Netz '+ abteilung+'\n#\n'
        isInvalid = True
       
        if(os.path.exists(self.data['name'])):
             while(isInvalid):
                userInput = str(input('Datei existiert bereits! Überschreiben? (J/N): ')).upper()
                if(userInput == 'J'):
                    self.output.overwriteToFile(self.data)
                    isInvalid = False
                    
                elif(userInput == 'N'):
                    self.data['name'] = str(input('Dateiname: '))
                    print(self.data)
                    self.output.writeToFile(self.data)
                    isInvalid = False

                    
        else:
            self.output.writeToFile(self.data)
        
        try:
            self.cursor.execute(sql, (str(ip.network), str(ip.broadcast), str(ip.netmask), str(abteilung)), True)
            self.mydb.commit()
            return self.data['name']


        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.mydb.rollback()
            sys.exit()



    def getNetworkID(self, ipAddress, abteilung):
        data = []
        sql = "SELECT ID FROM netze WHERE netzadresse = %s AND abteilung = %s"

        try:
            self.cursor.execute(sql, (str(ipAddress),str(abteilung)))

            result = self.cursor.fetchone()
            return result[0]

        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            
            self.mydb.rollback()
            sys.exit()
        

    
    def addressAssignment(self, ipAddress, pc, networkID, fileName):
        sql = "INSERT INTO `adresszuordnung` (`ID`, `hostadresse`, `pc`, `netz`) VALUES (NULL, %s, %s, %s);"

        self.data['content'] = ipAddress +"    "+ pc+'\n'

        # before writing to the database write to file
        self.data['name'] = fileName
        self.output.appendToFile(self.data) 

        try:
            self.cursor.execute(sql, (str(ipAddress), str(pc), str(networkID)), True)
            self.mydb.commit()

        except mysql.connector.Error as error:
            print('Jeder PC kann nur einer Hostadresse zugeordnet werden')
            print("parameterized query failed {}".format(error))
            
            self.mydb.rollback()
            sys.exit()



    def deleteIPAssignment(self, hostaddress, pc):
        sql = "DELETE FROM `adresszuordnung` WHERE hostadresse = %s AND pc = %s;"

        try:
            self.cursor.execute(sql, (hostaddress, pc))
            self.mydb.commit()

        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.mydb.rollback()



    def deleteNetwork(self, networkaddress, abteilung):
        sql = "DELETE FROM netze WHERE netzadresse = %s AND abteilung = %s;"

        try:
            self.cursor.execute(sql, (networkaddress, abteilung))
            self.mydb.commit()

        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.mydb.rollback()
