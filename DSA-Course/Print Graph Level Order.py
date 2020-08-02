from models import *

def levelPrint(root):
    if root is None:
        return None

    root.state = "visiting"
    q = []
    qNext = []
    q.append(root)

    currlvl = 0


    while len(q) > 0:

        current = q.pop(0)
        print(current.data)


        for neighbor in current.neighbors:
            if neighbor.state == "unvisited":
                qNext.append(neighbor)
                neighbor.state = "visiting"

        current.state = "visited"

        if len(q) == 0:
            print("\n")
            q = qNext
            qNext = []


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


# print(firstN)
levelPrint(first)