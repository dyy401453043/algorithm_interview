# leetcode 327, 统计区间和在某个范围内的个数，前缀和 & 归并 & 两个有序数组差值
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        res = 0

        presums = []
        for num in nums:
            if len(presums) == 0:
                presums.append(num)
            else:
                presums.append(presums[-1]+num)

        def mergesort(arr, l, r):
            nonlocal res
            if l == r:
                if lower <= arr[l] <= upper:
                    res += 1
                return
            else:
                mid = (l+r) // 2
                mergesort(arr, l, mid)
                mergesort(arr, mid+1,r)

                i,j,k = l,mid+1,mid+1
                for i in range(l, mid+1):
                    while j <= r and arr[j] - arr[i] < lower:
                        j += 1
                    while k <= r and arr[k] - arr[i] <= upper:
                        k += 1
                    res += k - j
                    
                i,j,temp=l,mid+1,[]
                while i <= mid and j <= r:
                    if arr[j] > arr[i]:
                        temp.append(arr[i])
                        i += 1
                    elif arr[j] < arr[i]:
                        temp.append(arr[j])
                        j += 1
                    else:
                        temp.append(arr[i])
                        temp.append(arr[j])
                        i += 1
                        j += 1
                while i <= mid:
                    temp.append(arr[i])
                    i += 1
                while j <= r:
                    temp.append(arr[j])
                    j += 1
                for k in range(l, r+1):
                    arr[k] = temp[k-l]
        mergesort(presums, 0, length-1)
        return res
