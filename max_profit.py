# leetcode 121 找到数组最小值和其后的最大值，目标使差值最大，做法是维护两个变量，最小和最大，O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value,max_value=0,0
        result = {}
        profit = 0
        for i,value in enumerate(prices):
            if i==0: # ensure max_value >= min_value
                min_value,max_value = value,value
                result[min_value] = max_value
            else:
                if value > max_value:
                    max_value = value
                    result[min_value] = max_value
                    if max_value - min_value > profit:
                        profit = max_value - min_value
                elif value < min_value:
                    min_value, max_value = value,value
                else:
                    continue
        print(result)
        return profit
