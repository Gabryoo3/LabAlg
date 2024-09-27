import ConnectedComponents
import ListGroup
import time
import math
import Plot
from TreeGroup import TreeGroup

timeChainNoHeuristics = []
timeChainHeuristics = []
timeTree = []
n = []

#Lista concatenata senza euristica
for i in range(3,17) :
    numElement = (int)(math.pow(2, i))
    n.append(numElement)
    groups = []
    for j in range(numElement):
        groups.append(ListGroup.ListGroup(j, False))
    startLinkNE = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    endLinkNE = time.time()
    timeChainNoHeuristics.append(round(endLinkNE-startLinkNE, 4))
    #print("LinkListNoEuristic: ", endLinkNE-startLinkNE)
    groups.clear()
    for j in range(numElement):
        groups.append(ListGroup.ListGroup(j, True))
    startLinkE = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    endLinkE = time.time()

    timeChainHeuristics.append(round(endLinkE-startLinkE,4))
    #print("LinkListNoEuristic: ", endLinkE-startLinkE)
    groups.clear()
    for j in range(numElement):
        groups.append(TreeGroup(j))
    startTree = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    endTree = time.time()
    timeTree.append(round(endTree-startTree,4))
    #print("Tree: ", endTree-startTree)
    groups.clear()

print("TimeChainWithNoHeuristics: ",timeChainNoHeuristics)
print("TimeChainWithHeuristics: ",timeChainHeuristics)
print("TimeTree: ",timeTree)

plt = Plot.Plot(timeChainNoHeuristics, timeChainHeuristics, timeTree, n)
plt.plotChainNoHeuristics()
plt.plotChainHeuristics()
plt.plotTree()
plt.plotAll()







