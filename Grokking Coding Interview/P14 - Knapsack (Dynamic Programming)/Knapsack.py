def solve_knapsack(profits, weights, capacity):
    dp = []
    for x in range(len(profits)):
        row = []
        for y in range(capacity+1):
            row.append(-1)

        dp.append(row)


    return solve_recursively(dp, profits, weights, capacity, 0)


def solve_recursively(dp, profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0:
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + solve_recursively(dp, profits, weights, capacity - weights[index], index + 1)

    profit2 = solve_recursively(dp, profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()

