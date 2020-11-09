class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):

                if grid[x][y] == "1":
                    count += self.dfs(x, y, grid)

        print(grid)
        return count

    def dfs(self, x, y, grid):
        if x >= len(grid) or x < 0 or y >= len(grid[x]) or y < 0:
            return 0

        if grid[x][y] == "1":
            grid[x][y] = "0"

            self.dfs(x + 1, y, grid)
            self.dfs(x - 1, y, grid)
            self.dfs(x, y + 1, grid)
            self.dfs(x, y - 1, grid)

            return 1


