# leetcode 12, 罗马数字转换，简单模拟题
class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        result = ''
        if num in hashmap:
            return hashmap[num]
        for k in hashmap.keys():
            mod = int(num / k)
            result += mod*hashmap[k]
            num = num - k*mod
        return result
