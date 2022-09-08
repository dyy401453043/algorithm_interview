# leetcode 312 戳气球，开区间dp，遍历最后一个被戳的气球
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [[0]*(length+2) for i in range(length+2)]
        for l in range(2, length+2):
            for i in range(-1, length+1):
                j = i + l
                if j > length:
                    continue
                for k in range(i+1, j):
                    before = 1 if i < 0 else nums[i]
                    after = 1 if j >= length else nums[j]
                    if dp[i][k]+before*nums[k]*after+dp[k][j] > dp[i][j]:
                        dp[i][j] = dp[i][k]+before*nums[k]*after+dp[k][j]
        return dp[-1][length]
