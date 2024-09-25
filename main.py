import ConnectedComponents
import ListGroup
import ChainList
import time
import random
import matplotlib.pyplot as plt

from TreeGroup import TreeGroup

n = [20, 50, 100, 200, 500]
timeChainNoEuristic = []
timeChainEuristic =[]
timeTree = []


#Lista concatenata senza euristica
for i in n:
    groups = []
    for j in range(i):
        groups.append(ListGroup.ListGroup(j, False))
    start = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    end = time.time()
    timeChainNoEuristic.append(end-start)
    groups.clear()
    for j in range(i):
        groups.append(ListGroup.ListGroup(j, True))
    start = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    end = time.time()
    timeChainEuristic.append(end-start)
    groups.clear()
    for j in range(i):
        groups.append(TreeGroup(j))
    start = time.time()
    ConnectedComponents.ConnectedComponents(groups).connected()
    end = time.time()
    timeTree.append(end-start)
    groups.clear()








