class TreeForest:
    def __init__(self, TreeElement):
       self.root = TreeElement
       self.rank = 0

    def union(self, TreeForest):
        if self.rank > TreeForest.getRank():
           TreeForest.getRoot().setFather(self.root)
        else:
            self.root.setFather(TreeForest.getRoot())
            if self.rank == TreeForest.getRank():
                TreeForest.setRank(TreeForest.getRank() + 1)

    def getRoot(self):
        return self.root

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank

