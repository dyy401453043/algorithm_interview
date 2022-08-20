# leetcode 76 最小覆盖子串，双指针（滑动窗口），附带证明
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""
        target = {}
        for char in t:
            target[char] = target[char]+1 if char in target else 1
        def cover(temp):
            return all(key in temp and temp[key]>=target[key] for key in target)
        l, r, temp= 0, 0, {s[0]:1}
        res = s + '@'
        while r < len(s):
            if cover(temp):
                if len(res) > r-l+1: #左开右闭
                    res = s[l:r+1]
                temp[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r == len(s):
                    break
                temp[s[r]] = temp[s[r]] + 1 if s[r] in temp else 1
        if len(res) > len(s):
            return ""
        return res
# 尝试证明正确性
# 由于连续性 一定存在一个时刻 r == r_T。 此刻l有 （a）l <= l_T 和 （b）l > l_T两种情况，
# 第一种情况(a)继续执行算法即可找到最优解，第二种情况(b)（l, r_T）,还是由于连续性依据，一定是由
# （c）(l_T, r_T)或（d）(l_T, r'<r_T)发育而来，但是根据算法和最小覆盖的条件，(d)会变成（c）,
# （c）不能变成（b）。故（b）不存在，即同时满足连续性和算法的条件下不会生成（b）这种情况。所以一定会演变成
# （a）这种情况然后获得最优解
