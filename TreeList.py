class TreeList:
    def __init__(self, TreeGroup):
        self.root = TreeGroup

    def union(self, TreeList):
        #TreeList.getRoot().setTree(self)
        #TreeList.getRoot().setFather(self.root)
        TreeList.setRoot(self.root)
        return self
    def getRoot(self):
        return self.root
    def setRoot(self, root):
        self.root = root
    #fai come osservazione che la findset riporta la struttura dati più che il rappresentante
