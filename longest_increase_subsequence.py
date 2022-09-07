# leetcode300 最长递增子序列，维护所有长度的子序列的尾值&二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        m = [nums[0]]

        for i in range(1, length):
            l, r = 0, len(m)-1
            while l <= r:
                mid = (l+r) // 2
                if m[mid] >= nums[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            if r+1 < len(m) and nums[i] < m[r+1]:
                m[r+1] = nums[i]
            elif r+1 == len(m):
                m.append(nums[i])

        return len(m)
