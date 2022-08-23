# 判断扰乱字符串，三个变量dp，用dp记忆化搜索O(n^4)来代替递归O(2^n)
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def is_disturb(s1, s2):
            length1, length2 = len(s1), len(s2)
            dp = [[[False] * (length1+1) for i in range(length2)] for j in range(length1)] # i_idx, j_idx, length
            l = 1
            for i in range(length1):
                for j in range(length2):
                    if s1[i] == s2[j]:
                        dp[i][j][l] = True
            for l in range(2, length1+1):
                for i in range(length1):
                    for j in range(length2):
                        if i+l > length1 or j+l > length2:
                            continue
                        dp[i][j][l] = any(dp[i][j][k] and dp[i+k][j+k][l-k] for k in range(1, l)) \
                            or any(dp[i][j+l-k][k] and dp[i+k][j][l-k] for k in range(1, l))
            return dp[0][0][length1]
        return is_disturb(s1, s2)
