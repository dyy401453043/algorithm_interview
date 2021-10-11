# leetcode 97，检测两个串能否交错组成第三个串，dp记录前i个和前j个能否组成前i+j个的bool
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dfs 会超时
        # def dfs(temp1, temp2, temp3):
        #     if temp1 == '' and temp2 == '' and temp3 =='':
        #         return True
        #     condition1, condition2 = False, False
        #     if len(temp1) > 0 and len(temp3) > 0 and temp1[0] == temp3[0]:
        #         condition1 = dfs(temp1[1:], temp2, temp3[1:])
        #     if len(temp2) > 0 and len(temp3) > 0 and temp2[0] == temp3[0]:
        #         condition2 = dfs(temp1, temp2[1:], temp3[1:])
        #     return condition1 or cis_interleave.pyondition2
        # return dfs(s1, s2, s3)

        # dp
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for i in range(m+1)]
        for i in range(0,m+1):
            dp[i][0] = s1[:i] == s3[:i]
        for j in range(0,n+1):
            dp[0][j] = s2[:j] == s3[:j]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = (dp[i+1][j] and s2[j] == s3[i+j+1]) or (dp[i][j+1] and s1[i] == s3[i+j+1])
        return dp[m][n]
