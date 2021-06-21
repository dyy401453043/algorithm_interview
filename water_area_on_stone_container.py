# 牛客网 NC128 直方图形状的石头容器上能盛多少水，双指针
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self , arr ):
        # write code here
        # 中 小 小 大 -> 2个 中减去小的水
        water = 0
        left,right = 0,len(arr)-1
        left_value,right_value = arr[left],arr[right]
        while left < right:
            if left_value <= right_value:
                left += 1
                if arr[left] <= left_value:
                    water += left_value - arr[left]
                else:
                    left_value = arr[left]
            else:
                right -= 1
                if arr[right] <= right_value:
                    water += right_value - arr[right]
                else:
                    right_value = arr[right]
        assert left == right
        return water
