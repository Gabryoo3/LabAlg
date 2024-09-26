import matplotlib.pyplot as plt


class plot:
    def __init__(self, timeChainNoEuristic, timeChainEuristic, timeTree, n):
        self.timeChainNoEuristic = timeChainNoEuristic
        self.timeChainEuristic = timeChainEuristic
        self.timeTree = timeTree
        self.n = n

    def plotAll(self):
        plt.plot(self.n, self.timeChainNoEuristic, label='timeChainNoEuristic')
        plt.plot(self.n, self.timeChainEuristic, label='timeChainEuristic')
        plt.plot(self.n, self.timeTree, label='timeTree')
        plt.xlabel('Numero di elementi')
        plt.ylabel('Tempo esecuzione')
        plt.legend()
        plt.show()
        plt.savefig('allPlots.png')
    def plotChainNoEuristic(self):
        plt.plot(self.n, self.timeChainNoEuristic, label='Catena senza euristica')
        plt.xlabel('Numero di elementi')
        plt.ylabel('Tempo esecuzione')
        plt.title("Tempo di esecuzione per la lista concatenata senza euristica")
        plt.legend()
        plt.show()
        plt.savefig('ChainNoEuristic.png')
    def plotChainEuristic(self):
        plt.plot(self.n, self.timeChainEuristic, label='Catena con euristica')
        plt.xlabel('Numero di elementi')
        plt.ylabel('Tempo esecuzione')
        plt.title("Tempo di esecuzione per la lista concatenata con euristica")
        plt.legend()
        plt.show()
        plt.savefig('ChainEuristic.png')
    def plotTree(self):
        plt.plot(self.n, self.timeTree, label='Albero con compressione')
        plt.xlabel('Numero di elementi')
        plt.ylabel('Tempo esecuzione')
        plt.title("Tempo di esecuzione per la lista albero")
        plt.legend()
        plt.show()
        plt.savefig('Tree.png')