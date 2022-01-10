
# DIRECTED GRAPH
from _collections import deque
from _collections import defaultdict
def is_scheduling_possible(tasks, prerequisites):

  # start by creating res for storage
  # adjList for nbr tracking
  # inbounds to see how many point to this node
  # source nodes will be how many have NO Inbounds
  res = []
  adjList= defaultdict(list)
  inbounds = defaultdict(int)
  sources = deque()

  for  x in range(0, tasks):
      adjList[x] = []

# u points to v with directed arrow
  for u, v in prerequisites:
      adjList[u].append(v)

      # increase inbounds
      inbounds[v] += 1

# check if the task has any inbounds
# if not, then it is a SOURCE
  for x in range(0, tasks):
      if inbounds[x] == 0:
          sources.append(x)

# while sources is not empty
# pop then process from queue
# remove inbounds from neighbors
# check if any nbr is now a source and append ot q
  while sources:
      popped = sources.popleft()
      res.append(popped)
      neighbors = adjList[popped]

      for nbr in neighbors:
          inbounds[nbr] -= 1
          if inbounds[nbr] == 0:
              sources.append(nbr)

# if the length of res is same as tasks then all can be completed
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
