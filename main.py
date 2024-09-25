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
    ListGroupNoEuristicList = []
    TreeGroupList = []
    for j in range(i):
        ListGroupNoEuristicList.append(ListGroup.ListGroup(j, False))
    start = time.time()
    ConnectedComponents.ConnectedComponents(ListGroupNoEuristicList).connected()
    end = time.time()
    timeChainNoEuristic.append(end-start)



