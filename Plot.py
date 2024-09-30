import matplotlib.pyplot as plt


class Plot:
    def __init__(self, timeChainNoHeuristics, timeChainHeuristics, timeTree, n):
        self.timeChainNoHeuristics = timeChainNoHeuristics
        self.timeChainHeuristics = timeChainHeuristics
        self.timeTree = timeTree
        self.n = n

    def plotAll(self):
        plt.plot(self.n, self.timeChainNoHeuristics, label='Lista senza euristica')
        plt.plot(self.n, self.timeChainHeuristics, label='Lista con euristica')
        plt.plot(self.n, self.timeTree, label='Foresta con compressione')
        plt.xlabel('Numero di FIND-SET')
        plt.ylabel('Tempo esecuzione(s)')
        plt.title("Esecuzione complessiva")
        plt.legend()
        plt.savefig('plotAll.png')
        plt.show()
    def plotChainNoHeuristics(self):
        plt.plot(self.n, self.timeChainNoHeuristics, label='Lista senza euristica')
        plt.xlabel('Numero di FIND-SET')
        plt.ylabel('Tempo esecuzione(s)')
        plt.title("Esecuzione della lista concatenata senza euristica")
        plt.legend()
        plt.savefig('plotChainNoHeuristics.png')
        plt.show()
    def plotChainHeuristics(self):
        plt.plot(self.n, self.timeChainHeuristics, label='Lista con euristica')
        plt.xlabel('Numero di FIND-SET')
        plt.ylabel('Tempo esecuzione(s)')
        plt.title("Esecuzione della lista concatenata con euristica")
        plt.legend()
        plt.savefig('plotChainHeuristics.png')
        plt.show()
    def plotTree(self):
        plt.plot(self.n, self.timeTree, label='Albero con compressione')
        plt.xlabel('Numero di FIND-SET')
        plt.ylabel('Tempo esecuzione(s)')
        plt.title("Esecuzione della foresta con compressione")
        plt.legend()
        plt.savefig('plotTree.png')
        plt.show()