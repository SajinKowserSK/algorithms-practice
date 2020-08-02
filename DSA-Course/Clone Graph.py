from models import *

def cloneGraph(root):
    if root is None:
        return None

    nodeMap = {}
    rootCopy = Vertex(root.data)
    nodeMap[root] = rootCopy
    dfsVisit(root, nodeMap)

    return rootCopy

def dfsVisit(root, nodeMap):
    root.state = "visiting"
    neighbors = root.neighbors

    for neighbor in neighbors:

        if neighbor not in nodeMap:
            nodeMap[neighbor] = Vertex(neighbor.data)

        neighborCopy = nodeMap[neighbor]
        rootCopy = nodeMap[root]
        rootCopy.neighbors.append(neighborCopy)


        if neighbor.state == "unvisited":
            dfsVisit(neighbor, nodeMap)


    root.state = "visited"






first = Vertex(1)
sec = Vertex(2)
third = Vertex(3)
fourth = Vertex(4)
fifth = Vertex(5)
sixth = Vertex(6)
lst = [first, sec, third, fourth, fifth, sixth]
testGraph = Graph(lst, isDirected=True)


testGraph.addEdge(first, sec)
testGraph.addEdge(first, third)
testGraph.addEdge(sec, fourth)
testGraph.addEdge(fourth, sixth)
testGraph.addEdge(third, fourth)
testGraph.addEdge(third, fifth)
testGraph.addEdge(fifth, sixth)

dfsPrint(first)
print("done first iter " + "\n")
testGraph.reset()
firstCopy = cloneGraph(first)
dfsPrint(firstCopy)

