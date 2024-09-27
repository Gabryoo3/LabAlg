from TreeList import TreeList

class TreeGroup:
    def __init__(self, element):
        self.element = element
        self.father = None
        self.TreeList = None


    def makeset(self) -> TreeList:
        self.TreeList = TreeList(self)
       # print("TreeList: ", self.TreeList)
        return self.TreeList #più che ritornare il rappresentante, ritorna l'intera struttura dati
    def findset(self):
        return self.TreeList
    def getElement(self):
        return self.element
    def setTree(self, tree):
        self.TreeList = tree
    def getFather(self):
        return self.father
    def setFather(self, father):
        self.father = father