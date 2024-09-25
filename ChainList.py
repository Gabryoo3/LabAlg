import ListGroup

class ChainList:
    def __init__(self, li:ListGroup,euristic):
        self.head = li
        self.tail = li
        self.size = 1
        self.euristic = euristic
    def union(self, chainList):
        if (self.size < chainList.getSize()) and (self.euristic == True): #caso con euristica
            print("Euristica")
            chainList.setSize(chainList.getSize() + self.size)
            i = self.head
            while i is not None:
                i.setChainList(chainList)
                i = i.next
            self.head = chainList.getTail().next
            chainList.setTail(self.tail)
            return chainList
        #caso senza euristica
        else:
            print("No Euristica")
            self.size += chainList.getSize()
            i = chainList.getHead()
            while i is not None:
                i.setChainList(self)
                i = i.next
            self.tail.next = chainList.getHead()
            self.tail = chainList.getTail()
            return self

    def getHead(self):
        return self.head
    def getTail(self) -> ListGroup:
        return self.tail
    def getSize(self):
        return self.size
    def setHead(self, chainList):
        self.head = chainList.getHead()
    def setTail(self, chainList):
        self.tail = chainList.getTail()
    def setSize(self, chainList):
        self.size = chainList.getSize()
    def print(self):
        i = self.head
        while i is not None:
            print(i.getElement())
            i = i.next



