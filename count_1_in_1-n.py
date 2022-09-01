# leetcode 233, 用min,max可以减少一些条件判断
class Solution:
    def countDigitOne(self, n: int) -> int:
# 1 10 11 12 13 14 15 16 17 18 19 21 31 41 51 ... 91 100 101 102

# 个位 1， 1 11 21 31  [n//10] + 1 个位大于等于 1 else [n//10]
# 十位 1,  10-19 110-119 210-219 ([n//100]+1) * 10 十位大于等于2 等于1看各位 十位等于0 ([n//100]) * 10
# 百位 1， 100-199 1100-99 2100-2199 ([n//1000]+1)*100 百位大于等于2 百位等于1 看十位和个位 等于0 [n//1000]*100

# [//10] * 1 + %10 >= 2 1 ,1 %1+1, 0 0
# [//100] * 10 + %100 >= 20 10 10-19 %10+1 0-9 0
# [//1000] * 100 + %1000 >= 200 100 100-199 %100+1 0-99 0
        res = 0
        # prev_b = 0
        for exp in range(1,11):
            divisor = 10 ** exp
            a, b = n // divisor, n % divisor
            c = divisor // 10
            # if b >= 2*c:
            #     res += a * c + c
            # elif c <= b < 2*c:
            #     res += a * c + prev_b+1
            # else:
            #     res += a * c
            res += a * c + min(max(b-c+1,0),c)
            # prev_b = b
        return res
