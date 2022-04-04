from _collections import deque
def topological_sort(vertices, edges):
    sortedOrder = []
    adjList = {}
    inbound = {}

    for node in range(0, vertices):
        adjList[node] = []

    for key in adjList:
        inbound[key] = 0

    for start, destination in edges:
        adjList[start].append(destination)
        inbound[destination] += 1

    sources = deque()
    for key in inbound:
        if inbound[key] == 0:
            sources.append(key)

    while sources:
        popped = sources.popleft()
        neighbors = adjList[popped]
        for nbr in neighbors:
            # remove edges
            inbound[nbr] -= 1
            if inbound[nbr] == 0: # if they became a source
                sources.append(nbr)

        sortedOrder.append(popped)


    if len(sortedOrder) != vertices:
        return []

    return sortedOrder




def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
