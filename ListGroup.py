from ChainList import ChainList


class ListGroup:
    def __init__(self, element, euristic):
        self.element = element
        self.next = None
        self.chainList: ChainList = None
        self.euristic = euristic

    def makeset(self) -> ChainList:
        self.chainList = ChainList(self, self.euristic)
        return self.chainList

    def findset(self):
        return self.chainList.head

    def getElement(self):
        return self.element

    def getGroup(self):
        return self



