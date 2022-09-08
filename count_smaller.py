# leetcode 315, 计算以每一个元素为左侧的逆序，归并加记录原始位置
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        index = [i for i in range(length)]
        ans = [0] * length

        def mergesort(l, r):
            nonlocal ans
            nonlocal index
            if l == r:
                return
            temp, p, temp_index = [0]*(r-l+1), 0, [i for i in range(l, r+1)]
            mid = (l+r) // 2
            mergesort(l, mid)
            mergesort(mid+1, r)
            i, j = l, mid+1
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp[p]=nums[i]
                    temp_index[p] = index[i]
                    ans[temp_index[p]] += j-mid-1
                    p += 1
                    i += 1
                elif nums[i] > nums[j]:
                    temp[p] = nums[j]
                    temp_index[p] = index[j]
                    p += 1
                    j += 1
            while i <= mid:
                temp[p]=nums[i]
                temp_index[p] = index[i]
                ans[temp_index[p]] += j-mid-1
                p += 1
                i += 1
            while j <= r:
                temp[p] = nums[j]
                temp_index[p] = index[j]
                p += 1
                j += 1
            for i in range(l, r+1):
                nums[i] = temp[i-l]
                index[i] = temp_index[i-l]
            # print(nums, index, ans)
        
        mergesort(0, length-1)
        return ans
