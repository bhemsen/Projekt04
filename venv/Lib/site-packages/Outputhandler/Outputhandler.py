import sys
class Outputhandler: 
    def __init__(self) -> None:
        pass

# all write methods take a dict and create/edit a file und write content 
    def writeToFile(self, data):
        file = open(data['name'], 'x')
        file.write(data['content'])
        file.close()

    def overwriteToFile(self, data):
        file = open(data['name'], 'w')
        file.write(data['content'])
        file.close()

    def appendToFile(self, data):
        file = open(data['name'],'a')
        file.write(data['content'])
        file.close()