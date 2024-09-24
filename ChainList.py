import ListGroup

class ChainList:
    def __init__(self, ListGroup,euristic):
        self.head = ListGroup
        self.tail = ListGroup
        self.size = 1
        self.euristic = euristic
    def union(self, ChainList):
        if self.size < ChainList.getSize() & self.euristic == True:
            ChainList.setSize(ChainList.getSize() + self.size)
            i = self.head
            while i is not None:
                i.setList(ChainList)
                i = i.next
            self.head = ChainList.getTail().next
            ChainList.setTail(self.tail)
            return ChainList
        else:
            self.size += ChainList.getSize()
            i = ChainList.getHead()
            while i is not None:
                i.setList(self)
                i = i.next
            self.tail.next = ChainList.getHead()
            self.tail = ChainList.getTail()
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



