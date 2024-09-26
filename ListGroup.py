from ChainList import ChainList


class ListGroup:
    def __init__(self, element, euristic):
        self.element = element
        self.next = None
        self.chainList = None
        self.euristic = euristic

    def makeset(self) -> ChainList:
        self.chainList = ChainList(self, self.euristic)
        #print("ChainList: ", self.chainList)
        return self.chainList

    def findset(self):
        return self.chainList

    def getElement(self):
        return self.element

    def getChainList(self):
        return self.chainList
    def setChainList(self, chainList):
        self.chainList = chainList



