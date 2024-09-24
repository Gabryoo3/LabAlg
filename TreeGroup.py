from TreeList import TreeList

class TreeGroup:
    def __init__(self, element):
        self.element = element
        self.father = None
        self.TreeList = None


    def makeset(self, treeGroup) -> TreeList:
        self.TreeList = TreeList(treeGroup)
        return self.TreeList
    def findset(self):
        return self.TreeList.root
    def getElement(self):
        return self.element
    def getGroup(self):
        return self