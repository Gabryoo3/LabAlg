import ListGroup

class ChainList:
    def __init__(self, ListGroup,euristic):
        self.head = ListGroup
        self.tail = ListGroup
        self.size = 1
    def union(self, ChainList):
        if self.size < ChainList.getSize() & self.euristic == True:
            ChainList.setSize(ChainList.getSize() + self.size)
            self.head = ChainList.getTail().next
            ChainList.setTail(self.tail)
            while self.tail != None:
                self.tail.getGroup().setList(ChainList)
                self.tail = self.tail.next
            return ChainList
        else:
            self.size += ChainList.getSize()
            self.tail.next = ChainList.getHead()
            self.tail = ChainList.getTail()
            while ChainList.getTail() != None:
                ChainList.getTail().getGroup().setList(self)
                ChainList.setTail(ChainList.getTail().next)
            return self
    def getHead(self):
        return self.head
    def getTail(self) -> ListGroup:
        return self.tail
    def getSize(self):
        return self.size
    def setHead(self, ChainList):
        self.head = ChainList.getHead()
    def setTail(self, ChainList):
        self.tail = ChainList.getTail()
    def setSize(self, ChainList):
        self.size = ChainList.getSize()



