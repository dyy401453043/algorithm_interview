# leetcode 264, 丑数, 三指针，正确性在于证明三指针的前身都是没有资格的（小于等于当前），三指针都是资格的（大于当前）
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        p1, p2, p3 = 0, 0, 0
        for i in range(1,n):
            candidate = [dp[p1]*2,dp[p2]*3,dp[p3]*5]
            dp[i] = min(candidate)
            if dp[i] == dp[p1]*2:
                p1+=1
            if dp[i] == dp[p2]*3:
                p2+=1
            if dp[i] == dp[p3]*5:
                p3+=1
        return dp[n-1]
