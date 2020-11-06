def restore(arr):
    adj = {}

    final = []
    for pair in arr:
        first = pair[0]
        second = pair[1]

        adj[first] = []
        adj[second] = []

    for pair in arr:
        first = pair[0]
        second = pair[1]

        adj[first].append(second)
        adj[second].append(first)

    first = None
    seen = set()

    for key in adj:
        if len(adj[key]) == 1:
            first = key
            break

    final.append(first)
    q = final.copy()
    seen.add(first)

    while q:
        popped = q.pop(0)
        if popped not in seen:
            seen.add(popped)
            final.append(popped)

        next = adj[popped]
        for num in next:
            if num not in seen:
                q.append(num)

    print(final)




print(restore([[1,2], [2,3], [3,4]]))


