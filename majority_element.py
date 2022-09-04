# leetcode 229, 寻找超过n//3的元素，摩尔消去 & 后验证
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        vote1, vote2 = 0, 0
        for num in nums:
            if vote1 > 0 and num1 == num:
                vote1 += 1
            elif vote2 > 0 and num2 == num:
                vote2 += 1
            elif vote1 == 0:
                num1 = num
                vote1 = 1
            elif vote2 == 0:
                num2 = num
                vote2 = 1
            else:
                vote1 -=1
                vote2 -=1
        

        count1, count2 = 0, 0
        for num in nums:
            if num1 == num:
                count1 += 1
            if num2 == num:
                count2 += 1
        res = []
        if count1 > len(nums) // 3:
            res.append(num1)
        if count2 > len(nums) // 3 and num2 != num1:
            res.append(num2)
        return res
