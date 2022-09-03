# leetcode 221 01矩阵中的最大正方形，dp存储以i,j为右下角的最大边长
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        for i in range(M):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for j in range(N):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i][j] != '0' else 0
        res = 0
        for i in range(M):
            for j in range(N):
                if (dp[i][j])*(dp[i][j]) > res:
                    res = (dp[i][j])*(dp[i][j])
        return res
