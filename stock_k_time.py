# leetcode 188, 买股票不超过k次，3个变量的dp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k==0:
            return 0
        def max_profit(arr, k):
            length = len(arr)
            # 初始化为不持有
            dp = [[[-float('inf'), -float('inf')] for j in range(k+1)] for i in range(length+1)]

            dp[0][0][0] = 0

            for i in range(1,length+1): # i 代表 天数
                for j in range(k+1): # j 代表完成交易 次数
                    dp[i][j][0] = max(dp[i-1][j-1][1]+arr[i-1], dp[i-1][j][0]) if j > 0 else dp[i-1][j][0]
                    dp[i][j][1] = max(dp[i-1][j][0]-arr[i-1], dp[i-1][j][1])
        
            # print([[dp[i][j][0] for j in range(k+1)] for i in range(length+1)])
            # print([[dp[i][j][1] for j in range(k+1)] for i in range(length+1)])
            return max(dp[length][j][0] for j in range(k+1))
        return max_profit(prices, k)
