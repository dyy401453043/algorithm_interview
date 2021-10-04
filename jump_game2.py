# leetcode 45，跳跃游戏II，time dfs > dp > greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        # dfs, 超时 82/106
        # result = float('inf')
        # def dfs(idx, times):
        #     nonlocal result
        #     if idx == len(nums)-1:
        #         if times < result:
        #             result = times
        #     elif idx > len(nums)-1:
        #         return
        #     else:
        #         if times >= result:
        #             return
        #         num = nums[idx]
        #         for stride in range(num,0,-1):
        #             dfs(idx+stride, times+1)
        # dfs(0,0)
        # return result

        # dp, 执行用时：24 ms, 在所有 Python3 提交中击败了5%的用户
        # length = len(nums)
        # result_table = [float('inf') for i in range(length)]
        # result_table[0] = 0
        # for i in range(1, length):
        #     for j in range(0, i):
        #         if nums[j] >= i - j:
        #             if result_table[j] + 1 < result_table[i]:
        #                 result_table[i] = result_table[j] + 1
        # return result_table[-1]

        # greedy, 执行用时：24 ms, 在所有 Python3 提交中击败了100%的用户
        length = len(nums)
        times = 0
        cur = -1
        bound = 0
        while bound < length -1:
            times += 1
            new_bound = 0
            for i in range(cur+1, bound+1):
                if nums[i] + i > new_bound:
                    new_bound = nums[i] + i
            cur = bound
            bound = new_bound
        return times
