from _collections import deque
from _collections import defaultdict
def is_scheduling_possible(tasks, prerequisites):
  res = []
  adjList= defaultdict(list)
  inbounds = defaultdict(int)
  sources = deque()

  for  x in range(0, tasks):
      adjList[x] = []

  for u, v in prerequisites:
      adjList[u].append(v)
      inbounds[v] += 1


  for x in range(0, tasks):
      if inbounds[x] == 0:
          sources.append(x)

  while sources:
      popped = sources.popleft()
      res.append(popped)
      neighbors = adjList[popped]

      for nbr in neighbors:
          inbounds[nbr] -= 1
          if inbounds[nbr] == 0:
              sources.append(nbr)

  if len(res) == tasks:
      return True

  return False


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
