from ChainList import ChainList


class ListGroup:
    def __init__(self, element, heuristics):
        self.element = element
        self.next = None
        self.chainList = None
        self.heuristics = heuristics

    def makeset(self) -> ChainList:
        self.chainList = ChainList(self, self.heuristics)
        #print("ChainList: ", self.chainList)
        return self.chainList

    def findset(self):
        return self.chainList

    def getElement(self):
        return self.element

    def setChainList(self, chainList):
        self.chainList = chainList



