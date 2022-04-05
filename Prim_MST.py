import sys
import collections
import math
from heap import Heap

class GraphNode:
    def __init__(self, nodeVal=None, nodeWeight=None):
        self.val = nodeVal
        self.weight = nodeWeight
        self.next = None
        self.prev = None

    def getWeight(self):
        return self.weight

    def getVal(self):
        return self.val

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setNext(self, nextNode):
        self.next = nextNode

    def setPrev(self, prevNode):
        self.prev = prevNode


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * (self.vertices + 1)

    def updateGraph(self, idx, node):
        self.graph[idx] = node

    def getGraphNode(self, idx):
        return self.graph[idx]

    def addEdge(self, source, destination, weight):
        # creating source and destination nodes
        src = GraphNode(source, weight)
        dst = GraphNode(destination, weight)

        # updating graph's representation with the connections
        src.setNext(self.graph[destination])
        dst.setNext(self.graph[source])
        self.updateGraph(source, dst)
        self.updateGraph(destination, src)


    def adj_list_print(self):
        print("THE ADJACENCY LIST REPRESENTATION OF GRAPH IN FORMAT (DESTINATION, WEIGHT): ")
        for v in range(self.vertices):
            adjacents = []
            currNode = self.getGraphNode(v)
            while currNode is not None:
                adjacents.append(currNode)
                currNode = currNode.getNext()

            for x in range(0, len(adjacents)):
                adjacents[x] = (adjacents[x].val, adjacents[x].weight)

            print("Vertex " + str(v) + " Adjacencies ->" + str(adjacents))

    def P_MST(self):
        firstVal = [0]
        remaining = (self.vertices - 1) * [math.inf]
        minHeap = Heap(firstVal + remaining, self.vertices)
        minSTree = []

        for x in range(0, self.vertices+1):
            minSTree.append(GraphNode())

        minHeap.decrease_key(1, 0)
        min_key = minHeap.min_key()

        while min_key < math.inf:
            lowest_weight_node = GraphNode(minHeap.min_id(), minHeap.min_key())
            minHeap.delete_min()

            currNode = self.graph[lowest_weight_node.val]
            while currNode.next is not None:
                successor = currNode.next
                if minHeap.in_heap(successor.val):
                    if (minHeap.key(successor.val) <= successor.weight):
                        currNode = successor
                        continue

                    else:
                        minHeap.decrease_key(successor.val, successor.weight)
                        minSTree[successor.val].prev = lowest_weight_node.val
                        minSTree[successor.val].weight = successor.weight

                currNode = successor
            min_key = minHeap.min_key()

        print("\n")
        print("\n")
        print("PRINTING EDGES OF MST: ")


        total = 0
        for x in range(0, self.vertices+1):
            if minSTree[x].getPrev() is not None:
                print("\t Parent: " + str(minSTree[x].getPrev()) + "\t Child: "
                      + str(x) + "\t Weight: " + str(minSTree[x].getWeight()))
                total = total + minSTree[x].getWeight()

        print("\n")

        print("THE WEIGHT OF THE MST IS: ", total)

def main():
    lines = []
    filename = sys.argv[1]

    with open(filename) as f:
        lines = f.readlines()

    for x in range(0, len(lines)):
        lines[x] = lines[x].strip()

    graph = Graph(int(lines[0]))

    for idx in range(1, len(lines)):
        currLine = lines[idx]
        split = currLine.split()
        src, dst, weight = int(split[0]), int(split[1]), int(split[2])
        graph.addEdge(src, dst, weight)

    graph.adj_list_print()
    graph.P_MST()

main()















