import ConnectedComponents
import ListElement
import time
import math
import Plot
import sys
from TreeElement import TreeElement
sys.setrecursionlimit(int(math.pow(10,6)))
timeChainNoHeuristics = []
timeChainHeuristics = []
timeTree = []
n = []


#Lista concatenata senza euristica
for i in range(1,15):
    numElement = (int)(math.pow(2, i))
    n.append(numElement)
    elements = []
    for j in range(numElement):
        elements.append(ListElement.ListElement(j, False))
    startLinkNE = time.time()
    ConnectedComponents.ConnectedComponents(elements).connected()
    endLinkNE = time.time()
    timeChainNoHeuristics.append(round(endLinkNE-startLinkNE, 3))
    #print("LinkListNoEuristic: ", endLinkNE-startLinkNE)
    elements.clear()
    #Lista concatenata con euristica
    for j in range(numElement):
        elements.append(ListElement.ListElement(j, True))
    startLinkE = time.time()
    ConnectedComponents.ConnectedComponents(elements).connected()
    endLinkE = time.time()
    timeChainHeuristics.append(round(endLinkE-startLinkE,3))
    #print("LinkListNoEuristic: ", endLinkE-startLinkE)
    elements.clear()
    #Foresta di insiemi disgiunti
    for j in range(numElement):
        elements.append(TreeElement(j))
    startTree = time.time()
    ConnectedComponents.ConnectedComponents(elements).connected()
    endTree = time.time()
    timeTree.append(round(endTree-startTree,3))
    #print("Tree: ", endTree-startTree)
    elements.clear()
#Debug per vedere i tempi di esecuzione
print("TimeChainWithNoHeuristics: ",timeChainNoHeuristics)
print("TimeChainWithHeuristics: ",timeChainHeuristics)
print("TimeTree: ",timeTree)

plt = Plot.Plot(timeChainNoHeuristics, timeChainHeuristics, timeTree, n)
plt.plotChainNoHeuristics()
plt.plotChainHeuristics()
plt.plotTree()
plt.plotAll()







