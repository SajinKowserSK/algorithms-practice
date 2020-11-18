class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        output = 0
        if not matrix:
            return output

        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                # we need to do the above mention dp step only if we find "1" in the matrix
                if matrix[r][c] == "1":
                    # The reason why we are updating r+1 and c+1 is because while making the dp matrix,
                    # there is 1 extra column and 1 extra row to offset the boundaries
                    # You can avoid this by putting a few if conditions, but this is more cleaner and readable
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1

                    output = max(output, dp[r + 1][c + 1])

        return output * output