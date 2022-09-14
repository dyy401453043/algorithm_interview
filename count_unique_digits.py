# leetcode 357, dp递归统计各位数字不相同的数字总数
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # dp[i] 表示结果总数, dp[i]-dp[i-1]表示纯i位数的结果总数
        # 递推的思路，以纯i-1位数的结果总数作为前i-1位，则最小位有11-i种选择
        # 即纯i位数的结果数量等于纯i-1位的结果数量*(11-i)
        if n==0:
            return 1
        if n==1:
            return 10
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2,n+1):
            dp[i] = (dp[i-1]-dp[i-2])*(11-i) + dp[i-1]
        return dp[n]
