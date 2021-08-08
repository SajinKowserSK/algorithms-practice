from collections import *

def canFinish(numCourses, prerequisites):
    adjList = defaultdict(list)

    for course, pre in prerequisites:
        adjList[pre].append(course)

    def cycle(node, tracker):
        tracker[node] = True
        for n in adjList[node]:
            if n in tracker or cycle(n, tracker):
                return True

        tracker.pop(node)
        return False

    for x in range(numCourses):
        print()
        tracker = {}
        if cycle(x, tracker):
            return False


    return True




