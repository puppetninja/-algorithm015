class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        r, c, max_side = len(matrix), len(matrix[0]), 0
        dp = [[0 for _ in range(c+1)] for _ in range(r+1)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j]) + 1
                    max_side = max(max_side, dp[i+1][j+1])

        return max_side * max_side
