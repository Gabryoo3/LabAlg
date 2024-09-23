import ChainList

class ListGroup:
    def __init__(self, element, euristic):
        self.element = element
        self.next = None
        self.ChainList: ChainList = None
        self.euristic = euristic

    def makeset(self) -> ChainList:
        self.ChainList = ChainList(self,self,self.euristic)
        return self.ChainList

    def findset(self):
        return self.ChainList.head
    def getElement(self):
        return self.element
    def setList(self, ChainList):
        self.ChainList = ChainList
    def getGroup(self):
        return self
    def __call__(self):
        self.makeset()



