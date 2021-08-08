class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        adjList = self.adjlist(wordList)

        return self.bfs(beginWord, endWord, adjList)

    def adjlist(self, wordList):
        adjList = {}

        for word in wordList:

            for x in range(0, len(word)):

                tmp = word[:x] + "*" + word[x + 1:]

                if tmp not in adjList:
                    adjList[tmp] = []

                adjList[tmp].append(word)

        return adjList

    def bfs(self, start, end, adjList):
        q = []  # need q as [(word, level)]
        q.append((start, 1))
        seen = set()

        while q:
            popped = q.pop(0)
            depth = popped[1]
            curr_word = popped[0]

            seen.add(curr_word)

            for x in range(0, len(curr_word)):
                tmp = curr_word[:x] + "*" + curr_word[x + 1:]

                if tmp in adjList:

                    nbrs = adjList[tmp]

                    for nbr in nbrs:
                        if nbr not in seen:
                            q.append(tuple([nbr, depth + 1]))

                        if nbr == end:
                            return depth + 1

        return 0
