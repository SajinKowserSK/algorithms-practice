'''
This class is used to process the input file graph, print adjacency list and then print the min, spanning tree along
with its total weight.
SM Shahariar (Sajin) Kowser | 251014520
'''

import sys
import collections
import math
from heap import Heap

# Graph node class used to represent nodes in an undirected graph
# Value is the node / vertex name
# Weight is the weight of the edge it connects with next to
# Next is the node its connecting to
class GraphNode:
    def __init__(self, nodeVal=None, nodeWeight=None):
        self.val = nodeVal
        self.weight = nodeWeight
        self.next = None

    def getWeight(self):
        return self.weight

    def getVal(self):
        return self.val

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode

# MST node class, very similiar to above GraphNode class but has a prev instance var
# which is used to represent the parent
class MSTNode:
    def __init__(self, nodeVal=None, nodeWeight=None):
        self.val = nodeVal
        self.weight = nodeWeight
        self.prev = None

    def getWeight(self):
        return self.weight

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getVal(self):
        return self.val

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev

# Graph class which intializes an array representation of all the nodes in
# the graph
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
        # for all the nodes
        for v in range(self.vertices):
            adjacents = []
            currNode = self.getGraphNode(v)

            # collect all the adjacent nodes
            while currNode is not None:
                adjacents.append(currNode)
                currNode = currNode.getNext()

            # change representation of adjacent nodes to (value, weight)
            for x in range(0, len(adjacents)):
                adjacents[x] = (adjacents[x].val, adjacents[x].weight)

            # print all the adjacent nodes
            print("Node " + str(v) + " Adjacencies :" + str(adjacents))

    def P_MST(self):

        # initialize array representation of min. spanning tree
        firstVal = [0]
        remaining = (self.vertices - 1) * [math.inf]
        minHeap = Heap(firstVal + remaining, self.vertices)
        minSTree = []
        for x in range(0, self.vertices+1):
            minSTree.append(MSTNode())

        minHeap.decrease_key(1, 0)
        min_key = minHeap.min_key()

        # get the min key, make an MST node out of it and delete it
        while min_key < math.inf:
            lowest_weight_node = MSTNode(minHeap.min_id(), minHeap.min_key())
            minHeap.delete_min()

            # get the node from the graph
            currNode = self.graph[lowest_weight_node.val]
            while currNode.getNext() is not None:
                successor = currNode.getNext()


                # take successor node if and only if the successor's value is leq the weight
                if minHeap.in_heap(successor.getVal()):
                    if minHeap.key(successor.getVal()) <= successor.getWeight():
                        currNode = successor
                        continue

                    else:
                        minHeap.decrease_key(successor.val, successor.weight)
                        minSTree[successor.getVal()].setPrev(lowest_weight_node.getVal())
                        minSTree[successor.getVal()].setWeight(successor.getWeight())

                currNode = successor
            min_key = minHeap.min_key()

        print("\n")
        print("\n")
        print("PRINTING EDGES OF MST IN FORMAT (I, J): W: ")


        total = 0 # weight counter for the mst
        for x in range(0, self.vertices+1):
            if minSTree[x].getPrev() is not None:
                i = minSTree[x].getPrev()
                j = x
                weight = minSTree[x].getWeight()


                print("\t (" +str(i) +", " +str(j)+"): " + "\t"+str(weight))
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
    # takes # of vertices from first line and intializes graph
    graph = Graph(int(lines[0]))

    # splits each line into i, j, w and creates necessary edges
    for idx in range(1, len(lines)):
        currLine = lines[idx]
        split = currLine.split()
        src, dst, weight = int(split[0]), int(split[1]), int(split[2])
        graph.addEdge(src, dst, weight)

    # prints adj list and MST with weight
    graph.adj_list_print()
    graph.P_MST()

main()















