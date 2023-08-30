class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = int(grid[-1][-1] != 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i == m-1 and j == n-1) or grid[i][j] == 1:
                    continue
                elif i == m-1:
                    dp[i][j] = dp[i][j+1]
                elif j == n-1:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        print(dp)
        return dp[0][0]