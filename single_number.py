# leetcode 137, 找到数列中仅出现一次的元素（其余元素均出现三次），位运算
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum(num >> i & 1 for num in nums) % 3
            if total != 0:
                if i != 31:
                    ans += total << i
                else:
                    ans -= total << i
        return ans
