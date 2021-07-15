# leetcode 29，用加减法实现除法，每次将除数倍增，实现一个reduce操作
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1 : # 负数比正数多一个，有一个实例会越界
            return 2147483647
        def reduce(dividend, divisor): # require dividend > 0, divisor > 0, dividend >= divisor
            old_divisor, count = None, 0 # count 始终表示 old_divisor/ori_divisor
            while dividend >= divisor:
                old_divisor = divisor
                count = 1 if count == 0 else count + count
                divisor = divisor + divisor
            return dividend - old_divisor, count
        if dividend == 0:
            return 0
        elif dividend > 0 and divisor < 0:
            return - self.divide(dividend, -divisor)
        elif dividend < 0 and divisor > 0:
            return - self.divide(-dividend, divisor)
        elif dividend < 0 and divisor < 0:
            return self.divide(-dividend, -divisor)
        else:
            result = 0
            while dividend >= divisor:
                dividend, count = reduce(dividend, divisor)
                result += count
            return result
