def can_partition(num, sum):
  dp = []
  for x in range(len(num)):
      row = []
      for y in range(sum+1):
          row.append(-1)

      dp.append(row)

  if helper(dp, num, sum, 0) == 1:
      return True


  return False

def helper(dp, num, sum, i):
    if i >= len(num) or sum < 0:
        return 0

    if sum == 0:
        return 1


    if dp[i][sum] == -1: # sub problem not yet solved
        if num[i] <= sum:
            if helper(dp, num, sum-num[i], i+1) == 1:
                dp[i][sum] = 1
                return 1

    dp[i][sum] = helper(dp, num, sum, i+1)





def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()

