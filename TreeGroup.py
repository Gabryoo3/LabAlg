import TreeList

class TreeGroup:
    def __init__(self, element):
        self.element = element
        self.father = None
        self.TreeList = None


    def makeset(self):
        self.TreeList = self
        return TreeList(self)
    def findset(self):
        return self.TreeList.root
    def getElement(self):
        return self.element
    def getGroup(self):
        return self
    def setList(self, TreeGroup):
        self.TreeList = TreeGroup