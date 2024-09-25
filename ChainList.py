from itertools import chain

import ListGroup

class ChainList:
    def __init__(self, li:ListGroup,euristic):
        self.head = li
        self.tail = li
        self.size = 1
        self.euristic = euristic
    def union(self, chain_list):
        if (self.size < chain_list.getSize()) and (self.euristic == True): #caso con euristica
            print("Euristica")
            chain_list.setSize(chain_list.getSize() + self.size)
            i = self.head
            while i is not None:
                i.setChainList(chain_list)
                i = i.next
            chain_list.getTail().next = self.head

            self.head = chain_list.getHead()
            chain_list.setTail(self.tail)
            return chain_list
        #caso senza euristica
        else:
            print("No Euristica")
            self.size += chain_list.getSize()
            i = chain_list.getHead()
            while i is not None:
                i.setChainList(self)
                i = i.next
            self.tail.next = chain_list.getHead()

            chain_list.setHead(self.head)
            self.tail = chain_list.getTail()

            return self

    def getHead(self):
        return self.head
    def getTail(self) -> ListGroup:
        return self.tail
    def getSize(self):
        return self.size
    def setHead(self, head):
        self.head = head
    def setTail(self, tail):
        self.tail = tail
    def setSize(self, value):
        self.size = value
    def print(self):
        i = self.head
        while i is not None:
            print(i.getElement())
            i = i.next




