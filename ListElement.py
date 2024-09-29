from ChainList import ChainList


class ListElement:
    def __init__(self, value, heuristics):
        self.value = value
        self.next = None
        self.chainList = None
        self.heuristics = heuristics

    def makeset(self):
        self.chainList = ChainList(self, self.heuristics)
        #print("ChainList: ", self.chainList)

    def findset(self):
        return self.chainList

    def getValue(self):
        return self.value

    def setChainList(self, chainList):
        self.chainList = chainList



