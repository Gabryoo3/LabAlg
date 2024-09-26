import ConnectedComponents
import ListGroup
import ChainList
import time
import random
import math
import plot
from TreeGroup import TreeGroup

timeChainNoEuristic = []
timeChainEuristic =[]
timeTree = []
n = []

#Lista concatenata senza euristica
for i in range(3,15) :
    numElement = (int)(math.pow(2, i))
    n.append(numElement)
    groups = []
    for j in range(numElement):
        groups.append(ListGroup.ListGroup(j, False))
    startLinkNE = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    endLinkNE = time.time()
    timeChainNoEuristic.append(round(endLinkNE-startLinkNE, 4))
    #print("LinkListNoEuristic: ", endLinkNE-startLinkNE)
    groups.clear()
    for j in range(numElement):
        groups.append(ListGroup.ListGroup(j, True))
    startLinkE = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    endLinkE = time.time()

    timeChainEuristic.append(round(endLinkE-startLinkE,4))
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

print("TimeChainWithNoEuristic: ",timeChainNoEuristic)
print("TimeChainWithEuristic: ",timeChainEuristic)
print("TimeTree: ",timeTree)

plt = plot.plot(timeChainNoEuristic, timeChainEuristic, timeTree, n)
plt.plotChainNoEuristic()
plt.plotChainEuristic()
plt.plotTree()
plt.plotAll()







