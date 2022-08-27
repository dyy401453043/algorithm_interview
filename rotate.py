# leetcode 189, 可用三次reverse操作，O(1)空间实现rotate
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums,i,j):
            l, r = i, j
            temp = 0
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l+=1
                r-=1
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        k = k % length
        reverse(nums,0,length-1)
        reverse(nums,0,k-1)
        reverse(nums,k,length-1)
