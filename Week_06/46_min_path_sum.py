class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        r, c = len(grid), len(grid[0])
        dp = [[0]*c for _ in range(r)]
        dp[0][0] = grid[0][0]

        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[r-1][c-1]
