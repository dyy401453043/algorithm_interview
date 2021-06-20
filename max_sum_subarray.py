# 牛客网 NC19 最大子数组和，动态规划
class Solution:
    def maxsumofSubarray(self , arr):
        # write code here
        dp = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0:
                dp[i] = arr[0]
            else:
                dp[i] = max(dp[i-1] + arr[i], arr[i])
        return max(dp)
