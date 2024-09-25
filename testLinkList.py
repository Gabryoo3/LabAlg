import ListGroup
import ChainList


l1 = ListGroup.ListGroup(1, True)
l2 = ListGroup.ListGroup(2, True)
l3 = ListGroup.ListGroup(3, True)


c1:ChainList = l1.makeset()
c2:ChainList = l2.makeset()
c3:ChainList = l3.makeset()
if l1.findset() == l2.findset():
    print("l1 and l2 are in the same set")
else:
    print("l1 and l2 are not in the same set")
c1.union(c2)
if l1.findset() == l2.findset():
    print("l1 and l2 are in the same set")
else:
    print("l1 and l2 are not in the same set")
c1.print()
print("Size of c1: ", c1.getSize())
print("Size of c2: ", c2.getSize())
print("Size of c3: ", c3.getSize())
c3.union(c1)
c3.print()


