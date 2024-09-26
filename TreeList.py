class TreeList:
    def __init__(self, TreeGroup):
        self.root = TreeGroup

    def union(self, TreeList):
        TreeList.getRoot().setFather(self.root)
        TreeList.getRoot().setTree(self)
        return self
    def getRoot(self):
        return self.root
    #fai come osservazione che la findset riporta la struttura dati più che il rappresentante
