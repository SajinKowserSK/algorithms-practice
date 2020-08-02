from models import *

def dfsTarget(graph, target):
    for node in graph.nodes:
        if node.state == "unvisited" and dfsVisit(node, graph, target):
            return True

    return False


def dfsVisit(node, graph, target):
    node.state = "visiting"

    if node.data == target:
        return True

    neighbors = graph.adjList[node]
    # print('neighbors is ' + str(neighbors))

    for neighbor in neighbors:
        if neighbor.state == "unvisited" and dfsVisit(neighbor, graph, target):
            return True

    node.state = "visited"
    return False






first = Vertex(1)
sec = Vertex(2)
third = Vertex(3)
fourth = Vertex(4)
fifth = Vertex(5)
sixth = Vertex(6)

lst = [first, sec, third, fourth, fifth, sixth]
testGraph = Graph(lst, isDirected=True)
# testGraph.showList()

testGraph.addEdge(first, sec)
testGraph.addEdge(first, third)
testGraph.addEdge(sec, fourth)
testGraph.addEdge(fourth, sixth)
testGraph.addEdge(third, fourth)
testGraph.addEdge(third, fifth)
testGraph.addEdge(fifth, sixth)

# testGraph.showList()
# print('next')
# print(testGraph.adjList)

for x in range(0, 8):
    print(dfsTarget(testGraph, x))
    testGraph.reset()