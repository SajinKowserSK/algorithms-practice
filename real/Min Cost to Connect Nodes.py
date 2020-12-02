# main takeaway: make map of component's parents then only add new edges if two node's parents aren't same
# Have to find the minimum cost
# have a map of node and it's parent node in it's connected component
# sort the edges by weight cost
# Only add edge if the two nodes have different parent nodes (they're NOT in same component)
# after adding edge, set node 2's parent to node 1's parent in the map AND increment the cost

# if the number of edges != number of nodes - 1 at the end of the algorithm, it is not possible

def min_cost(n, edges, newEdges):

    parentMap = {}
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]

        parentMap[node1] = node1
        parentMap[node2] = node2

    for edge in newEdges:
        node1 = edge[0]
        node2 = edge[1]

        parentMap[node1] = node1
        parentMap[node2] = node2

    def find_parent(node):
        parent = parentMap[node]
        while node != parent:
            node = parent
            parent = parentMap[parent]

        return parent

    numEdges = 0
    cost = 0

    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]

        node1_parent = find_parent(node1)
        node2_parent = find_parent(node2)

        if node1_parent != node2_parent:
            parentMap[node2_parent] = node1_parent
            numEdges += 1

    newEdges.sort(key = lambda edge: edge[2]) # sorts by cost ascending order

    for edge in newEdges:
        node1 = edge[0]
        node2 = edge[1]
        edge_cost = edge[2]

        node1_parent = find_parent(node1)
        node2_parent = find_parent(node2)

        if node1_parent != node2_parent: # only add edge if they are from diff components
            parentMap[node2_parent] = node1_parent # connect components by adding edge between node 2's parent and node1's parent
            numEdges += 1
            cost += edge_cost

    return cost



print(min_cost(n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))

