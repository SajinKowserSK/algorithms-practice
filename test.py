import math
import sys
class Heap:
    # element id = index, element key = array value
    def heap(self, keys, n):
        a = [math.inf] + keys
        h = [0] * (2 * n) # represents heap indicies

        for i in range(1, n+1):
            h[i + n -1] = i

        for i in reversed(range(1, n)):
            if a[h[2*i]] < a[h[2*i+1]]:
                h[i] = h[2*i]
            else:
                h[i] = h[2*i + 1]

        print("----")
        print(h)
        print(a)

        self.a = a
        self.h = h
        self.n = n

    def in_heap(self, id):
        return id in self.h

    def min_key(self):
        return self.a[self.min_id()]


    def min_id(self):
        return self.h[1]


    def key(self, id):
        return self.a[id]


    def delete_min(self):
        # self.n = self.n - 1

        self.a[0] = math.inf

        self.h[self.h[1] + self.n - 1] = 0

        v = self.a[self.h[1]]

        i = math.floor((self.h[1] + self.n - 1) / 2)

        while i >= 1:
            if self.a[self.h[i*2]] < self.a[self.h[i*2+1]]:
                self.h[i] = self.h[i*2]
            else:
                self.h[i] = self.h[2*i + 1]

            i = math.floor(i/2)


        return v


    def decrease_key(self, id, new_key):
        current_key = self.key(id)

        if current_key > new_key:
            self.a[id] = new_key
            # set the key of the element to the new key, as current key is greater than new_key aka new key is less than
            i = math.floor((id + self.n - 1) / 2)

            while i >= 1:
                if self.a[self.h[i*2]] < self.a[self.h[i*2+1]]:
                    self.h[i] = self.h[i*2]
                else:
                    self.h[i] = self.h[2*i + 1]

                i = math.floor(i/2)



class Node:
    def __init__(self, value=None, weight=None):
        self.value = value
        self.weight = weight
        self.next = None
        self.parent = None

class Graph:
    def __init__(self, vertex_count):
        self.graph = [None] * (vertex_count + 1) # todo read this from the file
        self.vertex_count = vertex_count

    def add_edge(self, start, end, weight):
        start_node = Node(start, weight)
        start_node.next = self.graph[end]

        end_node = Node(end, weight)
        end_node.next = self.graph[start]

        self.graph[start] = end_node
        self.graph[end] = start_node


    # Function to print the graph
    def print_adjencency_list(self):
        # loop through each vertex
        linebreak()
        print("Printing Graph in Adjecency List Format")
        for i in range(self.vertex_count):
            print(f"Vertex: {i}, is connected to nodes ", end="")
            current = self.graph[i]
            if current is not None:
                # current = current.next
                while current is not None:
                    print(f"| node: {current.value}, weight: {current.weight} ", end="")
                    current = current.next
                print("")
                print("")



    def prims_min_spaning(self):
        min_heap = Heap()

        max_keys = [0] +  [math.inf] * (self.vertex_count-1)
        min_heap.heap(max_keys, self.vertex_count)
        min_spanning_tree = [None] * (self.vertex_count + 1)


        for i in range(self.vertex_count + 1):
            min_spanning_tree[i] = Node()
            min_spanning_tree[i].parent = None

        min_heap.decrease_key(1, 0)

        while min_heap.min_key() != math.inf:
            min_weighted_node = Node(min_heap.min_id(), min_heap.min_key())
            min_heap.delete_min()


            current = self.graph[min_weighted_node.value]
            # loop through all adjecent vertexes
            while current.next != None:
                next = current.next
                if min_heap.in_heap(next.value):
                    if (min_heap.key(next.value) > next.weight):
                        min_heap.decrease_key(next.value, next.weight)
                        min_spanning_tree[next.value].parent = min_weighted_node.value
                        min_spanning_tree[next.value].weight = next.weight
                current = next


        # print results
        linebreak()
        print("Minimum Spanning Tree:")
        print(f"Format is: (i,j) w")
        weight = 0
        for i in range(self.vertex_count+1):
            if min_spanning_tree[i].parent != None:
                print(f"({min_spanning_tree[i].parent}, {i}) {min_spanning_tree[i].weight}")
                weight += min_spanning_tree[i].weight

        linebreak()
        print("Minimum Spanning Tree Weight: ", weight)

class Reader:
    def __init__(self, path):
        with open(path) as f:
            lines = f.readlines()

            vertex_count = int(lines[0])
            self.graph = Graph(vertex_count)

            for x in range(1, len(lines)):
                line = lines[x]

                # parse the line
                parts = line.split()

                i = int(parts[0])
                j = int(parts[1])
                w = int(parts[2])

                self.graph.add_edge(i, j, w)

            f.close()


def linebreak():
    print("=======================================================")
#
reader = Reader("/Users/sajinkowser/PycharmProjects/algorithms-practice/mst_graph_medium.txt")
reader.graph.print_adjencency_list()
reader.graph.prims_min_spaning()
#
# lines = []
# filename = sys.argv[1]
# with open(filename) as f:
#     lines = f.readlines()
#
# for x in range(0, len(lines)):
#     lines[x] = lines[x].strip()
#
# graph = Graph(int(lines[0]))
#
# for i in range(1, len(lines)):
#     currLine = lines[x]
#     split = currLine.split()
#     i = int(split[0])
#     j = int(split[1])
#     w = int(split[2])
#
#     graph.add_edge(i, j, w)
#
# graph.print_adjencency_list()
# graph.prims_min_spaning()
#




