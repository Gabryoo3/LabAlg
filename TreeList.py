class TreeList:
    def __init__(self, TreeGroup):
        self.root = TreeGroup

    def union(self, TreeList):
        TreeList.getRoot().father = self.root
        return self
    def getRoot(self):
        return self.root
