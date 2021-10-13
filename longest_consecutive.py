# leetcode 128, 找到数组中最长的连续数字，hash降低复杂度，前驱后继
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        max_count = 1
        for num in nums:
            if num-1 in nums:
                continue
            else:
                count = 1
                temp = num + 1
                while temp in nums:
                    count += 1
                    temp += 1
                max_count = max(max_count, count)
        return max_count
