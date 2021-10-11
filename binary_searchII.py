# leetcode 81，二分查找旋转数组II，简洁，不用递归
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
