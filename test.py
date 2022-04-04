import math

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

    # TODO - test this
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
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None


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


        # todo - delete this is copy pasted
        # node = Node(end, weight)
        # node.next = self.graph[start]
        # self.graph[start] = node
        #
        # # Adding the source node to the destination as
        # # it is the undirected graph
        # node = Node(start, weight)
        # node.next = self.graph[end]
        # self.graph[end] = node

    # Function to print the graph TODO DELETE THIS IS COPIED AND PASTED
    def print_graph(self):
        for i in range(self.vertex_count):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.value), end="")
                temp = temp.next
            print(" \n")


    def prims_min_spaning(self):
        heap = Heap()

        max_keys = [0,0] +  [math.inf] * (self.vertex_count-1)

        heap.heap(max_keys, self.vertex_count)


        heap.decrease_key(1, 0)



        #TODO -wtf this variable doing?
        history = [math.inf] * (self.vertex_count+1)
        # history[0] = 0
        # history[1] = 0

        min_spanning = []

        while heap.min_key() != math.inf:
            min_weighted_node = Node(heap.min_id(), heap.min_key())
            heap.delete_min()

            min_spanning.append(min_weighted_node)


            current = self.graph[min_weighted_node.value]
            # loop through all adjecent vertexes
            while current.next != None:
                next = current.next

                if heap.in_heap(next.value) and next.weight > min_weighted_node.weight - next.weight:
                    # history[next.value] = next.weight
                    # min_spanning[next.value] = next

                    heap.decrease_key(next.value, next.weight)

                current = next

            # heap.delete_min()

        print("history", history)
        print("min", min_spanning)


        # try to sum
        count = 0
        for x in min_spanning:
            if x != -1:
                count += x.weight

        print("weight", count)






class Reader:
    def __init__(self, path):
        print("aaa", path)
        with open(path) as f:
            print("f",f)
            lines = f.readlines()

            vertex_count = int(lines[0])

            self.graph = Graph(vertex_count)
            print("count", vertex_count)

            for x in range(1, len(lines)):
                line = lines[x]

                # parse the line
                parts = line.split()

                i = int(parts[0])
                j = int(parts[1])
                w = int(parts[2])


                self.graph.add_edge(i, j, w)


            f.close()



# p = Heap()
# p.heap([50,20,43,11,7,5], 6)
# print(p.min_key())
# p.decrease_key(6, 2)
# print(p.min_key())mes

# print(p.delete_min())
# print(p.min_key())

reader = Reader("/Users/mdanics/Documents/School/3340/assignment3/mst_graph_medium.txt")
reader.graph.prims_min_spaning()