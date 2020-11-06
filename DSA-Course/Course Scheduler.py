from models import *

first = Vertex(1)
sec = Vertex(2)
third = Vertex(3)
fourth = Vertex(4)
fifth = Vertex(5)
lst = [first, sec, third, fourth, fifth]
testGraph = Graph(lst, isDirected=True)


testGraph.addEdge(first, fourth)
testGraph.addEdge(first, sec)
testGraph.addEdge(sec, fourth)
testGraph.addEdge(sec, third)
testGraph.addEdge(sec, fifth)
testGraph.addEdge(third, fifth)



testGraph.dfsPrint(first)

def topSort(root):
    master = []
    stack = []
    stack.insert(0, root)
    master.append(root)
    seen = set()

    while stack:
        popped = stack.pop(0)

        if popped not in seen:
            seen.add(popped)

        for neighbor in popped.neighbors:
            if neighbor not in seen:
                stack.insert(0, neighbor)
                master.append(neighbor)

    return master

test = topSort(first)
for x in range (0, len(test)):
    test[x] = test[x].data

print(test)


