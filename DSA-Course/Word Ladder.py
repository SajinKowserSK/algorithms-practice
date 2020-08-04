from helpers import *

def createAdjlist(wordList):

    adj = {}
    for w in wordList:
        for i in range(0, len(w)):
            key = w[:i] + "*" + w[i+1:]
            if key not in adj:
                adj[key] = []

            adj[key].append(w)

    return adj


def bfs(start, end, adjlist):
    q = []
    q.append((start,1))
    visited = set()

    while len(q) > 0:
        curr = q.pop(0)
        word = curr[0]
        dst = curr[1]
        visited.add(word)

        for i in range (0, len(word)):
            key = word[:i] + "*" + word[i+1:]

            if key in adjlist:

                for neighbor in adjlist[key]:
                    if neighbor == end:
                        return dst + 1

                    if neighbor not in visited:
                        q.append((neighbor, dst + 1))

    return 0


def wordLadder(start, end, wordList):

    if start == end:
        return 0


    adjlist = createAdjlist(wordList)
    return bfs(start, end, adjlist)


testList = ['hit', 'dot', 'hot', 'dog', 'cog', 'log', 'lot']
testStart = 'hit'
testEnd = 'cog'


print(wordLadder(testStart, testEnd, testList))