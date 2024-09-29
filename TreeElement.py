from TreeForest import TreeForest

class TreeElement:
    def __init__(self, value):
        self.value = value
        self.father = None
        self.treeForest = None

    def makeset(self):
        self.treeForest = TreeForest(self)
        self.father = self
       # print("treeForest: ", self.treeForest) per vedere la creazione
    def findset(self):
        if self.treeForest != self.father.treeForest:
            self.father.treeForest = self.father.findset()
        return self.father.treeForest

    def getValue(self):
        return self.value

    def getTreeForest(self):
       return self.treeForest

    def setTreeForest(self, treeForest):
        self.treeForest = treeForest

    def getFather(self):
        return self.father

    def setFather(self, father):
        self.father = father
