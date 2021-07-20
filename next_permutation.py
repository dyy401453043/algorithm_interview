# leetcode 31, 寻找下一个排列（字典序）

# Algorithm:
# Find largest index i such that array[i] < array[i+1]. (If no such i exists, then this is already the last permutation.)
# Find largest index j such that j > i and array[j] > array[i].
# Swap array[j] and array[i − 1].
# Reverse the suffix starting at array[i].

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i , j):
            while i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

        length = len(nums)
        if length == 0 or length == 1:
            return nums
        for i in range(length-2, -1, -1):
            if i == 0 and nums[i] >= nums[i+1]:
                reverse(nums, i, length-1)
                break
            if nums[i] >= nums[i + 1]:
                continue
            else:
                for j in range(length-1,i,-1):
                    if nums[j] > nums[i]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
                if length-1 > i+1:
                    reverse(nums, i+1 , length-1)
                break
