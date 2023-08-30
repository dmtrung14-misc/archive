class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                elif j == n-1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif i == m-1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        return dp[0][0]