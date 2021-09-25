# leetcode 41，找到数组中缺失的第一个正数，原地哈希
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > length:
                nums[i] = 0
        # ori_data : 0(place holder), 1, ..., length
        # after_encryption: length+1(place holder), length+2, ..., 2*length+1
        for num in nums:
            if num >= length + 1:
                num = num - length - 1
            if num == 0:
                continue
            # encrypte the num_th item of the nums
            if nums[num-1] >= length + 1:
                continue
            else:
                nums[num-1] += length + 1
        for i in range(length):
            if nums[i] >= length + 1:
                continue
            # the num_th item is not encryted, meaning num is not in the original nums.
            else:
                return i+1
        return length+1
