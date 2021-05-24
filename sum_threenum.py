# leetcode 15, 三数之和，注意i,j,k在移动过程中都要去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        result = []
        for i in range(length-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,length-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j+1<length and nums[j+1] == nums[j]:
                        j+=1
                    j+=1
                    while k-1>=0 and nums[k-1] == nums[k]:
                        k-=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    while k-1>=0 and nums[k-1] == nums[k]:
                        k-=1
                    k-=1
                else:
                    while j+1<length and nums[j+1] == nums[j]:
                        j+=1
                    j+=1
        return result
