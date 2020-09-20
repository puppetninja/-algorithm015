class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0: return 0
        r = len(grid)
        c = len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        count = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, visited, i, j)
                    count += 1

        return count

    def dfs(self, grid, visited, i, j):
        r = len(grid)
        c = len(grid[0])
        if i < 0 or i >= r or j < 0 or j >= c or visited[i][j] or grid[i][j] == '0':
            return

        visited[i][j] = True
        self.dfs(grid, visited, i+1, j)
        self.dfs(grid, visited, i-1, j)
        self.dfs(grid, visited, i, j - 1)
        self.dfs(grid, visited, i, j + 1)
