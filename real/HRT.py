lass Graph:
    def __init__(self, Nodes, isDirected=False):
        self.nodes = Nodes
        self.adjList = {}
        self.isDirected = isDirected

        for node in self.nodes:
            self.adjList[node] = []

    def addVertex(self, node):
        self.adjList[node] = []

    def addEdge(self, u, v):
        if v not in self.adjList[u]:
            self.adjList[u].append(v)
            u.neighbors.append(v)

        if self.isDirected is not True and u not in self.adjList[v]:
            self.adjList[v].append(u)
            v.neighbors.append(u)


    def showList(self):
        for node in self.nodes:

            neighbors = self.adjList[node]
            neighborVals = []

            for x in range (0, len(neighbors)):
                neighborVals.append(neighbors[x].data)

            print(str(node.data) + "->" + str(neighborVals))
        print('\n')

    def degree(self, node):
        return len(self.adjList[node.data])

    def reset(self):
        for node in self.nodes:
            node.state = "unvisited"

    def dfsPrint(self, node):
        node.state = "visiting"
        print(node.data)
        neighbors = self.adjList[node]
        for neighbor in neighbors:
            if neighbor.state == "unvisited":
                self.dfsPrint(neighbor)

        node.state = "visited"

def dfsPrint(node):
    node.state = "visiting"
    print(node.data)
    neighbors = node.neighbors
    for neighbor in neighbors:
        if neighbor.state == "unvisited":
            dfsPrint(neighbor)

    node.state = "visited"

class Vertex:
    def __init__(self, data):
        self.data = data
        self.state = "unvisited"
        self.neighbors = []


def solution(N, A, B):


def getMax(k, matrix):
    visited = []
    count = [0]
    m = len(matrix)
    n = len(matrix[0])
    visited = []
    houses = []

    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 1:
                houses.append([i, j])

    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 0:
                checkPossibleHouses(i, j, k, houses, count)


    return count[0]



def checkPossibleHouses(x, y, k, houses, count):
    check = True
    for h in houses:
        houseX = h[0]
        houseY = h[1]

        if abs(x-houseX) + abs(y-houseY) > k:
            check = False
            break


    if check:
        count[0] += 1


matrix = [[0, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 0, 1, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 0]]


k = 4

print(getMax(4, matrix))