# leetcode 115，串1有多少个子序列等于串2，dp
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dfs超时 51/64
        # count = 0
        # def dfs(idx, cur):
        #     nonlocal count
        #     if cur == '':
        #         count += 1
        #         return
        #     if idx == len(s):
        #         return            
        #     if s[idx] == cur[0]:
        #         dfs(idx+1, cur[1:])
        #     dfs(idx+1, cur)
        # dfs(0, t)
        # return count

        # dp
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for i in range(m+1)]
        # for j in range(n+1):
        #     dp[0][j] = 0
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    dp[i+1][j+1] = dp[i][j+1] # 不激活 i
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i][j] # 不激活i和激活i两种情况
        return dp[m][n]
