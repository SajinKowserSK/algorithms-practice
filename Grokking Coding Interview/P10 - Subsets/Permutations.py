def find_permutations(nums):
  result = []
  chars = len(nums)
  permutations = [[]]

  for num in nums:
      n = len(permutations)
      for _ in range(n):
          popped = permutations.pop(0)

          for j in range(len(popped)+1): # +1 to reference adding to end
              toAdd = popped.copy()

              toAdd.insert(j, num)

              if len(toAdd) == chars:
                  result.append(toAdd)

              else:
                  permutations.append(toAdd)
  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
