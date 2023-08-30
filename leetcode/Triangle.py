class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * i for i in range(1, len(triangle) + 1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(dp)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][0]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        print(dp)
        return min(dp[len(triangle)-1])
