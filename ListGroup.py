from ChainList import ChainList


class ListGroup:
    def __init__(self, element, euristic):
        self.element = element
        self.next = None
        self.ChainList: ChainList = None
        self.euristic = euristic

    def makeset(self, listgroup) -> ChainList:
        self.ChainList = ChainList(listgroup, self.euristic)
        return self.ChainList

    def findset(self):
        return self.ChainList.head

    def getElement(self):
        return self.element

    def setList(self, chainList):
        self.ChainList = chainList

    def getGroup(self):
        return self



