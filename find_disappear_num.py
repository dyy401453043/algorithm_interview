# leetcode448,找到数组中消失的数字,空间复杂度O(1),这种O(1)的题还是很考验思维的
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            num = nums[i] % n
            nums[num-1] += n
        result = []
        for i in range(n):
            if nums[i] <= n:
                result.append(i+1)
        return result