# leetcode 16，找到数组中和最接近target的三个元素，双指针化n^3为n^2
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) <= 3:
            return sum(nums)
        gap = float('inf')
        result = None
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j != k:
                if nums[j] + nums[k] > target - nums[i]:
                    res = nums[j] + nums[k] + nums[i] - target
                    if res < gap:
                        gap = res 
                        result = nums[j] + nums[k] + nums[i]
                    k -= 1
                elif nums[j] + nums[k] < target - nums[i]:
                    res = target - nums[j] - nums[k] - nums[i]
                    if res < gap:
                        gap = res
                        result = nums[j] + nums[k] + nums[i]
                    j += 1
                else:
                    return target
        return result
