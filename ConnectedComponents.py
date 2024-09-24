class ConnectedComponents:
    def __init__(self, groups):
        self.groups = groups
        self.size = len(groups)
        self.lists = []

    def connected(self):
        for i in range (0, self.size):
            self.groups[i].makeset() #salva le liste/alberi creati
        for i in range (0, self.size):
            for j in range (i+1, self.size):
                if self.groups[i].get
                    self.lists[i].union(self.lists[j].findset())






0