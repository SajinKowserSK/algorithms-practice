from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
  result = []
  for elem in ropeLengths:
      heappush(result, elem)

  cost = 0
  while len(result) > 1:

      sum = heappop(result) + heappop(result)
      cost += sum

      heappush(result, sum)

  return cost


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()

