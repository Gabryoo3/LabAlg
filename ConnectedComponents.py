import random

class ConnectedComponents:
    def __init__(self, groups):
        self.groups = groups
        self.size = len(groups)

    def connected(self):
        for i in range (0, self.size):
            self.groups[i].makeset() #salva le liste/alberi creati
        for i in range(0, self.size):
            j = random.randint(0, self.size-1)
            if self.groups[i].findset() != self.groups[j].findset():
                self.groups[i].findset().union(self.groups[j].findset())









