class TreeForest:
    def __init__(self, TreeElement):
       self.root = TreeElement

    def union(self, TreeForest):
        TreeForest.getRoot().setFather(self.root)
        TreeForest.getRoot().setTreeForest(self)
    def getRoot(self):
        return self.root
