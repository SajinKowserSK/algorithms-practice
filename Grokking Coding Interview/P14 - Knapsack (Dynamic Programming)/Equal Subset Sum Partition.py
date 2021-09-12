def can_partition(num):
  totalSum = sum(num)

  if totalSum % 2 != 0:
      return False

  totalSum = totalSum / 2
  totalSum = int(totalSum)

  # now if half of the array equals the total sum / 2 then the other half will also equal the same

  dp = []
  for x in range(len(num)):
      row = []
      for y in range(totalSum+1):
          row.append(-1)

      dp.append(row)

  if solve_recursively(dp, num, 0, totalSum) == 1:
      return True

  return False

def solve_recursively(dp, num, i, target):
    if i >= len(num) or target < 0:
        return 0


    if target == 0:
        return 1

    if dp[i][target] == -1:

        if num[i] <= target:
            if solve_recursively(dp, num, i+1, target-num[i]) == 1:
                dp[i][target] = 1
                return 1


    dp[i][target] = solve_recursively(dp, num, i+1, target)

    return dp[i][target]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
