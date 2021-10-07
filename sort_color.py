# leetcode 75，颜色排序，快排思想
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        single point
        ptr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, len(nums)):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        # double point
        # ptr1, ptr2 = 0, 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         nums[ptr2], nums[i] = nums[i], nums[ptr2]
        #         ptr2 += 1
        #     elif nums[i] == 0:
        #         nums[ptr1], nums[i] = nums[i], nums[ptr1]
        #         if ptr1 != ptr2:
        #             nums[ptr2], nums[i] = nums[i], nums[ptr2]
        #         ptr1 += 1
        #         ptr2 += 1
