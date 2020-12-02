def power_grid(num, connections):
    pmap = {}
    output = []
    for node1, node2, cost in connections:
        pmap[node1] = node1
        pmap[node2] = node2

    # now we have a parent map where every node's parent is themselves
    # we create find_parent function to get every node's component parent

    def find_parent(node):
        parent = pmap[node]
        while node != parent:
            node = parent
            parent = pmap[parent]

        return parent # component's parent

    connections.sort(key = lambda connection: connection[2])
    # now we have connections in ascending order

    for node1, node2, cost in connections:
        node1_parent = find_parent(node1)
        node2_parent = find_parent(node2)

        if node1_parent != node2_parent: # different components
            # we have to connect them by adding edge between their parents
            pmap[node2_parent] = node1_parent
            output.append([node1, node2, cost])

    return output

print(power_grid(5, [
    ["A", "B", 1],
    ["B", "C", 4],
    ["B", "D", 6],
    ["D", "E", 5],
    ["C", "E", 1]
]))